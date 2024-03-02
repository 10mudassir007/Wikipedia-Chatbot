import streamlit as st
import time

def animated_output(message):
    for char in message:
        st.text(char)
        time.sleep(0.1)  # Adjust the sleep duration to control the speed

# Example usage
st.title("Animated Output")
message = "This is an animated output!"
animated_output(message)
