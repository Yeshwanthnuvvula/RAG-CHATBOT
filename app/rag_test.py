from app.retriever import get_context
from app.llm import ask_llm

question = "What is reinforcement learning?"


context = get_context(question)


answer = ask_llm(context, question)


print("\n--- ANSWER ---")
print(answer)