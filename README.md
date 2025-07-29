
# 📊 Sales Prediction 

An interactive machine learning dashboard built with **Streamlit** to predict **product sales** based on advertising budget allocation across TV, Radio, and Newspaper. It also provides visual analysis and performance metrics using **Linear Regression**.

---

## 🚀 Features

* Predict **sales output** based on TV, Radio, and Newspaper spending
* Explore **correlation heatmap** between features
* View **model performance** (R² score & MSE)
* Interactive sliders for user input
* Clean, responsive web interface using Streamlit

---

## 🧠 Tech Stack

* **Python**
* **Streamlit** – for dashboard UI
* **Pandas** – for data manipulation
* **Seaborn & Matplotlib** – for data visualization
* **Scikit-learn** – for machine learning and evaluation

---

## 📂 Project Structure

```
sales_prediction/
│
├── advertising.csv          # Dataset
├── app.py                   # Streamlit app
├── README.md                # Project documentation
└── requirements.txt         # Python dependencies
```

---

## 📈 Dataset

* Dataset: `advertising.csv`
* Features:

  * `TV` – Advertising budget spent on TV
  * `Radio` – Budget spent on radio
  * `Newspaper` – Budget spent on newspaper
* Target:

  * `Sales` – Number of product units sold

---

## 📊 Model Details

* **Algorithm**: Linear Regression
* **Evaluation Metrics**:

  * R² Score
  * Mean Squared Error (MSE)
* Train-test split: 80-20%

---

## 🖥️ How to Run the App

1. **Clone the repository**:

   ```bash
   git clone https://github.com/yourusername/sales_prediction.git
   cd sales_prediction
   ```

2. **Install dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Streamlit app**:

   ```bash
   streamlit run app.py
   ```

---



## 📜 License

This project is licensed under the [MIT License](LICENSE).

---


