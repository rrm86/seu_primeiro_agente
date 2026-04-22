from langchain.agents import create_agent
from langchain.tools import tool
from langchain_google_genai import ChatGoogleGenerativeAI

@tool(description="Confirmar inscricao na comunidade TOP HAWKS")
def confirmar_inscricao_comunidade() -> str:
    return f"Sua inscrição foi confirmada com sucesso! Agora você vai construir com IA"

prompt = """
Você é um assistente de matricula na comunidade TOP HAWKS.
A comunidade é para pessoas que querem construir soluções profissionais de sucesso.
"""

hawk = create_agent(
    model=ChatGoogleGenerativeAI(model="gemma-4-31b-it"),
    tools=[confirmar_inscricao_comunidade],
    system_prompt=prompt,
)
