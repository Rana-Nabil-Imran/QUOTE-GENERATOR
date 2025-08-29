import streamlit as st
import requests

st.title(" Quote Generator")
st.write("Click the button to get an inspiring quote from the web!")

# Function to fetch a random quote from ZenQuotes API
def get_random_quote():
    try:
        response = requests.get("https://zenquotes.io/api/random")
        if response.status_code == 200:
            data = response.json()[0]  # ZenQuotes returns a list
            return f'"{data["q"]}"\n\n— {data["a"]}'
        else:
            return "Sorry, could not fetch a quote at the moment."
    except:
        return "Error: Unable to connect to the quote API."

# Button to generate quote
if st.button("Generate Quote"):
    quote = get_random_quote()
    st.success(quote)
