import os
from dotenv import load_dotenv

from langchain_community.llms import OpenAI
from langchain.prompts import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.agents import AgentExecutor, initialize_agent, AgentType

from src.stock_data.langchain_tools import financial_data_tool


load_dotenv()  


llm = OpenAI(
    temperature=0.7,
    openai_api_key=os.getenv("OPENAI_API_KEY")
)

memory = ConversationBufferMemory(memory_key="chat_history")

prompt = PromptTemplate(
    template=(
        "You are a financial assistant. You can use the get_stock_data tool when needed.\n\n"
        "User Message: {input}\n\n"
        "Remember, always consider data from the tool in your final answer.\n"
        "If the user asks for data about a specific stock ticker, use the tool.\n"
    ),
    input_variables=["input"]
)


agent_chain = initialize_agent(
    tools=[financial_data_tool],
    llm=llm,
    agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
    verbose=True, 
    memory=memory,
    prompt=prompt
)


def main():
    print("Welcome to the Real-Time Financial Insights Agent!")
    print("Type 'exit' to quit.\n")

    while True:
        print("Write a message to the Financial Agent (Not Financial Advice):")
        user_input = input("User: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        
        response = agent_chain.run(input=user_input)
        print(f"\nAgent: {response}\n")

if __name__ == "__main__":
    main()