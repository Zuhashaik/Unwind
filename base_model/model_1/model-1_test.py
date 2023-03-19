
import openai
#  Setup your api key:
openai.api_key = "YOUR_OPEN_API_KEY"

# Define the model you want to use
model_engine = "davinci:ft-personal-2023-02-13-15-53-20"

print("Starting conversation...\n")

# Starting the conversation loop-----

# sample question : my wife died last year i cannot get through that..

while True:
    prompt = input("You: ")

    # Use the completions API to get a response
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=0.8,
    )
    print("\nModel: ", response.choices[0].text)
