import vertexai
from agent import root_agent # modify this if your agent is not in agent.py

# TODO: Fill in these values for your project
PROJECT_ID = "ai-agents-474107"
LOCATION = "us-central1"  # For other options, see https://cloud.google.com/vertex-ai/generative-ai/docs/agent-engine/overview#supported-regions
STAGING_BUCKET = "gs://vamsee-agent-bucket"
"

# Initialize the Vertex AI SDK
vertexai.init(
    project=PROJECT_ID,
    location=LOCATION,
    staging_bucket=STAGING_BUCKET,
)

from vertexai import agent_engines

# Wrap the agent in an AdkApp object
app = agent_engines.AdkApp(
    agent=root_agent,
    enable_tracing=True,
)