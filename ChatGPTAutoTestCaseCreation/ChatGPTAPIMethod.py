import openai

# Set your API key here
openai.api_key = "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"

# Define a conversation
conversation = [
    {"role": "system", "content": "Who is PM of india"},

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
