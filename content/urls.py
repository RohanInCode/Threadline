from django.urls import path
from . import views

urlpatterns = [
    # Public
    path('', views.home, name='home'),
    path('category/<slug:slug>/', views.category, name='category'),
    path('article/<slug:slug>/', views.article_detail, name='article_detail'),
    path('search/', views.search, name='search'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('signup/', views.signup_view, name='signup'),

    # Dashboard (CMS)
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/articles/', views.dashboard_articles, name='dashboard_articles'),
    path('dashboard/articles/create/', views.dashboard_article_create, name='dashboard_article_create'),
    path('dashboard/articles/<int:pk>/edit/', views.dashboard_article_edit, name='dashboard_article_edit'),
    path('dashboard/categories/', views.dashboard_categories, name='dashboard_categories'),
]
