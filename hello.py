from llama_index.llms.ollama import Ollama

# get the llms
llm = Ollama(model="llama3.1:latest", request_timeout=120.0)

# perform the completion
resp = llm.complete("Who is Ada Lovelace?")

# print hello
print(resp)
