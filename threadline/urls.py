from django.urls import path, include

urlpatterns = [
    # All public and CMS routes are handled by the content app
    path('', include('content.urls')),
]
