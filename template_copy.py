import streamlit as st
import joblib
import pandas as pd
import os
import image as IM
import dataset
import train as t
# 1. Import your model and any necessary dependencies here
if os.path.exists("Testing/model.joblib"):
    model = joblib.load("Testing/model.joblib")


# 2. Set up your Streamlit app
def main():
    # (Optional) Set page title and favicon.
    st.set_page_config(page_title="Treat Al Aid", page_icon="🧊")

    # (Optional) Set a sidebar for your app.
    with st.sidebar:
        # st.image("IMAGE_PATH")
        st.title("What do you wanna do?")
        choice = st.radio(
            "Menu", ["Home", "Enter your friend", "Recognize your friend"])
        st.info(
            "PROJECT_DESCRIPTION")
    
    # Now lets add content to each sub-page of your site
    if choice == "Home":
        # Add a title and some text to the app:
        st.title("Find your friends!")
        st.write(
            "Welcome!")
        st.write("I'm here to help you recognize your friends.")

    elif choice == "Enter your friend":
        # Add a title and some text to the app:
        st.title("Enter your friend")
        st.write("Capture a photo of your friend")

        # Adding a camera input to capture a photo
        input_picture = st.camera_input("Click a picture", disabled=False, label_visibility="visible")
        input_name = st.text_input("Enter name: ")

        # Adding a button to submit a person's identity and feeding it to the model.
        if st.button("Submit"):
            # Calling Enter_Friend function with input_picture and input_name as parameters
            Enter_Friend(input_picture, input_name)
            # Displaying message for successful submission of person's identity.
            st.write("Your friend " + input_name + " is added.")

    elif choice == "Recognize your friend":
        # Add a title and some text to the app:
        st.title("Recognize your friend")
        st.write("Turn the camera towards your friend.")
       
        # Calling Recognize_Friend() function
        Recognize_Friend()
        

# Define your model prediction function here
# For example:

# We are going to use st.cache to improve performance for predictions.
@st.cache_data
def Enter_Friend(input_picture, input_name):

   dataset.func1(input_name)


@st.cache_data
def Recognize_Friend():

    IM.func2()
    t.func3()


# Run the app
if __name__ == "__main__":
    main()
