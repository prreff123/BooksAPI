from django.shortcuts import render
from rest_framework.permissions import IsAuthenticated
from rest_framework import generics, status
from rest_framework.response import Response
from .serializer import BookSerializer,RecommendationSerializer,LikeSerializer,CommentSerializer
from .utils import fetch_books_by_query
from .models import Book,Like,Comment,Recommendation

class RecommendationCreateView(generics.CreateAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer
    # permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        book_data = self.request.data.get('book')
        if not book_data:
            return Response({'error': 'Book data is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        google_books_id = book_data.get('google_books_id')
        if not google_books_id:
            return Response({'error': 'Google Books ID is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        book, created = Book.objects.get_or_create(
            google_books_id=google_books_id, 
            defaults=book_data
        )
        serializer.save(user=self.request.user, book=book,created=created)

class RecommendationListView(generics.ListAPIView):
    queryset = Recommendation.objects.all()
    serializer_class = RecommendationSerializer

    def get_queryset(self):
        queryset = super().get_queryset()
        genre = self.request.query_params.get('genre')
        if genre:
            queryset = queryset.filter(book__genre=genre)
        return queryset.order_by('-created_at')

class LikeCreateView(generics.CreateAPIView):
    queryset = Like.objects.all()
    serializer_class = LikeSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CommentCreateView(generics.CreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)                    

class BookSearchView(generics.GenericAPIView):
    serializer_class = BookSerializer

    def get(self, request, *args, **kwargs):
        query = request.query_params.get('q')
        if not query:
            return Response({'error': 'Query parameter is required'}, status=status.HTTP_400_BAD_REQUEST)
        
        books = fetch_books_by_query(query)
        if books is not None:
            return Response(books, status=status.HTTP_200_OK)
        return Response({'error': 'Unable to fetch data from Google Books API'}, status=status.HTTP_503_SERVICE_UNAVAILABLE)

def book_list_view(request):
    query = request.GET.get('q', '')
    books = []
    if query:
        books = fetch_books_by_query(query) or []
    return render(request, 'book_list.html', {'books': books, 'query': query})