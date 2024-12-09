import streamlit as st

# Title of the web app
st.title('My First Streamlit App-GITAM')


# Input text box
user_input = st.text_input('Enter your name')

# Display the user's input
if user_input:
    st.write(f'Hello, {user_input}!')