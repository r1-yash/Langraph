from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent
from langchain_groq import ChatGroq


from dotenv import load_dotenv
load_dotenv()

import asyncio 

async def main():
    client = MultiServerMCPClient(
        {
            "math":{ #this is ugn absolute pat stdio format 
                "command":"python",
                "args":["/Users/yashsinghal/Desktop/Agentic Ai/Langraph/3-MCPdemo/1-mathMCP.py"],
                "transport":"stdio",
            },
            "weather":{ #this is running on http 
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )   
    import os
    os.environ["GROQ_API_KEY"] = os.getenv("GROQ_API_KEY")

    tools = await client.get_tools()
    model = ChatGroq(model="openai/gpt-oss-120b")
    agent = create_agent(
        model=model,
        tools=tools
    )

    math_response = await agent.ainvoke(
        {"messages": [{"role": "user", "content": "how is weather in california"}]}
    )

    print("Math response:", math_response['messages'][-1].content)

asyncio.run(main())
        
    
