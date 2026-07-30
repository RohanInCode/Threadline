from django.shortcuts import render, redirect
from django.http import Http404
from . import data


# ---------------- Public ----------------

def home(request):
    published = data.published_articles()
    featured = published[0] if published else None
    trending = published[1:4]
    latest = published[:6]

    return render(request, 'content/home.html', {
        'featured': featured,
        'trending': trending,
        'latest': latest,
        'sports_preview': data.published_by_category('sports')[:3],
        'technology_preview': data.published_by_category('technology')[:3],
        'news_preview': data.published_by_category('news')[:3],
        'entertainment_preview': data.published_by_category('entertainment')[:3],
        'categories': data.all_categories(),
    })


def category(request, slug):
    cat = data.category_by_slug(slug)
    if not cat:
        raise Http404('Category not found')
    articles = data.published_by_category(slug)
    return render(request, 'content/category.html', {
        'category': cat,
        'articles': articles,
        'categories': data.all_categories(),
    })


def article_detail(request, slug):
    article = data.article_by_slug(slug)
    if not article:
        raise Http404('Article not found')
    return render(request, 'content/article_detail.html', {
        'article': article,
        'category': data.category_by_slug(article['category']),
        'related': data.related_articles(article),
        'categories': data.all_categories(),
    })


def search(request):
    query = request.GET.get('q', '')
    results = data.search_articles(query)
    return render(request, 'content/search.html', {
        'query': query,
        'results': results,
        'categories': data.all_categories(),
    })


def login_view(request):
    return render(request, 'content/login.html', {
        'categories': data.all_categories(),
    })


# ---------------- Dashboard (CMS) ----------------

def dashboard(request):
    st = data.stats()
    return render(request, 'content/dashboard/overview.html', {
        'total_articles': st['total'],
        'published_count': st['published'],
        'drafts_count': st['drafts'],
        'categories_count': st['categories'],
        'recent_articles': data.all_articles()[:6],
        'active': 'dashboard',
    })


def dashboard_articles(request):
    q = request.GET.get('q', '').strip().lower()
    cat = request.GET.get('category', '').strip()
    status = request.GET.get('status', '').strip()

    articles = data.all_articles()
    if q:
        articles = [a for a in articles if q in a['title'].lower()]
    if cat:
        articles = [a for a in articles if a['category'] == cat]
    if status:
        articles = [a for a in articles if a['status'] == status]

    return render(request, 'content/dashboard/articles.html', {
        'articles': articles,
        'categories': data.all_categories(),
        'query': q,
        'category_filter': cat,
        'status_filter': status,
        'active': 'articles',
    })


def dashboard_article_create(request):
    return render(request, 'content/dashboard/article_create.html', {
        'article': None,
        'all_categories': data.all_categories(),
        'mode': 'create',
        'active': 'create',
    })


def dashboard_article_edit(request, pk):
    article = data.article_by_id(pk)
    if not article:
        raise Http404('Article not found')
    return render(request, 'content/dashboard/article_edit.html', {
        'article': article,
        'all_categories': data.all_categories(),
        'mode': 'edit',
        'active': 'articles',
    })


def dashboard_categories(request):
    categories = []
    for cat in data.all_categories():
        categories.append({
            **cat,
            'article_count': len(data.articles_by_category(cat['slug'])),
        })
    return render(request, 'content/dashboard/categories.html', {
        'categories': categories,
        'active': 'categories',
    })
