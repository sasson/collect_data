import ai21
import streamlit as st
import requests

class ai21_answer:
    def __init__(self, api_key):
        self.api_key = api_key

    def answer(self, context, question):
        url = "https://api.ai21.com/studio/v1/experimental/answer"
        
        payload = {
            "context": context,
            "question": question
        }
        
        headers = {
            "accept": "application/json",
            "content-type": "application/json",
            "Authorization": f"Bearer {self.api_key}"
        }

        response = requests.post(url, json=payload, headers=headers)
        return response
