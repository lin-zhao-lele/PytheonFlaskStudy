import openai

# Define OpenAI API key
openai.api_key = "sk-"

# Set up the model and prompt
model_engine = "text-davinci-003"
prompt = "Once upon a time, in a land far, far away, there was a princess who..."

# Generate a response
completion = openai.Completion.create(
    engine=model_engine,
    prompt=prompt,
    max_tokens=1024,
    n=1,
    stop=None,
    temperature=0.5,
)

# The above code will generate a response to the defined prompt using the ChatGPT model.
# The response will be returned as a string in the response variable.
#
# The temperature parameter controls the level of randomness in the output. The higher the temperature,
# the more varied and less coherent response output, you can adjust based on your experiment. stop defines the stop condition.

response = completion.choices[0].text
print(response)