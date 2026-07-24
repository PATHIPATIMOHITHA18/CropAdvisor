import ollama

def route_query(query):

    prompt = f"""
You are a routing agent.

Your job is ONLY to classify the user's query.

Available tools:

crop
- crop recommendation
- which crop should I grow
- suitable crop
- recommend crop
- best crop

disease
- leaf disease
- pest
- spots
- yellow leaves
- disease treatment

irrigation
- irrigation
- watering
- rainfall
- water plants

chatbot
- all other agricultural questions

Return ONLY ONE WORD.

Possible outputs:
crop
disease
irrigation
chatbot

User Query:
{query}
"""

    response = ollama.chat(
        model="qwen3.5:2b",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    tool = response["message"]["content"].strip().lower()

    if tool not in ["crop", "disease", "irrigation", "chatbot"]:
        tool = "chatbot"

    return tool