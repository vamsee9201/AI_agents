from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
from trip_planner_agent.tools import get_directions
#from prompt import SAMPLE_INSTRUCTION


transport_agent = Agent(
    model="gemini-2.5-flash",
    name="transport_agent",
    description="give the directions information between two locations",
    instruction="you are a helpful assistant that can give the directions information between two locations",
    tools=[get_directions]
)