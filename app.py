import streamlit as st
import os
from twitter_search import TwitterSearch
import ai21_answer_interface
from ai21_answer_interface import ai21_answer

# Define a Streamlit app function to search for tweets and cache the results
@st.cache_data
def get_tweets(query):
    # Initialize the TwitterSearch class with your Twitter API tokens and secrets

    search = TwitterSearch(
        TWITTER_API_KEY = os.environ["TWITTER_API_KEY"], 
        TWITTER_API_SECRET = os.environ["TWITTER_API_SECRET"], 
        TWITTER_ACCESS_TOKEN = os.environ["TWITTER_ACCESS_TOKEN"], 
        TWITTER_ACCESS_SECRET = os.environ["TWITTER_ACCESS_SECRET"]
    )

    results = search.search(query)
    return results

# Define a Streamlit app function to call the AI21 answer API and cache the results
@st.cache_data
def get_ai21_answer(context, question):
    # Call Constructor
    o = ai21_answer(api_key = os.environ["AI21_API_KEY"],)
    answer = o.answer(context, question)
    return answer

@st.cache_data
def get_screen_names(filename : str):
    screen_names = set()

    # Read the set of screen names from a file
    with open(filename, 'r') as f:
        screen_names = set([line.strip() for line in f.readlines()])    

    return screen_names

# Define a function to combine top tweets into a string
@st.cache_data
def combine_top_tweets(results):
    top_tweets = []
    for tweet in results:
        top_tweets.append(tweet['text'])
        if len(top_tweets) == 5:
            break
    return '\n'.join(top_tweets)


# Define the main Streamlit app code
def main():
    # Get a search query from the user
    query = st.text_input('Enter a Twitter search query:', '')

    # Search for tweets and generate context for ai21 answer
    if query:
        allowed_screen_names = get_screen_names(filename = "twitter_list_members.txt")
        results = get_tweets(query)
        num_resultsd = len(results)

        acceptable_tweets = []
        for tweet in results:
            if tweet['user'] in allowed_screen_names:
                acceptable_tweets.append(acceptable_tweets)

        context = combine_top_tweets(acceptable_tweets)

        context = combine_top_tweets(results[:5])
        print("[" + context + "]")

"""
        question = query

        # Call ai21 answer and display the result
        answer = get_ai21_answer(context, question)
        st.write('Answer:')
        st.write(answer.json()['answer'])
"""

# Run the Streamlit app
if __name__ == '__main__':
    main()
