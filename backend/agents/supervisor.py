from ollama import chat
from agents.calculator_agent import calculator_agent
from agents.research_agent import research_agent

MODEL = "mistral"

def supervisor_agent(user_message: str):
    print("\n==============================")
    print("[Supervisor Agent]")
    print("User:", user_message)

    # ---------------------------------------------
    # Supervisor decides which agent to use
    # ---------------------------------------------
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": """
                You are the Supervisor Agent of a personal AI system. You have access to the following specialized agents:
                1. calculator_agent - Handles mathematical calculations.
                2. research_agent - Handles general knowledge, technical, educational, and research-related questions.

                Rules:
                - Mathematical calculation: respond ONLY: calculator_agent
                - General knowledge, technical, educational, or research question: respond ONLY: research_agent
                - Simple conversation: answer directly.
                """
            },
            {
                "role": "user",
                "content": user_message
            }
        ]
    )

    decision = response["message"]["content"].strip()
    print("Supervisor decision:", decision)

    # ---------------------------------------------
    # Calculator Agent (Direct Return)
    # ---------------------------------------------
    if "calculator_agent" in decision.lower():
        result = calculator_agent(user_message)
        print("Calculator Agent result:", result)
        # Returns the raw math output directly, preserving absolute precision
        return result

    # ---------------------------------------------
    # Research Agent (Requires LLM formatting)
    # ---------------------------------------------
    if "research_agent" in decision.lower():
        result = research_agent(user_message)
        print("Research Agent result:", result)
        return create_final_response(user_message, "Research Agent", result)

    # ---------------------------------------------
    # Simple conversation
    # ---------------------------------------------
    return decision

# ---------------------------------------------
# Supervisor creates final response for Research
# ---------------------------------------------
def create_final_response(user_message: str, agent_name: str, result: str):
    print("\n[Supervisor Final Response]")
    response = chat(
        model=MODEL,
        messages=[
            {
                "role": "system",
                "content": f"""
                You are the Supervisor Agent. The specialized agent "{agent_name}" has completed the user's task.
                Create the final answer for the user using the result provided by that agent.
                Do not mention internal agents unless necessary.
                Do not say that you are delegating the task.
                Give only the useful final answer.
                """
            },
            {
                "role": "user",
                "content": user_message
            },
            {
                "role": "assistant",
                "content": f"{agent_name} result: {result}"
            }
        ]
    )
    
    final_result = response["message"]["content"]
    print("Final response:", final_result)
    return final_result
