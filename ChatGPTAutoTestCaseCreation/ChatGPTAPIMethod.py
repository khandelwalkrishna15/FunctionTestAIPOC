import openai

# Set your API key here
openai.api_key = "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"
#openai.api_key = "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"
#openai.api_key = "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"

# Define a conversation with user and assistant messages
conversation = [
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Who is the PM of India?"},
]

# Generate a response
response = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=conversation,
)

# Extract the assistant's reply
assistant_reply = response['choices'][0]['message']['content']

# Use the assistant's reply
print(assistant_reply)
