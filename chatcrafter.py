import tkinter as tk
from tkinter import scrolledtext, Entry, Button

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import wikipedia

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
def handle_user_input():
    user_input = user_entry.get()
    if user_input.lower() == 'exit':
        chat_display.insert(tk.END, "Chatcrafter: Goodbye!\n")
        root.destroy()
    else:
        processed_input = preprocess_input(user_input)
        if processed_input == 'hello':
            response = 'Hello, how may I help you?'
        else:
            response = get_wikipedia_summary(processed_input)

        # Display the response
        chat_display.insert(tk.END, f"You: {user_input}\n")
        chat_display.insert(tk.END, f"Chatcrafter: {response}\n")
        chat_display.yview(tk.END)  # Auto-scroll to the bottom

        # Clear the user input field
        user_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("ChatCRAFTER")

# Create a scrolled text widget for the chat display
chat_display = scrolledtext.ScrolledText(root, wrap=tk.WORD, width=40, height=10)
chat_display.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create an entry widget for user input
user_entry = Entry(root, width=30)
user_entry.grid(row=1, column=0, padx=10, pady=10)

# Create a button to send user input
send_button = Button(root, text="Send", command=handle_user_input)
send_button.grid(row=1, column=1, padx=10, pady=10)

# Start the main loop
root.mainloop()
