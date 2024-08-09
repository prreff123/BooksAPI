1. Introduction
BookHub API is a community-driven platform for sharing and exploring book recommendations. The backend is built using Django Rest Framework and integrates with the Google Books API to fetch and manage book data.

2. Features
Search for books using the Google Books API.
Submit and retrieve community book recommendations.
Like and comment on recommendations.

3. Setup Instructions
Prerequisites
Python 3.12.2
Django 5.0.5
Django Rest Framework 3.13+
A Google Books API key

4. Installation
pip install django
pip install django-rest framework
Run Migrations: python manage.py migrate
Create a Superuser: python manage.py createsuperuser
Run the Development Server: python manage.py runserver

5. API Endpoints
User Authentication
Register: POST /api/register/
Login: POST /api/token/
Refresh Token: POST /api/token/refresh/

6. Community Book Recommendations
Create Recommendation: POST recommendations/new/
List Recommendations: GET recommendations/
Retrieve a Recommendation: GET /api/recommendations/<id>/

7. Likes and Comments
Like a Recommendation: POST recommendations/<id>/like/
Comment on a Recommendation: POST recommendations/comment/

8. Serving the Frontend
You can serve these HTML files directly through Django by placing them in your templates folder and configuring your views to render these templates.

9. Troubleshooting
Issue: Incorrect type. Expected pk value, received list.
Solution: Ensure that the user field is passed as an integer and not as a list.

10. Issue: The submitted data was not a file. Check the encoding type on the form.
Solution: Ensure the cover_image field is sent as a file, using form-data in Postman.

11. Contributing
If you wish to contribute, please fork the repository, create a new branch, and submit a pull request. Ensure all new code follows the project’s coding standards and includes relevant tests.
