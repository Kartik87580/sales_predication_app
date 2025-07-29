# 📢 Advertisement Click Prediction using Machine Learning

A machine learning web app that predicts whether a user will **click on an advertisement** or not, based on features like **age**, **daily internet usage**, **timestamp**, etc. Built using **Streamlit**, **Pandas**, and **Scikit-learn**.

---

## 📊 Features Used

* Daily Time Spent on Site
* Age
* Area Income
* Daily Internet Usage
* Timestamp (can be processed into hour/day)
* Gender (if included)
* Clicked on Ad (Target)

---

## 🧠 Tech Stack

* **Python**
* **Pandas & NumPy** – for data analysis
* **Scikit-learn** – for ML models and preprocessing
* **Matplotlib & Seaborn** – for visualization (if included)
* **Streamlit** – for deploying interactive web app

---

## 🧪 ML Model

* **Logistic Regression** or any suitable classification model
* Target variable: `Clicked on Ad` (0 = No, 1 = Yes)

---

## 📂 Project Structure

```
ad_click_prediction/
│
├── advertising.csv             # Dataset
├── ad_click_prediction.ipynb   # Model training and EDA
├── app.py                      # Streamlit application
├── model.pkl                   # Trained ML model (optional)
├── README.md                   # Documentation
└── requirements.txt            # Python dependencies
```

---

## 🚀 How to Run

1. **Clone the repo**:

   ```bash
   git clone https://github.com/yourusername/ad_click_prediction.git
   cd ad_click_prediction
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Launch the app**:

   ```bash
   streamlit run app.py
   ```

---

## 🧠 Model Workflow

1. Data loaded and preprocessed
2. Features selected and target encoded
3. Trained using classification algorithm
4. User input taken via Streamlit UI
5. Model predicts probability of clicking the ad



## 📜 License

This project is licensed under the [MIT License](LICENSE).

---

