from openai import OpenAI

# Initialize OpenAI client (insert your API key)
client = OpenAI(
    api_key="enter your API key"
)

# Read the prompt from an external text file
try:
    with open("prompt.txt", "r", encoding="utf-8") as prompt_file:
        prompt = prompt_file.read().strip()   # Load and clean the prompt text
except FileNotFoundError:
    # Handle the case where the prompt file is missing
    print("Error: The file 'prompt.txt' was not found. Please check the current working directory and the file name.")
    exit(1)

# Send the prompt to the model and request a completion
completion = client.chat.completions.create(
    model="gpt-4o-mini",
    store=True,  # Optional: stores the conversation for future retrieval if enabled
    messages=[
        {"role": "user", "content": prompt}
    ]
)

# Extract the generated response from the model
output_message = completion.choices[0].message.content

# Save the model's output to a text file
with open("output.txt", "w", encoding="utf-8") as output_file:
    output_file.write(output_message)

print("Output has been written to output.txt")
