
#This script connects to Azure OpenAI, asks GPT-4o the question “I am going to Paris, what should I see?”, and prints the assistant’s answer.
#It’s basically a Python client demo for Azure OpenAI Chat Completions API.

import os
from openai import AzureOpenAI

endpoint = "https://nitishpandey24-8531-resource.cognitiveservices.azure.com/"
model_name = "gpt-4o"
deployment = "gpt-4o"

subscription_key = "GFvatKksGHi2BTn7teQf0J4I7U4oPtm7L3w3wNxhZJM9o1ZCG7EGJQQJ99BHACHYHv6XJ3w3AAAAACOGRLdh"
api_version = "2024-12-01-preview"

client = AzureOpenAI(
    api_version=api_version,
    azure_endpoint=endpoint,
    api_key=subscription_key,
)

response = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "I am going to Paris, what should I see?",
        }
    ],
    max_tokens=4096,
    temperature=1.0,
    top_p=1.0,
    model=deployment
)

print(response.choices[0].message.content)