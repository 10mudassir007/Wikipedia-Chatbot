import streamlit as st
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import wikipedia
import time
# Download NLTK resources
# nltk.download('punkt')
# nltk.download('stopwords')

# Set up Wikipedia
wikipedia.set_lang("en")

# Function to preprocess input text
def preprocess_input(text):
    stop_words = set(stopwords.words('english'))
    word_tokens = word_tokenize(text.lower())
    filtered_text = [word for word in word_tokens if word.isalnum() and word not in stop_words]
    return ' '.join(filtered_text)

# Function to get Wikipedia summary for a given query
def get_wikipedia_summary(query):
    try:
        page = wikipedia.page(query)
        return page.summary
    except wikipedia.exceptions.DisambiguationError as e:
        # If there are multiple suggestions, return the options
        return f"Ambiguous query. Options: {', '.join(e.options)}"
    except wikipedia.exceptions.PageError:
        return "Sorry, I couldn't find information on that topic."

# Function to handle user input
def handle_user_input(user_input):
    if user_input.lower() == 'exit':
        return "Goodbye!"
    else:
        processed_input = preprocess_input(user_input)
        if processed_input == 'hello':
            response = 'Hello, how may I help you?'
        else:
            response = get_wikipedia_summary(processed_input)


        return f"{response}"



css = """<style>
            .output {
            font-family: 'Arial';
            font-size: 20px;
}"""


st.title('Chatcrafter')
st.markdown(css,unsafe_allow_html=True)
try:
    user_input = st.text_input('You: ')
    if st.button('Submit'):
        response = handle_user_input(user_input)
        x = (f'<p class="output"> Chatcrafter:{response}<p>')
        st.write(x,unsafe_allow_html=True)

except:
    st.write('Invalid Input')
# while True:
#     user_input = input("You: ")
#     response = handle_user_input(user_input)
#     try:
#         print(response)
#     except:
#         print('Invalid Input')