"""
content/data.py — Data access layer for views.py

All functions return plain dicts (via .to_dict()) so that views.py and
templates require zero changes when switching from mock data to the database.
"""

from .models import Article, Category


# ---------------------------------------------------------------------------
# Category helpers
# ---------------------------------------------------------------------------

def all_categories():
    return [c.to_dict() for c in Category.objects.all()]


def category_by_slug(slug):
    try:
        return Category.objects.get(slug=slug).to_dict()
    except Category.DoesNotExist:
        return None


# ---------------------------------------------------------------------------
# Article helpers
# ---------------------------------------------------------------------------

def all_articles():
    """Return every article regardless of status, newest first."""
    return [a.to_dict() for a in Article.objects.select_related('category').order_by('-created_at')]


def published_articles():
    """Return only published articles, newest first."""
    return [a.to_dict() for a in Article.objects.filter(status='published').select_related('category').order_by('-created_at')]


def published_by_category(slug):
    """Published articles for a single category."""
    return [
        a.to_dict()
        for a in Article.objects.filter(status='published', category__slug=slug)
        .select_related('category')
        .order_by('-created_at')
    ]


def articles_by_category(slug):
    """All articles (any status) for a single category."""
    return [
        a.to_dict()
        for a in Article.objects.filter(category__slug=slug)
        .select_related('category')
        .order_by('-created_at')
    ]


def article_by_slug(slug):
    try:
        return Article.objects.select_related('category').get(slug=slug).to_dict()
    except Article.DoesNotExist:
        return None


def article_by_id(pk):
    """Look up by integer primary key."""
    try:
        return Article.objects.select_related('category').get(pk=pk).to_dict()
    except Article.DoesNotExist:
        return None


def related_articles(article, limit=3):
    """Articles in the same category, excluding the current one."""
    return [
        a.to_dict()
        for a in Article.objects.filter(
            status='published',
            category__slug=article['category']
        ).exclude(slug=article['slug'])
        .select_related('category')
        .order_by('-created_at')[:limit]
    ]


def search_articles(query):
    """Case-insensitive search across title and excerpt."""
    from django.db.models import Q
    q = query.strip()
    if not q:
        return []
    return [
        a.to_dict()
        for a in Article.objects.filter(
            Q(title__icontains=q) | Q(excerpt__icontains=q),
            status='published'
        ).select_related('category').order_by('-created_at')
    ]


# ---------------------------------------------------------------------------
# Dashboard stats
# ---------------------------------------------------------------------------

def stats():
    """Summary counts for the dashboard overview cards."""
    total     = Article.objects.count()
    published = Article.objects.filter(status='published').count()
    drafts    = Article.objects.filter(status='draft').count()
    cats      = Category.objects.count()
    return {
        'total':      total,
        'published':  published,
        'drafts':     drafts,
        'categories': cats,
    }
