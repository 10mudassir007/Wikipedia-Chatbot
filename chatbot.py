import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import wikipedia
import pickle
# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

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
            with open('response.pkl','wb') as response_file:
                pickle.dump(response,response_file)
        else:
            response = get_wikipedia_summary(processed_input)
            with open('response.pkl','wb') as response_file:
                pickle.dump(response,response_file)


        return f"You: {user_input}\nChatcrafter: {response}"

# Example usage

# while True:
#     user_input = input("You: ")
#     response = handle_user_input(user_input)
#     print(response)

#     with open('response.pkl','wb') as response_file:
#         pickle.dump(response,response_file)

#     if user_input.lower() == 'exit':
#         break



