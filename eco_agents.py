from azure.identity import DeviceCodeCredential
from openai import AzureOpenAI
import os



client = AzureOpenAI(
    azure_endpoint="https://YOUR-RESOURCE-NAME.openai.azure.com/",
    api_version="2024-02-01",
    azure_ad_credential=DeviceCodeCredential()
)

response = client.chat.completions.create(
    model="eco-gpt4o",
    messages=[
        {"role": "system", "content": "You are an AI sustainability analyst."},
        {"role": "user", "content": "Estimate the carbon cost of training a 70B parameter model."}
    ]
)

print(response.choices[0].message.content)