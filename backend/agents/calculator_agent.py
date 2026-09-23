from ollama import chat

from tools.calculator import calculate


MODEL = "mistral"


def calculator_agent(task: str):

    print("\n[Calculator Agent]")
    print("Task:", task)

    # ---------------------------------------------
    # Ask Mistral to extract the mathematical
    # expression from the user's task
    # ---------------------------------------------

    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
You are a calculator specialist.

Your job is to identify the mathematical expression
from the user's request.

Return ONLY the mathematical expression.

Examples:

User:
What is 25 * 40?

Return:
25 * 40

User:
Calculate 100 divided by 5.

Return:
100 / 5
"""
            },
            {
                "role": "user",
                "content": task
            }
        ]
    )

    expression = response["message"]["content"].strip()

    print("Expression:", expression)

    # ---------------------------------------------
    # Execute calculator tool
    # ---------------------------------------------

    result = calculate(expression)

    print("Calculator result:", result)

    return result