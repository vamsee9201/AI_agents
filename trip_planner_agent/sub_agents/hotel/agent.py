from google.adk.agents import Agent
from google.adk.tools.agent_tool import AgentTool
#from trip_planner_agent.tools import get_directions
#from prompt import SAMPLE_INSTRUCTION
from trip_planner_agent.tools import get_hotels


hotel_agent = Agent(
    model="gemini-2.5-flash",
    name="hotel_agent",
    description="give information on hotels near the specified address",
    instruction="""
    you are a helpful agent that gets the nearest hotels near the specified address
    """,
    tools=[get_hotels]
)