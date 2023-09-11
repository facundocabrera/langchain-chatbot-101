from pathlib import Path

# All prompts are loaded through the `load_prompt` function.
from langchain.prompts import load_prompt

input_path = Path(__file__) / ".." / ".." / ".." / ".." / "data" / "prompts" / "example.yaml"
input_path = input_path.resolve()

# Load yml into a BasePromptTemplate
prompt = load_prompt(input_path)

# Replace the variables in the prompt with the values provided.
print(prompt.format(adjective="funny", content="chickens"))
