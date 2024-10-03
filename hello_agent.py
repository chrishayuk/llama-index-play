from tools import tools
from llama_index.core.agent import AgentRunner, ReActAgentWorker, ReActAgent
from llama_index.llms.ollama import Ollama
from llama_index.core.llms import ChatMessage

# get the llms
llm = Ollama(model="llama3.1:latest", request_timeout=120.0)

# react agent
agent = ReActAgent.from_tools(tools, llm=llm, verbose=True)

# create a task
task = agent.create_task("What is (121 * 3) + 42?")

# run the step
step_output = agent.run_step(task.task_id)

# repeat until the last step is reached
while not step_output.is_last:
    step_output = agent.run_step(task.task_id)
    print(f"step output: {step_output}")
    for item in task.extra_state["current_reasoning"]:
        # thought
        if(hasattr(item, "thought")):
            print(item.thought)

        # action
        if(hasattr(item, "action")):
            print(item.action)

        # action
        if(hasattr(item, "action_input")):
            print(item.action_input)

        # thought
        if(hasattr(item, "observation")):
            print(item.observation)

# show final answer
response = agent.finalize_response(task.task_id)