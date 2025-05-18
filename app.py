import streamlit as st

# Set page title and layout
st.set_page_config(page_title="Courier Tracking System", page_icon="📦", layout="centered")

# Title with improved styling
st.markdown("<h1 style='text-align: center; color: #FF8800;'>📦 Online Tracking System</h1>", unsafe_allow_html=True)

# Input field for tracking number
tracking_number = st.text_input("Enter Tracking Number:")

# Dropdown for selecting the courier service
courier_options = ["DHL", "Leopard", "M&P", "Pakistan Post"]
selected_courier = st.selectbox("Select Courier:", courier_options)

# Buttons for tracking and history
col1, col2 = st.columns(2)

with col1:
    if st.button("Track 🚚"):
        if tracking_number:
            st.success(f"Tracking {tracking_number} with {selected_courier}...")
        else:
            st.warning("Please enter a tracking number.")

with col2:
    if st.button("History 📜"):
        st.info("Showing tracking history...")
