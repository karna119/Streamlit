import streamlit as st

# Title of the web app
st.title('My Streamlit App with More Widgets')

# Input text box
user_input = st.text_input('Enter your name')

# Dropdown menu
options = ['Data scientist', 'Data analyst', 'Data Engineer']
dropdown_selection = st.selectbox('Choose an option:', options)

# Text area
text_area_input = st.text_area('Enter your Skill set')

# Display the user's input
if user_input:
    st.write(f'Hello, {user_input}!')

st.write(f'You selected: {dropdown_selection}')

if text_area_input:
    st.write('Your skillset:')
    st.write(text_area_input)

# Buttons
if st.button('JAva'):
    st.write('Angular,React,Mongodb,Express.js,Node.JS')

if st.button('Python'):
    st.write('Django,Mongodb,Flutter,React')

# A checkbox for fun
if st.checkbox('Check me out'):
    st.write('Checkbox is checked!')
