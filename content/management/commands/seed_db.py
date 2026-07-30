"""
Management command: seed_db

Imports all categories and articles from mock_data.py into the database.
Safe to run multiple times — uses get_or_create to avoid duplicates.

Usage:
    python manage.py seed_db
"""

from django.core.management.base import BaseCommand
from django.utils.dateparse import parse_datetime
from django.utils import timezone

from content.mock_data import CATEGORIES, ARTICLES
from content.models import Category, Article


class Command(BaseCommand):
    help = 'Seed the database with mock categories and articles from mock_data.py'

    def handle(self, *args, **options):
        self.stdout.write('--- Seeding categories ---')
        cat_map = {}
        for cat_data in CATEGORIES:
            cat, created = Category.objects.get_or_create(
                slug=cat_data['slug'],
                defaults={
                    'name':        cat_data['name'],
                    'description': cat_data.get('description', ''),
                }
            )
            cat_map[cat.slug] = cat
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'  [{status}] {cat.name}')

        self.stdout.write('\n--- Seeding articles ---')
        for a in ARTICLES:
            cat_slug = a.get('category', '')
            category = cat_map.get(cat_slug)

            # Parse the human-readable date string or fall back to now
            created_at = timezone.now()

            article, created = Article.objects.get_or_create(
                slug=a['slug'],
                defaults={
                    'title':      a['title'],
                    'excerpt':    a.get('excerpt', ''),
                    'content':    a.get('content', ''),
                    'image':      a.get('image', ''),
                    'author':     a.get('author', ''),
                    'category':   category,
                    'status':     a.get('status', 'draft'),
                    'featured':   a.get('featured', False),
                    'created_at': created_at,
                }
            )
            status = 'Created' if created else 'Already exists'
            self.stdout.write(f'  [{status}] {article.title}')

        total_cats     = Category.objects.count()
        total_articles = Article.objects.count()
        self.stdout.write(
            self.style.SUCCESS(
                f'\nDone -- {total_cats} categories, {total_articles} articles in database.'
            )
        )
