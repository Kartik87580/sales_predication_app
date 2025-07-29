import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Set page config
st.set_page_config(page_title="Sales Prediction Dashboard", layout="wide")

st.title("📊 Sales Prediction using Advertising Dataset")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv("advertising.csv")
    if "Unnamed: 0" in df.columns:
        df.drop("Unnamed: 0", axis=1, inplace=True)
    return df

df = load_data()

# Sidebar - Input features
st.sidebar.header("Enter Advertising Spend")

tv = st.sidebar.slider("TV Spend ($)", 0.0, 300.0, 150.0)
radio = st.sidebar.slider("Radio Spend ($)", 0.0, 50.0, 25.0)
newspaper = st.sidebar.slider("Newspaper Spend ($)", 0.0, 120.0, 30.0)

# Main - Dataset preview
with st.expander("🔍 Preview Dataset"):
    st.write(df.head())

# Main - Correlation heatmap
st.subheader("🔗 Feature Correlation")
fig1, ax1 = plt.subplots()
sns.heatmap(df.corr(), annot=True, cmap="coolwarm", ax=ax1)
st.pyplot(fig1)

# Train-test split
X = df[['TV', 'Radio', 'Newspaper']]
y = df['Sales']
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model
model = LinearRegression()
model.fit(X_train, y_train)

# Evaluation
y_pred = model.predict(X_test)
r2 = r2_score(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)

st.markdown("### 📈 Model Performance")
st.write(f"**R² Score:** {r2:.2f}")
st.write(f"**Mean Squared Error:** {mse:.2f}")

# Prediction from user input
user_input = [[tv, radio, newspaper]]
# predicted_sales = model.predict(user_input)[0]

st.markdown("### 📤 Prediction from Input")
if st.button("Predict"):
    user_input = [[tv, radio, newspaper]]
    predicted_sales = model.predict(user_input)[0]
    st.success(f"Estimated Sales: **{predicted_sales:.2f} units**")

# Footer
st.markdown("---")
st.markdown("Made with ❤️ using Streamlit")

