import openai

def generate_answer(question, docs):

    context = "\n".join(docs)

    prompt = f"""
Use the following documentation to answer the question.

Documentation:
{context}

Question:
{question}
"""

    response = openai.ChatCompletion.create(
        model="gpt-4o-mini",
        messages=[{"role":"user","content":prompt}]
    )

    return response["choices"][0]["message"]["content"]