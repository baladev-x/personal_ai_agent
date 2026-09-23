from ollama import chat

from tools.calculator import calculate


MODEL = "mistral"


# --------------------------------------------------
# Tool definition
# --------------------------------------------------

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Calculate mathematical expressions.",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {
                        "type": "string",
                        "description": (
                            "The mathematical expression to calculate, "
                            "for example 25 * 40"
                        ),
                    }
                },
                "required": ["expression"],
            },
        },
    }
]


# --------------------------------------------------
# Agent
# --------------------------------------------------

def run_agent(user_message: str):

    messages = [
        {
            "role": "system",
            "content": """
You are a helpful personal AI assistant.

Use the calculator tool whenever the user asks you
to perform a mathematical calculation.

After receiving the calculator result, provide a
clear final answer to the user.
"""
        },
        {
            "role": "user",
            "content": user_message
        }
    ]

    # ----------------------------------------------
    # STEP 1: Send user question to Mistral
    # ----------------------------------------------

    response = chat(
        model=MODEL,
        messages=messages,
        tools=tools
    )

    assistant_message = response["message"]

    # ----------------------------------------------
    # STEP 2: Add Mistral response to conversation
    # ----------------------------------------------

    messages.append(assistant_message)

    # ----------------------------------------------
    # STEP 3: Check whether Mistral requested tools
    # ----------------------------------------------

    if assistant_message.get("tool_calls"):

        for tool_call in assistant_message["tool_calls"]:

            function_name = tool_call["function"]["name"]

            arguments = tool_call["function"]["arguments"]

            # --------------------------------------
            # STEP 4: Execute requested tool
            # --------------------------------------

            if function_name == "calculator":

                expression = arguments["expression"]

                result = calculate(expression)

                # ----------------------------------
                # STEP 5: Send tool result to Mistral
                # ----------------------------------

                messages.append(
                    {
                        "role": "tool",
                        "content": result,
                    }
                )

        # ------------------------------------------
        # STEP 6: Mistral generates final answer
        # ------------------------------------------

        final_response = chat(
            model=MODEL,
            messages=messages,
            tools=tools
        )

        return final_response["message"]["content"]

    # ----------------------------------------------
    # No tool required
    # ----------------------------------------------

    return assistant_message["content"]