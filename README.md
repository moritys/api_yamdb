# API for YaMDb

This project collects reviews, ratings and comments on movies, books, music and pretty much anything else you can imagine!
(Pretty much like IMDb, but far cooler (at least the backend part))

## Important aspects
 1. Latest API version is `v1`
 2. All API urls start with `api/<api_version>/...`
 3. This API implies that you have at least superficial knowledge of what YaMDb is and how it works
 4. Authentication by JWT-tokens

## How to install it on your VM
The following points are roughly as they should be. You should do as you are accustomed to - it's your machine, you know it best.
**NB!** If you are a Mac user, use `python3` instead of `python` 

1. Clone this project - `git clone https://github.com/moritys/api_yamdb`

2. Install virtual environment - `python -m venv venv`

3. Activate virtual environment - `venv/Scripts/activate`

4. Install necessary requirements - `pip install -r requirements.txt`

5. Change directory - `cd api_yamdb`

6. Make migrations - `python manage.py migrate`

7. Run server - `python manage.py runserver`

8. Enjoy making requests to our service :)

## What current-version API can do
1. Get all genres, along with categories, titles and their corresponding reviews and comments
2. Make, update and delete reviews and comments
3. Making, updating and deleting genres, categories and titles can be done only by a user with Administrator permission
4. Everything, except getting your own authorization details or updating them, can be done only by a user with Administrator permission

## Examples of usage
1. GET-requests (**NB!** The resulting JSON objects are paginated and therefore do not have all desired objects in one bundle):
 - Get all:
   - Reviews - `titles/{title_id}/reviews/`
   - Comments - `titles/{title_id}/reviews/{review_id}/comments/`
   - All categories, genres and titles - `categories/`, `genres/` and `titles/` respectively
 - Get one specific:
   - Review - `titles/{title_id}/reviews/{review_id}/`
   - Comment - `titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`

2. POST-requests:
 - Reviews - `titles/{title_id}/reviews/`, with required `text` and `score` fields
 - Comments - `titles/{title_id}/reviews/{review_id}/comments/`, with a required `text` field

3. PATCH-requests:
 - Reviews - `titles/{title_id}/reviews/{review_id}/`, with required `text` and `score` fields
 - Comments - `titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`, with a required `text` field

4. DELETE-requests:
 - Reviews - `titles/{title_id}/reviews/{review_id}/`
 - Comments - `titles/{title_id}/reviews/{review_id}/comments/{comment_id}/`

5. Authorization details:
 - Get your authorization details - GET-request to `users/me/`
 - Update your authorization details - PATCH-request to `users/me/`, with required `username` and `email` fields and three other optional fields - `first_name`, `last_name` and `bio`

## Authors
 - Team Lead - @moritys
 - And last, but not least - @Osokin-Nikita and @StriderDunedain
 
## Afterword
We hope you get the best of experience from using our service. If you happen to notice some bugs that have slipped us or simply want to share your experience, feel free to reach out.
