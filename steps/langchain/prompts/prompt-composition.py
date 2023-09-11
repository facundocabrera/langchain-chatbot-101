from langchain.prompts.pipeline import PipelinePromptTemplate
from langchain.prompts.prompt import PromptTemplate

# Define a fstring and use it as a template for a prompt, you can give any
# structure you would like
full_template = """
{task}

{example}

{start}
"""
full_prompt = PromptTemplate.from_template(full_template)

# Lets define the {task} part of the prompt
task_template = """You are impersonating {person}."""
task_prompt = PromptTemplate.from_template(task_template)

# Lets define the {example} part of the prompt
example_template = """Here's an example of an interaction: 

Q: {example_q}
A: {example_a}"""
example_prompt = PromptTemplate.from_template(example_template)

# Lets define the {start} part of the prompt
start_template = """Now, do this for real!

Q: {input}
A:"""
start_prompt = PromptTemplate.from_template(start_template)

# Now we can define the pipeline prompt, which is a list of tuples
input_prompts = [
    ("task", task_prompt),
    ("example", example_prompt),
    ("start", start_prompt)
]
pipeline_prompt = PipelinePromptTemplate(
    final_prompt=full_prompt, pipeline_prompts=input_prompts, input_variables=[])

print(
    "VARIABLES:",
    pipeline_prompt.input_variables, "\n"
)

print(
    "INSTANCE:",
    pipeline_prompt.format(
    person="Leo Messi",
    example_q="Cual es tu deporte favorito?",
    example_a="Futbol, claramente",
    input="Cual es tu país favorito?"
))
