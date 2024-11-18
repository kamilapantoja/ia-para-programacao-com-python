import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API"])

model = genai.GenerativeModel("gemini-1.5-flash")

food_plate = genai.upload_file(path="prato-de-comida.png")

prompt = "Pode identificar com cuidado o que é servido nesse prato e estimar com o máximo de precisão as suas calorias?"
response = model.generate_content([food_plate, prompt])

print(response.text)

# ===================================================

# dog1 = genai.upload_file(path="dog1.png")
# dog2 = genai.upload_file(path="dog2.png")
# dog3 = genai.upload_file(path="dog3.jpeg")

# response = model.generate_content(
#     [
#         dog3,
#         "Pode identificar a raça do cachorro da foto e me dar duas ou três frases de informações a respeito dele? "
#    "De preferência, alguma curiosidade interessante em português, citando a fonte da informação e sempre de um jeito leve e interessante."
#     ]
# )

# print(response.text)

# =====================================================

# students_spreadsheet = genai.upload_file(
#     path="desempenho_estudantes_enem.csv", display_name="Notas do ENEM"
# )

# response = model.generate_content(
#     [
#         students_spreadsheet, 
#         "Pode gerar um relatório de dois ou três parágrafos baseado nesses dados? Fale de tendências nos grupos de estudantes."
#     ]
# )

# print(response.text)

# =======================================================

# with open("curriculo-joao-silva.txt", "r") as file:
#     curriculo = file.read()

# prompt = f"Por favor, aprimore o meu currículo para deixá-lo mais assertivo e enfatizando os pontos positivos. Eis o meu currículo:\n{curriculo}"
# response = model.generate_content(prompt)

# print(response.text)

# =========================================================


# response = model.generate_content("Crie uma história sobre um computador mágico")

# print(response.text)