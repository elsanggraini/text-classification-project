# Classification of ChatGPT-Generated vs. Human-Written News Articles using SVM

## 📌 Project Overview
As AI-generated content becomes more prevalent in media, the ability to distinguish between human-authored news and AI-generated text is crucial for information integrity. This project implements a **Support Vector Machine (SVM)** classifier to analyze and categorize news articles based on their origin.

## 🚀 Features
- **Data Preprocessing:** Cleaning and structuring raw text data for NLP tasks.
- **Feature Analysis:** Identifying linguistic patterns and sentence structures unique to ChatGPT and human journalists.
- **Multi-Metric Evaluation:** Beyond simple accuracy, the model is evaluated using Kappa, Weighted Mean Recall, and Precision to assess its reliability.

## 🛠️ Methodology
The workflow of this research includes:
1. **Data Acquisition:** Gathering a balanced dataset of human-written news and ChatGPT outputs.
2. **Preprocessing:** Text normalization, cleaning, and labeling.
3. **Training:** Implementing the SVM algorithm for binary classification.
4. **Evaluation:** Measuring performance against a test dataset.

## 📊 Evaluation Results
The model achieved the following results during the initial testing phase:
- **Accuracy:** 50.24%
- **Kappa Score:** 0.010
- **Weighted Mean Recall:** 33.67%
- **Weighted Mean Precision:** 33.44%

### **Analysis of Results**
The current accuracy suggests a significant challenge in distinguishing between the two classes using traditional SVM. The low Kappa score indicates that the model's predictions are currently close to random, likely due to:
- The high level of linguistic sophistication in ChatGPT-generated text.
- Limited training data size.
- Complex linguistic features that require more advanced feature engineering.

## 🔮 Future Work & Improvements
To improve the detection accuracy, future iterations will focus on:
- **Expanding the Dataset:** Increasing the volume of training data to capture more diverse writing styles.
- **Advanced Feature Engineering:** Exploring deeper linguistic markers like perplexity and burstiness.
- **Deep Learning Models:** Implementing Transformer-based models (e.g., BERT or RoBERTa) or Ensemble Learning techniques.

## 📂 Project Structure
- `data/`: Contains the processed datasets.
- `notebooks/`: Jupyter notebooks for data exploration and model training.
- `results/`: Detailed evaluation metrics and logs.
