# ML-Powered Movie Recommendation System

## Overview
This project implements an intelligent movie recommendation system using machine learning algorithms. The system analyzes user preferences and viewing history through collaborative filtering techniques to provide personalized movie recommendations. By leveraging user similarity metrics and rating patterns, the system identifies movies that align with individual user preferences, enhancing the overall user experience.

## Project Objective
The primary goal is to build a recommendation engine that utilizes collaborative filtering methodology to suggest movies based on:
- User ratings and preferences
- Similarity between users with comparable tastes
- Historical viewing patterns
- Movie characteristics and metadata

## Key Algorithm: Collaborative Filtering
The system employs user-based collaborative filtering, which works by:
1. Creating a user-item matrix with users as rows and movies as columns
2. Computing cosine similarity between all users to identify similar preferences
3. Recommending movies watched by similar users that the target user hasn't seen
4. Ranking recommendations based on average ratings from similar users

## Technical Stack
- **Programming Language:** Python
- **Data Processing:** Pandas, NumPy
- **Machine Learning:** Scikit-learn
- **Algorithm:** Cosine Similarity for User-Based Collaborative Filtering
- **Data Source:** MovieLens Dataset

## Dataset Structure
The system works with the following data files:
- **movies.csv:** Contains movie information (movieId, title)
- **ratings.csv:** Contains user ratings (userId, movieId, rating)

## Features
- Generates personalized movie recommendations for individual users
- Utilizes cosine similarity to identify users with similar preferences
- Filters recommendations to exclude movies already watched by the user
- Returns top N recommendations (customizable parameter)
- Processes and merges user ratings with movie metadata
- Handles sparse data by replacing missing values with 0

## Project Implementation Steps

### Step 1: Data Loading and Preprocessing
- Import necessary libraries (pandas, numpy, scikit-learn)
- Load movies.csv and ratings.csv datasets
- Merge datasets on movieId to create consolidated data

### Step 2: User-Item Matrix Construction
- Create a pivot table with users as rows and movies as columns
- Populate cells with user ratings
- Replace NaN values with 0 for similarity calculations

### Step 3: Similarity Computation
- Calculate cosine similarity between all user vectors
- Create a similarity matrix for easy lookup of similar users
- Store results in a pandas DataFrame for efficient access

### Step 4: Recommendation Engine
- Identify the most similar users to the target user
- Extract movies watched by similar users
- Calculate average ratings from similar users
- Filter out movies already rated by the target user
- Sort by ratings and return top recommendations

### Step 5: Output Generation
- Return movie titles as recommendations
- Display recommendations in readable format
- Support customizable number of recommendations (default: 5)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/Gunashekhar4/ML-Powered-Movie-Recommendation-System.git
```

2. Navigate to the project directory:
```bash
cd ML-Powered-Movie-Recommendation-System
```

3. Install the required dependencies:
```bash
pip install -r requirements.txt
```

## Running the System

To run the `Movie-Recommendation-System.py` file and get movie recommendations, follow the instructions below:

1. **Make sure you have Python installed on your system.**  
   You can download it from [python.org](https://www.python.org/downloads/).

2. **Install the required packages:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Open your command line interface (Terminal, Command Prompt, etc.).**

4. **Navigate to the directory where the Movie-Recommendation-System.py file is located:**
   ```bash
   cd ML-Powered-Movie-Recommendation-System
   ```

5. **Run the script:**
   ```bash
   python Movie-Recommendation-System.py
   ```

6. **Enter your input when prompted in the terminal:**
   - When the script runs, it will prompt you to enter the User ID
   - Enter the User ID (for example: `1`, `5`, `100`, etc.)
   - Press Enter
   - Next, you will be asked to enter the number of recommendations
   - Enter the number (for example: `5`, `10`, etc.)
   - Press Enter

7. **View the recommendations:**
   - The system will display personalized movie recommendations in the terminal based on your input

## Example Execution

```bash
$ python Movie-Recommendation-System.py
Enter the User ID: 1
Enter the number of recommendations: 5
Recommended movies for user 1:
Aliens (1986)
Hunt for Red October, The (1990)
Blade Runner (1982)
Godfather, The (1972)
Terminator 2: Judgment Day (1991)
```

## Required Dependencies
- pandas
- numpy
- scikit-learn

## Usage

### Basic Usage
```python
# Import the recommendation function
from recommendation_system import recommend_movies

# Get recommendations for a specific user
user_id = 1
recommended_movies = recommend_movies(user_id, num_recommendations=5)

# Display results
print(f"Recommended movies for user {user_id}:")
for movie in recommended_movies:
    print(movie)
```

### Example Output
```
Recommended movies for user 1:
Aliens (1986)
Hunt for Red October, The (1990)
Blade Runner (1982)
Godfather, The (1972)
Terminator 2: Judgment Day (1991)
```

### Customization Options
- **user_id:** Specify any user ID from the dataset
- **num_recommendations:** Adjust the number of recommendations (default: 5)

## How It Works

1. **Load Data:** The system reads MovieLens dataset files containing user ratings and movie information
2. **Create Matrix:** Constructs a user-movie matrix from the merged data
3. **Compute Similarity:** Calculates cosine similarity between all users to identify preference patterns
4. **Generate Recommendations:** For a given user, finds similar users and recommends their highly-rated unwatched movies
5. **Rank Results:** Returns top recommendations sorted by average ratings from similar users

## Data Flow
```
Load CSV Files → Merge Data → Create User-Item Matrix → 
Compute Cosine Similarity → Select Similar Users → 
Extract Recommendations → Sort by Rating → Return Top N Movies
```

## Algorithm Advantages
- **Simplicity:** Easy to understand and implement
- **Personalization:** Tailored recommendations based on user similarity
- **Scalability:** Efficient with moderate dataset sizes
- **No Content Analysis:** Works without requiring movie feature data
- **Diverse Recommendations:** Leverages diverse user preferences

## Performance Considerations
- Matrix operations are optimized using NumPy
- Cosine similarity computation is efficient for medium-sized datasets
- Sparse data handling prevents memory issues
- Pivot table structure enables fast user lookups

## Potential Enhancements
- Integration of content-based filtering
- Hybrid recommendation approach combining collaborative and content-based methods
- Matrix factorization techniques (SVD, NMF)
- Real-time recommendation updates
- Support for cold-start problem solutions
- Incorporation of temporal dynamics
- Implementation of item-based collaborative filtering
- Rating prediction accuracy metrics

## Project Structure
```
ML-Powered-Movie-Recommendation-System/
├── README.md
├── requirements.txt
├── Movie-Recommendation-System.py
├── movies.csv
└── ratings.csv
```

## Notes
- The system requires properly formatted CSV files with correct column names
- User IDs and movie IDs should be present in both datasets for proper merging
- Recommendation quality improves with larger datasets
- The system handles missing values gracefully
- Ensure CSV files are in the same directory as the Python script

## Troubleshooting

### FileNotFoundError for CSV files
- Verify that `movies.csv` and `ratings.csv` are in the project directory
- Check that file paths in the script match your actual file locations

### Invalid User ID
- Enter a user ID that exists in your dataset
- Check the dataset to see valid user ID ranges

### Module Import Error
- Ensure all dependencies are installed: `pip install -r requirements.txt`
- Verify Python version compatibility

## Contributing
If you'd like to contribute, please fork the repository and submit a pull request.
