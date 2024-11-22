import google.generativeai as genai
import os
import time
import gradio as gr
from google.api_core.exceptions import InvalidArgument

genai.configure(api_key=os.environ["GEMINI_API"])

initial_prompt = (
    "Se alguem te perguntar quem é você e o que você faz, diga que é um assistente virtual e que faz o processamente de diversos arquivos"
    "Você é um assistente virtual que pode receber e processar arquivos de vários tipos, "
    "como imagens, áudios, vídeos, textos e planilhas. Ao receber um arquivo, você deve analisá-lo "
    "e fornecer uma resposta adequada baseada no conteúdo."
)
model = genai.GenerativeModel("gemini-1.5-flash", system_instruction=initial_prompt)
chat = model.start_chat()

#chat.send_message("Você é um consultor de desenvolvimento web")

# response = chat.send_message("Oi!")

# print(response.text)

def assemble_prompt(message):
   prompt = [message["text"]]
   uploaded_files = upload_files(message)
   prompt.extend(uploaded_files)
   return prompt

def upload_files(message):
    uploaded_files = []
    if message["files"]:
        for file_gradio_data in message["files"]:
            uploaded_file = genai.upload_file(file_gradio_data["path"])
            while uploaded_file.state.name == "PROCESSING":
                time.sleep(5)
                uploaded_file = genai.get_file(uploaded_file.name)
            uploaded_files.append(uploaded_file)
    return uploaded_files
def gradio_wrapper(message, _history):
   prompt = assemble_prompt(message)
   try:
       response = chat.send_message(prompt)
   except InvalidArgument as e:
       response = chat.send_message(
           f"O usuário te enviou um arquivo para você ler e obteve o erro: {e}. "
           "Pode explicar o que houve e dizer quais tipos de arquivos você "
           "dá suporte? Assuma que a pessoa não sabe programação e "
           "não quer ver o erro original. Explique de forma simples e concisa."
       )
   return response.text
# Crie e lance a interface do chat com suporte a arquivos
chat_interface = gr.ChatInterface(
   fn=gradio_wrapper,
   title="Chatbot com Suporte a Arquivos 🤖",
   multimodal=True
)
# Inicie a interface
chat_interface.launch()