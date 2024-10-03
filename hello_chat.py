from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

# get the llms
llm = Ollama(model="llama3.1:latest", request_timeout=120.0)

# setup messages
messages = [
    ChatMessage(
        role="system", content="You are a pirate with a colorful personality"
    ),
    ChatMessage(role="user", content="Who is Ada Lovelace?"),
]

# chat
resp = llm.chat(messages)

# print
print(resp)