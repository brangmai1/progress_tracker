# Movie Progress Tracker

Welcome to the Movie Progress Tracker! This application helps users manage and track their movie-watching progress by organizing movies into different lists, such as To Watch, Watching, and Watched. It also includes an admin feature to oversee users' progress and manage the movie database.

## Table of Contents
- Features
- Tech Stack
- Installation
- Usage
- Project Structure
- Future Improvements

## Features
#### User Accounts: Users can sign up and log in with a unique username.
#### Movie Tracking: Organize movies into three categories:
- To Watch: Movies the user plans to watch.
- Watching: Movies the user is currently watching.
- Watched: Movies the user has finished.
#### Admin Dashboard: An admin account can view and manage user accounts and movie lists.
#### Search by Movie Title: Find movies by movie titles.
#### Search by Genre: Find movies by specific genres.
#### Password Protection: Secure user login with password masking.

## Tech Stack
#### Backend: Python, SQLAlchemy ORM
#### Database: MySQL (or your preferred relational database)
#### Other Libraries: Pandas(for data manipulation and analysis)

## Installation 
### Prerequisities
- Python 3.x
_ MySQL (or an alternative SQL-Compatible database)

### Steps 
1. Clone this repository:

		- git clone https://github.com/yourusername/movie-progress-tracker.git
		- cd movie-progress-tracker

2. Install dependencies:

		- pip install -r requirements.txt
	
4. Set up your MySQL database
- Create a new MySQL database name movie_progress_tracker
- Update the database connection details in connect_database.py to match your MySQL setup.

## Usage 
### Running the Application
1. Start the main application:

   		- python3 main.py
   
2. Sign up as a user or sign in to an existing account.
3. User Features: Once signed in, you can:
- Add movies to your To Watch, Watching, or Watched lists.
- Update status or delete movies from your movie lists.
- View movie lists and track your watching progress.
- Search movies by movie or genre.

## Project Structure

	movie-progress-tracker/
	├── connect_database.py       # Database connection setup
	├── initial_setup.py          # Setup tables and initial data
	├── insert_data.py		      # Insert initial data to the database
	├── tables.py                 # ORM models for Users, Movies, Genres, etc.
	├── setup_user_account.py     # User account setup                 
	├── main.py                   # Entry point to run the application
	└── README.md                 # Project documentation

## Future Improvements
- Movie Recommendations: Recommend movies based on the user's genre preferences. 
- Front-End Interface: Develop an intuitive front-end to simplify user interactions and enhance the overall experience. 
- Social Sharing: Allow users to share their progress with friennds.








