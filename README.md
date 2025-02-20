# 📌 Question Pair Similarity Classification

## **Introduction**  
This project aims to build a **machine learning system** that can identify whether two questions have the **same meaning** or not. Using **text processing, data analysis, and machine learning models**, we compare question pairs to detect duplicates.  

---

## **📂 1. Reading the Dataset**  
The dataset contains **404,290 question pairs**, but training on the full dataset requires too much time.  
✅ To optimize performance, we **randomly selected 50,000 rows** for training.  

---

## **📊 2. Exploratory Data Analysis (EDA)**  
Before training the model, we analyzed the data:  
✅ Checked the **number of duplicate questions**.  
✅ Used **graphs and charts** to visualize word distributions.  

---

## **🔍 3. Text Preprocessing**  
Since raw text contains **noise**, we cleaned the questions using:  
✅ **Removing HTML tags & punctuation**  
✅ **Converting text to lowercase**  
✅ **Removing stopwords** (e.g., "is", "the", "a")  
✅ **Lemmatization** (e.g., "running" → "run")  
✅ **Replacing special characters** (e.g., "$" → "dollar")  

---

## **⚙️ 4. Feature Engineering**  
We added extra features to help the model understand **question similarities**:  
✅ **Basic Features:** Question length, word count, and shared words.  
✅ **Token-based Features:** Checked if questions start or end with the same word.  
✅ **Fuzzy Matching Features:** Compared phrase similarity.  
✅ **TF-IDF Vectorization:** Converted text into numerical features for model training.  

---

## **🤖 5. Model Building & Training**  
The dataset was split into:  
✅ **80% Training Data**  
✅ **20% Test Data**  

We tested multiple machine learning models:  
✅ **Logistic Regression**  
✅ **Random Forest**  
✅ **XGBoost (XGB)**  
✅ **Decision Tree**  
✅ **Artificial Neural Network (ANN) using Keras**  
✅ **LSTM for sequence-based learning**  

We also performed **Grid Search** for **hyperparameter tuning**.  

---

## **📈 6. Model Evaluation**  
✅ The best model achieved **XX% accuracy** (*replace with actual number*).  
✅ A **confusion matrix** was used to analyze the model's performance.  

---

## **🚀 7. Deployment**  
We deployed the model using **Streamlit**, allowing users to:  
✅ Enter **two questions**  
✅ Get a **similarity probability score**  

🔗 **Try the Web App:** [👉 Click Here](https://questionquora.streamlit.app/)  

![Application Screenshot](image.png)  

