# Add memory to store input and outputs over time as in a conversation

# You could find more here:
# https://linuxhint.com/to-initialize-chains-with-memory-objects-in-langchain-simply-use-the-llm-and-buffermemory-modules-and-chat-model-to-configure-the-chatbot-and-then-test-it/

from langchain.memory import (
    ConversationBufferMemory,
    # ConversationBufferWindowMemory 
)

from langchain.schema import (
    HumanMessage,
    SystemMessage
)

from langchain.prompts import (
    ChatPromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
    HumanMessagePromptTemplate,
)

# Prompt 
prompt = ChatPromptTemplate(
    messages=[
        SystemMessagePromptTemplate.from_template(
            "You are a nice chatbot having a conversation with a human."
        ),
        # The `variable_name` here is what must align with memory
        MessagesPlaceholder(variable_name="chat_history"),
        HumanMessagePromptTemplate.from_template("{question}")
    ],
    input_variables=["chat_history", "question"]
)

# Notice that we `return_messages=True` to fit into the MessagesPlaceholder
# Notice that `"chat_history"` aligns with the MessagesPlaceholder name
memory = ConversationBufferMemory(memory_key="chat_history",return_messages=True)

# Lets format the prompt and see how it looks without any messages in the memory
print(
    "EMPTY MEMORY:"
)
print(
    prompt.format(
        chat_history=memory.buffer_as_messages,
        question="Hey chatbot! I've a question for you..."
    )
)

# Lets add few messages to see how the memory placeholder works
memory.chat_memory.add_message(
    HumanMessage(content=">>> Hey chatbot! This is a message from memory!")
)
memory.chat_memory.add_message(
    SystemMessage(content=">>> Finally you got how it works! Congrats!")
)

# Lets format the prompt and see how it looks
print(
    "FEW MESSAGES IN THE MEMORY:"
)
print(
    prompt.format(
        chat_history=memory.buffer_as_messages,
        question="Hey chatbot! I've a question for you..."
    )
)
