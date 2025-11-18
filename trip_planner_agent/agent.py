
from google.adk.agents import SequentialAgent,Agent
from trip_planner_agent.tools import get_hotels
from trip_planner_agent.tools import get_directions
from google.adk.tools.agent_tool import AgentTool
#from trip_planner_agent.sub_agents.transport.agent import transport_agent
#from trip_planner_agent.sub_agents.hotel.agent import hotel_agent

#steps to do
#first add the agents here
#second test if that is working
#add state to that
#test if it is working

#State Keys
NEAREST_HOTELS = "nearest_hotels"

hotel_agent = Agent(
    model="gemini-2.5-flash",
    name="hotel_agent",
    description="give information on hotels near the specified address",
    instruction="""
    you are a helpful agent that gets the nearest hotels near the specified address
    """,
    tools=[get_hotels],
    output_key=NEAREST_HOTELS
)

transport_agent = Agent(
    model="gemini-2.5-flash",
    name="transport_agent",
    description="give the directions information between two locations",
    instruction="""you are a helpful assistant that can give the directions information between two locations 
    hotel address : {nearest_hotels} and original address
    give the directions for all available travel modes
    give the distance
    give the duration
    """,
    tools=[get_directions]
)






root_agent = SequentialAgent(
    name="RefinementLoop",
    # Agent order is crucial: Critique first, then Refine/Exit
    sub_agents=[
        hotel_agent,
        transport_agent,
    ],
    description="executes by getting the address of the hotel closest to the given address and then uses the transport agent to get the directions between those two locations",
)

#test