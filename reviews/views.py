from rest_framework.generics import ListCreateAPIView
from rest_framework.permissions import IsAdminUser
from .serializers import ReviewSerializer
from .models import Review

class AllReviews(ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAdminUser]
