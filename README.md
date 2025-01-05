# Movie Progress Tracker

Welcome to the Movie Progress Tracker! This full-stack web application helps users manage and track their movie-watching progress. Organize your movies into different lists, such as "**To Watch**", "**Watching**", and "**Watched**", and interact with an intuitive front-end interface. Admins can monitor user activities and manage the movie database.

## Table of Contents
- Features
- Tech Stack
- Installation
- Usage
- Project Structure
- Future Improvements

## User Features
**User Accounts**: Create and log in securely with unique usernames and passwords.
**Movie Tracking**: Manage movies across three categories:
- Watching: Movies the user is currently watching.
- To Watch: Movies the user plans to watch.
- Watched: Movies the user has finished watching.
**Interactive UI**: A dynamic front-end interface for seamless user interaction.
**Movie List Management**: Easily add, update or remove movies from any tracking category.
**Account settings**: Update profile details, including passwords, names, and email addresses.
**Search by Title**: Quickly locate movies using their titles.
**Search by Genre**: Discover movies base on specific genres.
**Password Protection**: Ensure secure login with password masking during input.

## Admin Features
**Admin Dashboard**: An admin account can monitor and manage user accounts and their movie lists.
**Database Management**: Add, edit, or delete movies in the database.

## Tech Stack
#### Back-End
- Flask: Python web framework for handling server-side logic.
- SQLAlchemy: ORM for database interactions.
- MySQL: relational database to store user and movie data.

#### Front-End
- HTML5: Markup for structure and content.
- CSS3: Styling with custom themes and responsiveness.
- Bootstrap: Predefined components for a polished UI.

## Installation 
### Prerequisities
> - python_version >= 3.13
>
> -  MySQL (or an alternative SQL-Compatible database)

### Steps 
1. Clone this repository:

		- git clone https://github.com/Future-Horizons-Python-Sept-2024/pep-progress-tracker-brangmai1.git

		- cd pep-progress-tracker-brangmai1

2. Install dependencies:

		- pip install -r requirements.txt
	
3. Configure the database:
	- Create a new MySQL database or your favorite DBMS.
	- Add .env file to the project, outside the static or templates folders.
	- Add the following key-value pairs to the .env file, and update the values with your own information.

		DB_NAME=my_database
		DB_USER=my_user
		DB_PASSWORD=my_password
		DB_HOST=localhost
		DB_PORT=3306


## Usage 
### Running the Application
1. Start the main application:

   		- python main.py

	or

		- flask run
2. Open your browser and navigate to **http://127.0.0.1:5000**.	
3. Sign up as a new user or sign in to an existing account.
4. User Features: Once signed in, you can:
	- Add movies to your To Watch, Watching, or Watched lists.
	- Update or remove movies from your lists.
	- Search for movies by title, genre or trend.
5. Admin users can access the admin dashboard to manage users and movies.

## Project Structure

	movie-progress-tracker/
	├── connect_database.py		# Database connection setup
	├── initial_setup.py		# Setup tables and initial data
	├── insert_data.py		# Insert initial data to the database
	├── tables.py			# ORM models for Users, Movies, Genres, etc.
	├── setup_user_account.py	# User account setup                 
	├── main.py			# Entry point to run the application
	├── .env			# Enviroment variables
	├── requirements.txt		# Python dependentcies
	└── README.md			# Project documentation

## Future Improvements
- Movie Recommendations: Recommend movies based on user preferences and watch history. 
- Social Sharing: Allow users to share their progress with friends.









