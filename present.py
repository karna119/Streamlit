import streamlit as st

# Title
st.title('My Interactive Presentation')

# Introduction section
st.header('Introduction')
st.write('Welcome to my Streamlit presentation! This app showcases interactive elements.')

# Slide 1: Text and Image
st.header('Slide 1: Text and Image')
st.write('Here is some informative text.')
st.image('https://www.example.com/image.jpg', caption='An example image')

# Slide 2: Data Visualization
st.header('Slide 2: Data Visualization')
st.write('This slide includes a data visualization.')
# Example plot with matplotlib
import matplotlib.pyplot as plt

fig, ax = plt.subplots()
ax.plot([1, 2, 3, 4], [10, 20, 25, 30])
ax.set_title('Sample Plot')
st.pyplot(fig)

# Slide 3: Interactive Elements
st.header('Slide 3: Interactive Elements')
user_name = st.text_input('What is your name?')
if user_name:
    st.write(f'Hello, {user_name}!')

option = st.selectbox('Choose an option:', ['Option 1', 'Option 2', 'Option 3'])
st.write(f'You selected: {option}')

# Slide 4: Closing
st.header('Closing')
st.write('Thank you for viewing my presentation! Feel free to interact with the elements above.')

# Run Streamlit app
if st.button('Start Presentation'):
    st.write('Presentation is starting...')

if st.button('End Presentation'):
    st.write('Presentation has ended.')
