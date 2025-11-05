
from google.adk.agents import LoopAgent,Agent
from trip_planner_agent.sub_agents.transport.agent import transport_agent

from trip_planner_agent.sub_agents.hotel.agent import hotel_agent


#State Keys
NEAREST_HOTEL = "nearest_hotel"




root_agent = LoopAgent(
    name="RefinementLoop",
    # Agent order is crucial: Critique first, then Refine/Exit
    sub_agents=[
        hotel_agent,
        transport_agent,
    ],
    description="this will return the nearest hotel address to the desired destination and give transportation details",
    max_iterations=3 # Limit loops
)