from django.urls import path
from rest_framework.routers import DefaultRouter
from book.views import BookViewSet

router = DefaultRouter()
router.register(r'', BookViewSet, basename='books')
urlpatterns = [
    
]