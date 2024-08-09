import requests

GOOGLE_BOOKS_API_URL = 'https://www.googleapis.com/books/v1/volumes'

def fetch_books_by_query(query):
    try:
        response = requests.get(GOOGLE_BOOKS_API_URL, params={'q': query})
        response.raise_for_status()
        data = response.json()
        books = []
        if 'items' in data:
            for item in data['items']:
                volume_info = item['volumeInfo']
                book = {
                    'title': volume_info.get('title'),
                    'author': ', '.join(volume_info.get('authors', [])),
                    'description': volume_info.get('description', ''),
                    'cover_image': volume_info.get('imageLinks', {}).get('thumbnail', ''),
                    'average_rating': volume_info.get('averageRating', None),
                    'ratings_count': volume_info.get('ratingsCount', 0)
                }
                books.append(book)
        return books
    except requests.exceptions.RequestException as e:
        print(f"Error fetching data from Google Books API: {e}")
        return None
