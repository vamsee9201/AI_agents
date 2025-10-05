
from google.adk.agents import Agent
from trip_planner_agent.sub_agents.transport.agent import transport_agent

root_agent = Agent(
    model="gemini-2.5-flash",
    name="root_agent",
    description="A Travel Conceirge using the services of multiple sub-agents",
    instruction="You are a helpful assistant that can answer the best transport mode to reach the destination.",
    sub_agents=[
        transport_agent,
    ],
    )