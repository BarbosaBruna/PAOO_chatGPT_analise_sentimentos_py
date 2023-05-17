import os
import openai
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

pergunta_padrao = 'Qual sentimento da seguinte frase? Responda com apenas uma palavra: Positivo, Negativo ou Neutro. Eis a frase: '

frase_usuario = input('Escreva uma frase para enviarmos para o ChatGPT\n')

prompt = f'{pergunta_padrao}{frase_usuario}'

resposta = openai.Completion.create(
    engine='text-davinci-003',
    prompt=prompt
)

print (resposta.choices[0].text)
