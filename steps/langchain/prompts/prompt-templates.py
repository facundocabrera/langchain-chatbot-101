# How to build prompts (it is just a template engine)

# required to format the output to console
import json

# few classes to see how they represent different type of messages
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

# the content argument is used to populate the message structure
human = HumanMessage(content="Translate this sentence from English to French: I love programming.")
ai = AIMessage(content="J'aime programmer.")
system = SystemMessage(content="Correct!")

# serialize the objects to see how they looks internally
out = json.dumps([human.to_json(), ai.to_json(), system.to_json()], indent=2)

# pay attention to the output and how the objects differenciate from each other
print(out)
