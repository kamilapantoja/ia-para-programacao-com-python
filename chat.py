import google.generativeai as genai
import os
import gradio

genai.configure(api_key=os.environ["GEMINI_API"])

model = genai.GenerativeModel("gemini-1.5-flash")

chat = model.start_chat()
chat.send_message("Você é um consultor de desenvolvimento web")

# response = chat.send_message("Oi!")

# print(response.text)

def gradio_wrapper(message, _history):
    response = chat.send_message(message)
    return response.text

chatInterface = gradio.ChatInterface(gradio_wrapper)
chatInterface.launch()