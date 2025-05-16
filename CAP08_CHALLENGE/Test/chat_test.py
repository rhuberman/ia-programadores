import openai
import os

# Asegúrate de tener tu clave de API de OpenAI configurada como variable de entorno
# o cárgala de forma segura. NUNCA la hardcodees en el script para producción.
print("Key " + os.getenv("OPENAI_API_KEY"))
openai.api_key = os.getenv("OPENAI_API_KEY")

def obtener_respuesta(mensajes):
    """
    Obtiene una respuesta del modelo de chat de OpenAI.

    Args:
        mensajes (list): Una lista de diccionarios que representan la conversación.
                         Cada diccionario debe tener las claves "role" (system, user, assistant)
                         y "content" (el texto del mensaje).

    Returns:
        str: La respuesta del modelo, o None si hay un error.
    """
    try:
        completion = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=mensajes
        )
        return completion.choices[0].message.content
    except Exception as e:
        print(f"Ocurrió un error al obtener la respuesta: {e}")
        return None

def main():
    """
    Función principal que ejecuta el chat.
    """
    mensajes_chat = [
        {"role": "system", "content": "Sos un asistente útil y amigable."}
    ]

    print("¡Bienvenido al chat con OpenAI!")
    while True:
        pregunta_usuario = input("Tú: ")
        if pregunta_usuario.lower() in ["adiós", "chau", "salir"]:
            print("¡Hasta luego!")
            break

        mensajes_chat.append({"role": "user", "content": pregunta_usuario})
        respuesta_asistente = obtener_respuesta(mensajes_chat)

        if respuesta_asistente:
            print(f"Asistente: {respuesta_asistente}")
            mensajes_chat.append({"role": "assistant", "content": respuesta_asistente})

if __name__ == "__main__":
    main()



# import os
# from openai import OpenAI

# OPEN_API_KEY = "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"
# client = OpenAI()

# # response = client.responses.create(
# #     model="gpt-4o",
# #     instructions="You are a coding assistant that talks like a pirate.",
# #     input="How do I check if a Python object is an instance of a class?",
# # )

# # print(response.output_text)

# def main():
#   completion =  client.chat.completions.create(
#     model="gpt-3.5-turbo",
#     messages=[
# 	{"role": "system", "content": "Sos un asistente que ayudará al usuario con sus consultas."},
#        {"role": "user", "content": "Quién ganó el mundial de fútbol en 1986?"},
#        {"role": "assistant", "content": "Argentina lo ganó en 1986."},
#        {"role": "user", "content": "Donde se jugó?"}
#   ]
# )
#   print(completion.choices[0].message)

# if __name__ == "__main__":
#     main()