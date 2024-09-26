# Gamer-Rater API

Welcome to the **Gamer-Rater API**, a platform where players can discuss, share information, and rate the games they play. This API allows users to create unique entries for games, upload images, submit ratings, write reviews, and browse a comprehensive list of games with sorting and filtering options.

## Features

- **Game Creation**: Players can create unique game entries, ensuring that no two users create the same game in the system.
- **Image Uploads**: Players can upload images to showcase the games they are playing.
- **Game Ratings**: Players can rate the games they play on a scale of 1-5 stars.
- **Game Reviews**: Players can write detailed reviews of the games they have played.
- **Search & Sorting**: Games can be searched by title, and sorted by category or year of release.
- **Average Rating**: Games display an average rating, calculated from all user ratings, implemented via a custom model property.

## API Endpoints

<details>

### Authentication

- `POST /auth/login/`: User login.
- `POST /auth/register/`: User registration.

### Games

- `GET /games/`: List all games with search and sort options.
- `POST /games/`: Create a new game (unique entry for each player).
- `GET /games/:id/`: Retrieve details of a specific game.
- `PUT /games/:id/`: Update game information (if owner).
- `DELETE /games/:id/`: Delete a game entry (if owner).

### Images

- `POST /games/:id/images/`: Upload an image for a specific game.

### Ratings

- `POST /games/:id/ratings/`: Submit a rating for a specific game.
- `GET /games/:id/ratings/`: Retrieve the average rating of a game.

### Reviews

- `POST /games/:id/reviews/`: Write a review for a game.
- `GET /games/:id/reviews/`: List all reviews for a specific game.
</details>

## Installation

1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/gamer-rater-api.git
   ```

2. Create development environment:
   ```sh
   pipenv shell
   ```

3. Install dependencies:
   ```sh
   pipenv install
   ```
   
4. Run migrations:
   ```sh
   python manage.py migrate
   ```

5. Start the development server:
   ```sh
   python manage.py runserver
