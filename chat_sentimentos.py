import google.generativeai as genai
import os
import gradio as gr
# Configurar a chave de API
genai.configure(api_key=os.environ["GEMINI_API"])
# Definir o prompt inicial para o analisador de sentimentos
initial_prompt = (
    "Você é um assistente que analisa o sentimento de textos fornecidos, "
    "identificando se o sentimento é positivo, negativo ou neutro, e fornecendo um breve feedback."
)
# Criar o modelo com o prompt inicial
model = genai.GenerativeModel("gemini-1.5-flash",
                              system_instruction=initial_prompt)
# Iniciar o chat
chat = model.start_chat()
def gradio_wrapper(message, _history):
    # Extraia o texto da mensagem
    user_text = message["text"]
    # Extraia a lista de arquivos
    files = message.get("files", [])
    # Lista para armazenar conteúdos dos arquivos
    file_contents = []
    # Verifique se há arquivos anexados
    if files:
        for file_info in files:
            # Obter o caminho local do arquivo
            file_path = file_info["path"]
            # Ler o conteúdo do arquivo se for um texto
            if file_info["mime_type"] == "text/plain":
                with open(file_path, "r", encoding="utf-8") as f:
                    content = f.read()
                file_contents.append(content)
            else:
                # Ignorar arquivos que não sejam de texto simples
                pass
    # Combinar o texto do usuário com o conteúdo dos arquivos
    combined_text = user_text + "\n\n" + "\n\n".join(file_contents)
    # Criar o prompt para análise de sentimento
    prompt = f"Analise o sentimento do seguinte texto:\n{combined_text}"
    # Envie o prompt para o chat e obtenha a resposta
    response = chat.send_message(prompt)
    return response.text
# Crie e lance a interface do chat com suporte a arquivos
chat_interface = gr.ChatInterface(
    fn=gradio_wrapper,
    title="Analisador de Sentimentos 🎭",
    multimodal=True
)
chat_interface.launch()