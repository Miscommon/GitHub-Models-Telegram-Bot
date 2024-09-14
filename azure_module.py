from azure.ai.inference import ChatCompletionsClient
from azure.ai.inference.models import SystemMessage, UserMessage
from azure.core.credentials import AzureKeyCredential

def response_request(text: str) -> str:
    endpoint = "https://models.inference.ai.azure.com"
    model_name = "gpt-4o"
    token = "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"

    client = ChatCompletionsClient(endpoint=endpoint, credential=AzureKeyCredential(token),)
    response = client.complete(
        messages=[
        SystemMessage(content="You are a helpful multilanguage assistant."),
        UserMessage(content=text),
        ],
        model=model_name,
        temperature=1.0,
        max_tokens=1000,
        top_p=1.0
    )
    
    module_response = response.choices[0].message.content
    return module_response