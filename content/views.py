from django.shortcuts import render, redirect
from django.http import Http404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.utils.text import slugify
from .models import Article, Category
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
    error_message = None
    if request.method == 'POST':
        email_or_username = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')

        # Check if login input is an email address, resolve to username
        username = email_or_username
        if '@' in email_or_username:
            user_obj = User.objects.filter(email=email_or_username).first()
            if user_obj:
                username = user_obj.username

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('dashboard')
        else:
            error_message = 'Invalid username/email or password.'

    return render(request, 'content/login.html', {
        'categories': data.all_categories(),
        'error_message': error_message,
    })


def logout_view(request):
    logout(request)
    return redirect('login')


def signup_view(request):
    error_message = None
    if request.method == 'POST':
        username = request.POST.get('username', '').strip()
        email = request.POST.get('email', '').strip()
        password = request.POST.get('password', '')
        password_confirm = request.POST.get('password_confirm', '')

        if not username or not email or not password:
            error_message = 'Please fill out all required fields.'
        elif password != password_confirm:
            error_message = 'Passwords do not match.'
        elif User.objects.filter(username__iexact=username).exists():
            error_message = 'That username is already taken.'
        elif User.objects.filter(email__iexact=email).exists():
            error_message = 'An account with that email address already exists.'
        else:
            user = User.objects.create_user(username=username, email=email, password=password)
            login(request, user)
            return redirect('dashboard')

    return render(request, 'content/signup.html', {
        'categories': data.all_categories(),
        'error_message': error_message,
        'username_val': request.POST.get('username', '') if request.method == 'POST' else '',
        'email_val': request.POST.get('email', '') if request.method == 'POST' else '',
    })


# ---------------- Dashboard (CMS) ----------------

@login_required(login_url='login')
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


@login_required(login_url='login')
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


@login_required(login_url='login')
def dashboard_article_create(request):
    if request.method == 'POST':
        title = request.POST.get('title', '').strip()
        slug_val = request.POST.get('slug', '').strip()
        excerpt = request.POST.get('excerpt', '').strip()
        content = request.POST.get('content', '').strip()
        status = request.POST.get('status', 'draft')
        category_slug = request.POST.get('category', '')
        author = request.POST.get('author', '').strip()
        image = request.POST.get('image', '').strip()

        slug_val = slugify(slug_val) if slug_val else slugify(title)
        if not slug_val:
            slug_val = 'article'

        base_slug = slug_val
        counter = 1
        while Article.objects.filter(slug=slug_val).exists():
            slug_val = f"{base_slug}-{counter}"
            counter += 1

        cat_obj = Category.objects.filter(slug=category_slug).first()
        Article.objects.create(
            title=title,
            slug=slug_val,
            excerpt=excerpt,
            content=content,
            status=status,
            category=cat_obj,
            author=author,
            image=image,
        )
        return redirect('dashboard_articles')

    cats = data.all_categories()
    return render(request, 'content/dashboard/article_create.html', {
        'article': None,
        'categories': cats,
        'all_categories': cats,
        'mode': 'create',
        'active': 'create',
    })


@login_required(login_url='login')
def dashboard_article_edit(request, pk):
    try:
        article_obj = Article.objects.get(pk=pk)
    except Article.DoesNotExist:
        raise Http404('Article not found')

    if request.method == 'POST':
        article_obj.title = request.POST.get('title', '').strip()
        slug_val = request.POST.get('slug', '').strip()
        slug_val = slugify(slug_val) if slug_val else slugify(article_obj.title)
        if not slug_val:
            slug_val = f'article-{article_obj.pk}'

        base_slug = slug_val
        counter = 1
        while Article.objects.filter(slug=slug_val).exclude(pk=article_obj.pk).exists():
            slug_val = f"{base_slug}-{counter}"
            counter += 1

        article_obj.slug = slug_val
        article_obj.excerpt = request.POST.get('excerpt', '').strip()
        article_obj.content = request.POST.get('content', '').strip()
        article_obj.status = request.POST.get('status', 'draft')
        category_slug = request.POST.get('category', '')
        article_obj.category = Category.objects.filter(slug=category_slug).first()
        article_obj.author = request.POST.get('author', '').strip()
        article_obj.image = request.POST.get('image', '').strip()
        article_obj.save()
        return redirect('dashboard_articles')

    article_dict = article_obj.to_dict()
    cats = data.all_categories()
    return render(request, 'content/dashboard/article_edit.html', {
        'article': article_dict,
        'categories': cats,
        'all_categories': cats,
        'mode': 'edit',
        'active': 'articles',
    })


@login_required(login_url='login')
def dashboard_article_delete(request, pk):
    if request.method == 'POST':
        Article.objects.filter(pk=pk).delete()
    return redirect('dashboard_articles')



@login_required(login_url='login')
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
