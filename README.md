# Question Pair Similarity Classification

## Introduction
The goal of this project is to check if two questions mean the same thing. This is done using text processing, data analysis, and machine learning.

## Steps Taken:
### 1. Loaded the Data
- Used a dataset with 404,290 rows and 6 columns.
- To save time, only 50,000 rows were used for training.

### 2. Data Cleaning
- Removed special characters and HTML tags from the text.
- Used tokenization to break sentences into words.
- Removed stopwords (words that don’t add much meaning).

### 3. Exploratory Data Analysis (EDA)
- Checked how many duplicate questions exist.
- Visualized word distributions using graphs.

### 4. Feature Engineering
- Used TF-IDF and word embeddings to convert text into numbers.

### 5. Model Training
- Tried different models like Logistic Regression, Random Forest, and Neural Networks.
- Compared models based on accuracy and F1-score.

### 6. Results
- The best model achieved **XX% accuracy** (replace with actual number).
- Created a confusion matrix to analyze errors.

### 7. Deployment
- Built a **Streamlit web app** so users can input questions and check if they are similar.
- The app is available at: [https://questionquora.streamlit.app/](https://questionquora.streamlit.app/)

