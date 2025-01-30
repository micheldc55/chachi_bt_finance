from langchain.agents import Tool

from src.stock_data.data_extraction import get_stock_data


financial_data_tool = Tool(
    name="get_stock_data",
    func=get_stock_data,
    description=(
        "Use this tool to get real-time or near real-time market data for a stock. "
        "Input should be the stock ticker symbol (e.g., 'AAPL', 'TSLA')."
    )
)