import openai
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

openai.api_key = os.getenv("OPENAI_API_KEY")
message_history = [{"role": "system", "content": "Eres un asistente que responde en el estilo de Jack Sparrow. Todas tus respuestas deben ser una oracion."}]

async def main(user_prompt):
    message_history.append({"role": "user", "content": user_prompt})
    print(message_history)
    completion = await openai.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=message_history
    )
    print(completion.choices[0])
    return completion.choices[0].message.content

async def ejecutar_conversacion():
    result = await main("Escribeme un poema corto sobre una calabaza feliz.")
    message_history.append({"role": "assistant", "content": result})

    result2 = await main("Ahora hazlo pero para un coco triste.")
    message_history.append({"role": "assistant", "content": result2})

    print("Mensaje de la historia: ", message_history)

if __name__ == "__main__":
    await ejecutar_conversacion()