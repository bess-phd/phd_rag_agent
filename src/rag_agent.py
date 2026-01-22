"""
Minimal RAG agent skeleton for PhD experiments
"""
from openai import OpenAI
import os

# 1. Load dummy docs
def load_docs():
    docs = []
    for f in os.listdir("../data"):
        if f.endswith(".txt"):
            with open(f"../data/" + f, "r") as file:
                docs.append(file.read())
    return docs

# 2. Retrieve context (simulated)
def retrieve_context(query):
    docs = load_docs()
    return "\n".join(docs)

# 3. Build prompt
def build_prompt(context, question):
    return f"""
You are a research assistant agent.
Answer ONLY using the context below.

Context:
{context}

Question:
{question}
"""

# 4. Ask agent (simulated)
def ask_agent(question):
    context = retrieve_context(question)
    prompt = build_prompt(context, question)
    return f"Simulated answer for: {question}\nContext:\n{context}"

# Example
if __name__ == "__main__":
    response = ask_agent("Explain the documents.")
    print(response)
