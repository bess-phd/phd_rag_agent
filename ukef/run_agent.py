import asyncio
from agent_framework.azure import AzureAIClient
from azure.identity.aio import DefaultAzureCredential

AGENT_ID = "UKEF1:8"
ENDPOINT = "https://phd-agent-ukef-resource.services.ai.azure.com/api/projects/phd_agent_ukef"
MODEL_DEPLOYMENT_NAME = "gpt-4o-mini"

# Case context - can be customized
case_data = """Kamil Changan Consultancy
- Location: UK-based
- Export History (last 3 financial years):
  * Year 1 (2023-2024): 5% of annual turnover from exports
  * Year 2 (2024-2025): 5% of annual turnover from exports
  * Year 3 (2025-2026): 7% of annual turnover from exports
- Proposed Project: Consultancy contract in South Sudan
- Project Value: TBD
- UK Content: TBD"""

async def ask_agent(agent, question):
    """Ask a single question to the agent."""
    try:
        full_prompt = f"{question}\n\nContext: {case_data}"
        result = await agent.run(full_prompt)
        return result.text
    except Exception as e:
        return f"❌ Error: {str(e)}"

async def interactive_chat():
    """Interactive chat loop with the UKEF agent."""
    # Configuration check
    if AGENT_ID == "asst_PASTE_YOUR_ID_HERE":
        print("❌ ERROR: Please update AGENT_ID in the script")
        print("   1. Go to Azure AI Foundry")
        print("   2. Open your agent")
        print("   3. Copy the agent ID (usually starts with 'asst_')")
        return
    
    try:
        async with DefaultAzureCredential() as credential:
            client = AzureAIClient(
                project_endpoint=ENDPOINT,
                model_deployment_name=MODEL_DEPLOYMENT_NAME,
                agent_name="UKEF-Agent",
                credential=credential,
            )
            
            async with client.as_agent(agent_id=AGENT_ID) as agent:
                # Welcome banner
                print("\n" + "="*60)
                print("🤖 UKEF Export Finance Policy Agent")
                print("="*60)
                print("💼 Company: Kamil Changan Consultancy")
                print("📊 Export History: 5% → 5% → 7% (meets 5% rule)")
                print("🌍 Project: South Sudan Consultancy")
                print("-"*60)
                print("Commands:")
                print("  'exit' or 'quit' - Exit the chat")
                print("  'help'          - Show example questions")
                print("  'case'          - Show case data")
                print("="*60 + "\n")
                
                # Interactive loop
                while True:
                    try:
                        user_input = input("📝 Your question: ").strip()
                        
                        if not user_input:
                            continue
                        
                        # Handle commands
                        if user_input.lower() in ['exit', 'quit']:
                            print("\n👋 Goodbye!\n")
                            break
                        
                        if user_input.lower() == 'help':
                            print("\n💡 Example Questions:")
                            print("  • Is Kamil Changan eligible for UKEF?")
                            print("  • What is the 5% rule?")
                            print("  • Analyze South Sudan country risk")
                            print("  • Should UKEF support this project?")
                            print("  • What is the 20% export intensity rule?\n")
                            continue
                        
                        if user_input.lower() == 'case':
                            print("\n📋 Case Data:")
                            print(case_data)
                            print()
                            continue
                        
                        # Ask the agent
                        print("\n🔄 Processing...\n")
                        response = await ask_agent(agent, user_input)
                        print("🤖 Agent:")
                        print("-" * 60)
                        print(response)
                        print("-" * 60 + "\n")
                    
                    except KeyboardInterrupt:
                        print("\n\n👋 Chat ended (Ctrl+C)")
                        break
    
    except Exception as e:
        print(f"\n❌ ERROR: {str(e)}")
        print("\nTroubleshooting:")
        print("  1. Verify ENDPOINT is correct")
        print("  2. Verify MODEL_DEPLOYMENT_NAME is correct")
        print("  3. Ensure Azure credentials are configured")
        print("  4. Check agent exists in Azure AI Foundry\n")

if __name__ == "__main__":
    asyncio.run(interactive_chat())
