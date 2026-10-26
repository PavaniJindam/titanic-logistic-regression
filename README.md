# Titanic Survival Prediction Using Logistic Regression

## Project Description
This project uses Logistic Regression to predict the survival of passengers aboard the Titanic based on passenger information.

## Objectives
- Explore and understand the Titanic dataset.
- Perform data preprocessing.
- Build and train a Logistic Regression model.
- Evaluate the model using classification metrics and an ROC curve.
- Deploy the trained model using Streamlit.

## Technologies Used
- Python
- Pandas
- Scikit-learn
- Matplotlib and Seaborn
- Joblib
- Streamlit
- Google Colab / Jupyter Notebook

## Project Files
- `app.py` — Streamlit application for survival prediction.
- `.ipynb` — Notebook containing data exploration, preprocessing, model training, and evaluation.
- `titanic_model.pkl` — Saved trained model.

## How to Run the Application
Install the required libraries:

```bash
pip install streamlit pandas joblib scikit-learn
```

Run the application:

```bash
python -m streamlit run app.py
```

## Model Evaluation
The Logistic Regression model achieved an accuracy of 80.45% and an ROC-AUC score of 0.8437 on the evaluation data.

## Conclusion
This project demonstrates the application of Logistic Regression to a classification problem and the use of Streamlit to provide an interactive prediction interface.
