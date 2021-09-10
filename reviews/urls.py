from django.urls import path
from .views import AllReviews

urlpatterns = [
    path('', AllReviews.as_view(), name='all_reviews'),
]