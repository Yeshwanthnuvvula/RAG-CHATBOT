import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


def ask_llm(context, question):

    prompt = f"""
You are a helpful document question-answering assistant.

Answer the user's question using ONLY the provided context.

If the answer cannot be found in the context, say:
"I couldn't find that information in the document."

Keep the answer clear and concise.
Do not add information from your own knowledge.

Context:
{context}

Question:
{question}

Answer:
"""

    response = client.responses.create(
        model="gpt-4o-mini",
        input=prompt,
        max_output_tokens=150
    )

    return response.output_text