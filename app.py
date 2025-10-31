import streamlit as st

st.set_page_config(page_title="Simple Calculator", layout="centered")
st.title("🧮 Simple Calculator")

st.markdown("Enter two numbers and choose an operation:")

# --- Inputs ---
num1 = st.number_input("Enter first number:", value=0.0, step=1.0)
num2 = st.number_input("Enter second number:", value=0.0, step=1.0)
operation = st.selectbox("Select operation:", ["Add", "Subtract", "Multiply", "Divide"])

# --- Calculate ---
if st.button("Calculate"):
    try:
        if operation == "Add":
            result = num1 + num2
        elif operation == "Subtract":
            result = num1 - num2
        elif operation == "Multiply":
            result = num1 * num2
        elif operation == "Divide":
            if num2 == 0:
                st.error("Cannot divide by zero.")
                st.stop()
            result = num1 / num2
        st.success(f"**Result:** {result}")
    except Exception as e:
        st.error(f"Error: {e}")

st.divider()
st.caption("Built with Streamlit 💡 — fast, simple, interactive Python apps.")
