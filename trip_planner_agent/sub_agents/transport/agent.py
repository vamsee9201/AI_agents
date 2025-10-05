from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool

#from prompt import SAMPLE_INSTRUCTION


transport_agent = Agent(
    model="gemini-2.5-flash",
    name="transport_agent",
    description="provide the best transport mode to reach the destination",
    instruction="You are a helpful assistant that can answer the best transport mode to reach the destination.",
)