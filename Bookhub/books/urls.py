from django.urls import path
from .views import BookSearchView, BookSerializer,book_list_view,RecommendationCreateView,RecommendationListView,LikeCreateView,CommentCreateView

urlpatterns = [
    path('booksearch/', BookSearchView.as_view(), name='book-search'),
    path('',book_list_view, name='book-list'),
    path('recommendations/', RecommendationListView.as_view(), name='recommendation-list'),
    path('recommendations/new/', RecommendationCreateView.as_view(), name='recommendation-create'),
    path('recommendations/like/', LikeCreateView.as_view(), name='like-create'),
    path('recommendations/comment/', CommentCreateView.as_view(), name='comment-create'),
]
