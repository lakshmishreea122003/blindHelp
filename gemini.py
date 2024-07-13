"""
Install the Google AI Python SDK

$ pip install google-generativeai

See the getting started guide for more information:
https://ai.google.dev/gemini-api/docs/get-started/python
"""

import os

import google.generativeai as genai

genai.configure(api_key="AIzaSyANbBqjsb7XcJtbPaZm2MC0K0J_c2GQf98")

# Create the model
# See https://ai.google.dev/api/python/google/generativeai/GenerativeModel
generation_config = {
  "temperature": 1,
  "top_p": 0.95,
  "top_k": 64,
  "max_output_tokens": 8192,
  "response_mime_type": "text/plain",
}

model = genai.GenerativeModel(
  model_name="gemini-1.5-flash",
  generation_config=generation_config,
  # safety_settings = Adjust safety settings
  # See https://ai.google.dev/gemini-api/docs/safety-settings
  system_instruction="You are a model which helps in navigating the blind person\nThe input will be in text format, you need to understand it and response should be minimal, clear and understandable\nThe response should be human friendly",
)

chat_session = model.start_chat(
  history=[
  ]
)

def Provider(Model_input):
    print('Generating response:\n')
    response = chat_session.send_message(Model_input)

    return response.text
