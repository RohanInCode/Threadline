from django.core.management.base import BaseCommand
from django.utils.text import slugify
from content.models import Article


class Command(BaseCommand):
    help = 'Find and fix any Article slugs that contain invalid characters (spaces, ?, etc.)'

    def handle(self, *args, **options):
        fixed = 0
        for article in Article.objects.all():
            clean = slugify(article.slug)
            if clean != article.slug:
                self.stdout.write(
                    f'Fixing: {repr(article.slug)} → {repr(clean)}'
                )
                # Ensure uniqueness
                base = clean or f'article-{article.pk}'
                candidate = base
                counter = 1
                while Article.objects.filter(slug=candidate).exclude(pk=article.pk).exists():
                    candidate = f'{base}-{counter}'
                    counter += 1
                article.slug = candidate
                article.save(update_fields=['slug'])
                fixed += 1

        if fixed:
            self.stdout.write(self.style.SUCCESS(f'Done. Fixed {fixed} article(s).'))
        else:
            self.stdout.write(self.style.SUCCESS('No bad slugs found — all articles are clean.'))
