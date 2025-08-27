# app.py
import streamlit as st
import requests

st.set_page_config(page_title="Quote Generator", page_icon="💬")
st.title("💬 Quote Generator")
st.write("Click the button to get an inspiring quote from the web!")

# Function to fetch a random quote from the API
def get_random_quote():
    try:
        response = requests.get("https://api.quotable.io/random")
        if response.status_code == 200:
            data = response.json()
            return f'"{data["content"]}"\n\n— {data["author"]}'
        else:
            return "Sorry, could not fetch a quote at the moment."
    except:
        return "Error: Unable to connect to the quote API."

# Button to generate quote
if st.button("Generate Quote"):
    quote = get_random_quote()
    st.success(quote)
