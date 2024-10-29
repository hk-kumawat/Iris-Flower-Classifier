import pickle
import streamlit as st
import numpy as np
import sklearn

# Load scaler and model
scaler_file = pickle.load(open('scaler.pkl', 'rb'))
model_file = pickle.load(open('model.pkl', 'rb'))

# Prediction function
def pred_output(user_input):
    scaled_input = scaler_file.transform(np.array(user_input).reshape(-1, 4))
    ypred = model_file.predict(scaled_input)
    return ypred[0]

# Streamlit App
def main():
    # Page layout and title
    st.set_page_config(page_title="Iris Flower Classifier", layout="centered")
    
    # Set a gradient background
    st.markdown(
        """
        <style>
        .reportview-container {
            background: linear-gradient(to bottom right, #6a82fb, #fc5c7d);
            height: 100vh;
            color: white;
        }
        </style>
        """,
        unsafe_allow_html=True
    )
    
    # Centering the title with HTML and setting color to white
    st.markdown(
        "<h1 style='text-align: center; font-size: 2.5em;'>🌸 Iris Flower Classification 🌸</h1>",
        unsafe_allow_html=True
    )
    st.markdown(
        "<h3 style='text-align: center;'>Developed by - Harshal Kumawat</h3>",
        unsafe_allow_html=True
    )

    # Divider and instructions
    st.divider()
    st.markdown(
        "<p style='text-align: center;'>Enter the dimensions below and let the magic of AI classify your Iris flower species! 🌼</p>",
        unsafe_allow_html=True
    )

    # Input fields with descriptions
    col1, col2 = st.columns(2)
    with col1:
        sepalLength = st.text_input(
            "🌱 Sepal Length (Cm)",
            help="Enter the length of the sepal in centimeters."
        )
        petalLength = st.text_input(
            "🌸 Petal Length (Cm)",
            help="Enter the length of the petal in centimeters."
        )
    with col2:
        sepalWidth = st.text_input(
            "🍃 Sepal Width (Cm)",
            help="Enter the width of the sepal in centimeters."
        )
        petalWidth = st.text_input(
            "🌺 Petal Width (Cm)",
            help="Enter the width of the petal in centimeters."
        )

    # Validation for numeric input
    if sepalLength.isalpha() or sepalWidth.isalpha() or petalLength.isalpha() or petalWidth.isalpha():
        st.error("🚨 Input must be a numeric value!")
        st.warning("It seems one or more inputs are not numbers. Please enter valid numbers to proceed.")

    # Predict button with a loader
    if st.button('🌼 Classify My Flower'):
        # Check if all fields are filled
        if not sepalLength or not sepalWidth or not petalLength or not petalWidth:
            st.error("🚨 Please enter values for all fields before classifying!")
        else:
            user_input = [sepalLength, sepalWidth, petalLength, petalWidth]
            with st.spinner("Analyzing... 🌱"):
                prediction = pred_output(user_input)
                st.success(f"🌸 This Iris flower is likely: **{prediction}**")

# Run the app
if __name__ == '__main__':
    main()
