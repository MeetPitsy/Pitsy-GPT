import openai
import streamlit as st

class PitsyAutomationGPT:
    def __init__(self):
        # Get the API key from Streamlit secrets
        self.api_key = st.secrets["OPENAI_API_KEY"]
        openai.api_key = self.api_key
        self.conversation_history = []

    def get_response(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        try:
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=self.conversation_history
            )
            assistant_response = response['choices'][0]['message']['content']
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            return assistant_response
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Instantiate PitsyAutomationGPT
pitsy = PitsyAutomationGPT()

# Streamlit UI setup
st.title("🤖 Pitsy Automation GPT Interface 🚀")

import openai
import streamlit as st

class PitsyAutomationGPT:
    def __init__(self):
        # Get the API key from Streamlit secrets
        self.api_key = st.secrets["OPENAI_API_KEY"]
        openai.api_key = self.api_key
        self.conversation_history = []

    def get_response(self, user_input):
        self.conversation_history.append({"role": "user", "content": user_input})
        try:
            response = openai.ChatCompletion.create(
              model="gpt-3.5-turbo",
              messages=self.conversation_history
            )
            assistant_response = response['choices'][0]['message']['content']
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            return assistant_response
        except Exception as e:
            return f"An error occurred: {str(e)}"

# Instantiate PitsyAutomationGPT
pitsy = PitsyAutomationGPT()


