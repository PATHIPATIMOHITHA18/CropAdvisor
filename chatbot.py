import ollama

def ask_bot(question):

    response = ollama.chat(
        model="qwen3.5:2b",
        messages=[
            {
                "role": "system",
                "content": """
You are an agricultural expert.

Answer in simple English.

Give practical farming advice.

Keep responses short and easy to understand.
"""
            },
            {
                "role": "user",
                "content": question
            }
        ]
    )
    return response["message"]["content"]