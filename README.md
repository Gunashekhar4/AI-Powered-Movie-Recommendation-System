# 🎬 Movie Recommendation System

## 📌 Project Overview
A personalized Movie Recommendation System built using **Machine Learning** and **Collaborative Filtering**. By analyzing historical user ratings and computing behavioral overlap between users, the system predicts and recommends unseen movies that a target user is highly likely to enjoy. 

## 📂 Dataset
The system utilizes the benchmark **MovieLens Dataset**, processing two primary files:
*   **`movies.csv`**: Contains metadata for 10,000 movies (Features: `movieId`, `title`, `genres`).
*   **`ratings.csv`**: Contains user interactions and feedback (Features: `userId`, `movieId`, `rating`, `timestamp`). Represents 1 million ratings from over 600 users on a 0 to 5 scale.

## 🛠️ Technologies & Libraries
*   **Python**: Core programming language.
*   **Pandas**: Data manipulation, dataset merging, and pivot table creation.
*   **NumPy**: Numerical array operations.
*   **Scikit-Learn**: Mathematical modeling (specifically calculating Cosine Similarity).

## ⚙️ Methodology & Workflow
1.  **Data Preprocessing**: Merges `movies.csv` and `ratings.csv` using the common `movieId` column.
2.  **User-Item Matrix**: Generates a structured pivot table where rows represent users, columns represent movies, and cells contain ratings. Unrated movies are filled with `0`.
3.  **Similarity Computation**: Applies **Cosine Similarity** to measure the angle between user rating vectors, resulting in a comprehensive user-similarity matrix.
4.  **Recommendation Generation**:
    *   Identifies the top $N$ users with preferences most similar to the target user.
    *   Aggregates and averages the ratings from these similar users for movies the target user *has not yet watched*.
    *   Ranks the movies by predicted score and returns the top recommendations.

## 🚀 Local Installation & Usage

### 1. Clone the Repository
git clone <your-repository-url>
cd <your-repository-folder>
2. Install Dependencies
Ensure Python is installed on your system. Run the following command to install required libraries:
pip install pandas numpy scikit-learn
3. Folder Structure
Ensure your project files are organized as follows before running:
├── data/
│   ├── movies.csv
│   └── ratings.csv
├── app.py             # Main execution script
└── README.md
4. Run the Engine
Execute the script to generate recommendations:
python app.py
📊 Sample Output
Example of generating the top 5 movie recommendations for User 1:
Recommended movies for user 1:
- Aliens (1986)
- Hunt for Red October, The (1990)
- Blade Runner (1982)
- Godfather, The (1972)
- Terminator 2: Judgment Day (1991)
📈 Evaluation Metrics
The effectiveness of recommendation systems is typically measured using:
• Precision: Proportion of recommended movies that are actually relevant to the user.
• Recall: How many of the relevant movies were successfully recommended.
• RMSE (Root Mean Square Error): Evaluates the accuracy of the system's predicted ratings against actual ratings.
🔮 Future Enhancements
• Hybrid Recommendation Models: Combine Collaborative Filtering with Content-Based Filtering (utilizing movie genres/tags) to overcome the "Cold Start" problem for brand new users or movies.
• Deep Learning: Implement neural networks to capture complex, non-linear patterns in user behavior and viewing history.
• Real-Time Adaptation: Update similarity scores and recommendations dynamically as users provide new ratings on the fly.
