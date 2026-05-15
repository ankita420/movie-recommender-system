Movie Recommender System
A content-based movie recommendation engine built with Python, leveraging Machine Learning techniques to suggest movies based on their metadata (genres, keywords, cast, and crew).

🚀 Overview

This project uses the TMDB 5000 Movies Dataset to find similarities between films. By processing text data and converting it into vectors, the system can recommend the top 5 most similar movies to any user-selected title.

🛠️ Tech Stack

Language: Python 3.x

Data Manipulation: Pandas, NumPy

Machine Learning: Scikit-Learn (CountVectorizer, Cosine Similarity)

Frontend: Streamlit

Serialization: Pickle

📊 How it Works

Data Preprocessing: The system cleans the dataset by merging the movies and credits dataframes. It extracts relevant tags from JSON-formatted columns like genres and cast.

Vectorization: Using Bag of Words (CountVectorizer), the textual tags are converted into numerical vectors.

Similarity Measurement: Cosine Similarity is calculated between all movie vectors. This distance determines how "close" one movie is to another in terms of content.

Deployment: A Streamlit web app provides an intuitive interface for users to select a movie and view recommendations instantly.

📂 Project Structure

movie-recommender-system.ipynb: The Jupyter Notebook containing the full Data Analysis, Feature Engineering, and Model Building pipeline.

app.py: The Streamlit application script for the web interface.

movie_dict.pkl: Preprocessed movie data stored in dictionary format.

movies.pkl: The processed DataFrame used for the app.

Note on similarity.pkl: Due to GitHub's file size limitations, the similarity matrix file (similarity.pkl) is not included in this repository. To run the project locally, you can generate this file by running the Jupyter Notebook provided.


⚙️ Installation & Usage

Clone the repository:

Bash
git clone https://github.com/yourusername/movie-recommender-system.git

cd movie-recommender-system

Install dependencies:

Bash
pip install -r requirements.txt
Run the application:

Bash
streamlit run app.py

📈 Future Improvements

Integrate the TMDB API to display movie posters in the UI.

Incorporate Collaborative Filtering to suggest movies based on user ratings.

Deploy the application using Heroku or AWS.

