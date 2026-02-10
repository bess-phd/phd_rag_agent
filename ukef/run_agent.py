import asyncio
from agent_framework.azure import AzureAIClient
from azure.identity.aio import DefaultAzureCredential

AGENT_ID = "UKEF1:8"
ENDPOINT = "https://phd-agent-ukef-resource.services.ai.azure.com/api/projects/phd_agent_ukef"
# Extract the model deployment name from the endpoint or set it explicitly
MODEL_DEPLOYMENT_NAME = "gpt-4o-mini"  # Change this to your actual model deployment name (check Azure AI Foundry)

case_data = "Kamil Changan Consultancy. UK-based. 7% export revenue. Project: South Sudan."

async def run_step(agent, instruction):
    """Run a single step with the agent."""
    try:
        result = await agent.run(f"{instruction}: {case_data}")
        return result.text
    except Exception as e:
        return f"Error: {str(e)}"

async def main():
    """Main function to run the agent."""
    # Check configuration
    if AGENT_ID == "asst_PASTE_YOUR_ID_HERE":
        print("ERROR: Please update AGENT_ID in the script with your actual agent ID from Azure AI Foundry")
        print("To get your AGENT_ID:")
        print("1. Go to Azure AI Foundry")
        print("2. Open your agent")
        print("3. Copy the agent ID (usually starts with 'asst_')")
        return
    
    try:
        async with DefaultAzureCredential() as credential:
            client = AzureAIClient(
                project_endpoint=ENDPOINT,
                model_deployment_name=MODEL_DEPLOYMENT_NAME,
                agent_name="UKEF-Agent",  # Required: alphanumeric and hyphens only, no underscores
                credential=credential,
            )
            # Get or use the agent
            async with client.as_agent(agent_id=AGENT_ID) as agent:
                print("\nStep 1: Checking Policy...")
                policy = await run_step(agent, "Check exporter eligibility under the 5% rule")
                print(policy)

                print("\nStep 2: Checking Country Risk...")
                risk = await run_step(agent, "Analyze South Sudan country risk under UKEF policy")
                print(risk)
    except Exception as e:
        print(f"ERROR: {str(e)}")
        print("\nTroubleshooting:")
        print("1. Verify ENDPOINT is correct (check Azure AI Foundry project settings)")
        print("2. Verify MODEL_DEPLOYMENT_NAME matches your deployment")
        print("3. Ensure your Azure credentials are configured correctly")
        print("4. Check that the agent exists in Azure AI Foundry")

if __name__ == "__main__":
    asyncio.run(main())
