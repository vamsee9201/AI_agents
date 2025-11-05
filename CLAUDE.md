# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

This repository contains multiple AI agent implementations using Google's Agent Development Kit (ADK) and Vertex AI. The agents are designed to provide specialized capabilities through a modular, hierarchical architecture.

## Architecture

### Agent Hierarchy

The project follows a **hierarchical agent architecture** where:
- **Root agents** coordinate high-level tasks and delegate to specialized sub-agents
- **Sub-agents** handle specific domains (e.g., transport, weather)
- **Tools** provide atomic functionality (e.g., API calls, data processing)

### Key Modules

1. **trip_planner_agent/** - Travel planning agent using Google Maps API
   - Root agent (`agent.py`) - Travel concierge that orchestrates sub-agents
   - `sub_agents/transport/` - Handles route planning and directions
   - `tools.py` - Google Maps Routes API integration for multi-modal transport

2. **multi_tool_agent/** - General-purpose agent with time/weather capabilities
   - Demonstrates basic tool integration pattern
   - Uses mock data for demonstration

### Agent Configuration Pattern

All agents follow this configuration structure:
```python
Agent(
    model="gemini-2.5-flash" or "gemini-2.0-flash",
    name="agent_name",
    description="Brief description for delegation",
    instruction="Detailed prompt for agent behavior",
    tools=[list_of_functions],
    sub_agents=[list_of_agents]  # Optional, for hierarchical agents
)
```

## Development Setup

### Prerequisites
- Python 3.13
- Google Cloud Platform account with Vertex AI enabled
- Google Maps API key (for trip_planner_agent)

### Environment Configuration

Each agent module requires a `.env` file:
- `trip_planner_agent/.env` - Contains environment variables
- `multi_tool_agent/.env` - Contains environment variables

API keys are stored separately:
- `trip_planner_agent/google_maps_api.json` - Format: `{"api_key": "YOUR_KEY"}`

**Important:** Never commit `.env` files or `google_maps_api.json` (already in `.gitignore`)

### Installing Dependencies

```bash
# Activate virtual environment
source AI_agents/bin/activate

# Install Google ADK and dependencies
pip install google-cloud-aiplatform google-adk requests
```

### Running Agents Locally

Individual agents can be tested by importing and running them:
```bash
cd trip_planner_agent
python -c "from agent import root_agent; # interact with agent"
```

### Deploying to Vertex AI

Use the `deploy.py` pattern for Vertex AI deployment:

1. Update `deploy.py` with your GCP configuration:
   - `PROJECT_ID` - Your GCP project ID
   - `LOCATION` - Vertex AI region (e.g., "us-central1")
   - `STAGING_BUCKET` - GCS bucket for staging (format: "gs://bucket-name")

2. Deploy:
```bash
cd multi_tool_agent  # or trip_planner_agent
python deploy.py
```

## Google Maps Routes API Integration

The `trip_planner_agent` uses Google Routes API v2 for directions:

### API Endpoint
`https://routes.googleapis.com/directions/v2:computeRoutes`

### Travel Modes Supported
- DRIVE - Car/driving directions
- WALK - Walking directions
- BICYCLE - Cycling directions
- TRANSIT - Public transportation

### Key Function: `get_directions(origin, destination)`
- Returns routes for all travel modes
- Provides distance (km), duration, and toll information
- Origin/destination are address strings (e.g., "2726 phillips dr dallas")

## Code Organization Principles

### Adding New Sub-Agents

1. Create directory under `sub_agents/` (e.g., `sub_agents/hotels/`)
2. Implement `agent.py` with Agent configuration
3. Create `prompt.py` for instruction templates (optional)
4. Implement tools in parent `tools.py` or agent-specific module
5. Register sub-agent in root agent's `sub_agents` list

### Tool Development

Tools are Python functions with:
- Clear docstrings (used by LLM for tool selection)
- Type hints for parameters
- Dictionary returns with `status` and `report`/`error_message` keys

Example pattern:
```python
def tool_name(param: str) -> dict:
    """Description used by LLM to understand when to call this tool.

    Args:
        param (str): Description of parameter

    Returns:
        dict: status and result or error msg.
    """
    # Implementation
    return {"status": "success", "report": "result"}
```

## Working with API Keys

When adding new API integrations:
1. Store keys in JSON files (add to `.gitignore`)
2. Load keys at runtime: `json.load(open("path/to/key.json"))`
3. Use absolute paths for development, consider environment variables for production

## Testing

Currently manual testing via direct function calls. When adding tests:
- Test individual tools independently
- Test agent responses with various prompts
- Verify API integrations handle errors gracefully

## Common Patterns

### Hardcoded Paths
Several files contain hardcoded absolute paths (e.g., `/Users/vamseekrishna/Desktop/...` in `tools.py:18`). When modifying:
- Use relative paths from project root
- Consider `os.path.join()` for cross-platform compatibility
- Use environment variables for deployment-specific paths

### Model Selection
- `gemini-2.5-flash` - Latest model for root/transport agents
- `gemini-2.0-flash` - Used in multi_tool_agent example

## Git Workflow

Current branch: `main` (no separate development branches configured)

When committing:
```bash
git add .
git commit -m "descriptive message"
git push origin main
```
