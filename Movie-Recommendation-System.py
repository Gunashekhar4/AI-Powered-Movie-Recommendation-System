# Step 1: Import Libraries
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

# Step 2: Load the Dataset
# Assuming the MovieLens dataset is downloaded and extracted
movies = pd.read_csv('movies.csv')
ratings = pd.read_csv('ratings.csv')

# Step 3: Merge the ratings and movies DataFrames on 'movieId'
merged_data = pd.merge(ratings, movies, on='movieId')

# Step 4: Create a Pivot Table (User-Item Matrix)
# Create a pivot table with users as rows and movies as columns, and ratings as values
user_movie_matrix = merged_data.pivot_table(index='userId', columns='title', values='rating')

# Step 5: Replace NaN values with 0 for cosine similarity
user_movie_matrix.fillna(0, inplace=True)

# Step 6: Compute the Cosine Similarity between Users
user_similarity = cosine_similarity(user_movie_matrix)
user_similarity_df = pd.DataFrame(user_similarity, index=user_movie_matrix.index, columns=user_movie_matrix.index)

# Step 7: Create a Function to Recommend Movies
def recommend_movies(user_id, num_recommendations=5):
    # Find the most similar users to the given user_id
    similar_users = user_similarity_df[user_id].sort_values(ascending=False).index[1:num_recommendations+1]
    
    # Find movies that similar users have watched but the current user hasn't
    similar_users_movies = user_movie_matrix.loc[similar_users].mean(axis=0)
    user_movies = user_movie_matrix.loc[user_id]
    movies_to_recommend = similar_users_movies[user_movies == 0].sort_values(ascending=False).head(num_recommendations)
    
    return movies_to_recommend.index

# Step 8: Recommend Movies for a Specific User
user_id = 1  # Change this to any user ID you'd like
recommended_movies = recommend_movies(user_id, num_recommendations=5)
print(f"Recommended movies for user {user_id}:")
for movie in recommended_movies:
    print(movie)