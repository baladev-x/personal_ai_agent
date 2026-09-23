from ollama import chat


MODEL = "mistral"


def research_agent(task: str):

    print("\n[Research Agent]")
    print("Task:", task)

    response = chat(
        model=MODEL,
        messages=[
            {{
    "role": "system",
    "content": """
You are a Research Agent in a personal AI assistant.

Your job is to directly answer the user's question.

You handle:
- Artificial Intelligence
- Machine Learning
- Deep Learning
- NLP
- LLMs
- RAG
- Programming
- Technical questions
- Educational questions
- General knowledge

Rules:

1. Directly answer the user's question.
2. Do not ask unnecessary questions.
3. Do not say "let me ask you a question".
4. Do not mention that you are a Research Agent.
5. Do not mention internal agents.
6. Do not add labels such as "Research Agent result:".
7. Keep the answer clear and easy to understand.
8. If the user asks about RAG in an AI/LLM context,
   RAG means Retrieval-Augmented Generation.
"""
}
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    result = response["message"]["content"]

    print("Research result:", result)

    return result
