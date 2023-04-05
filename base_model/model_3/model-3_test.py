import openai
# sample question : my wife died last year i cannot get through that
openai.api_key = "OPENAI_API_KEY"

# Define the model you want to use------------this model is generated using data3 and finetuned with text-davinci-002
model_engine = "davinci:ft-personal-2023-03-19-20-39-50"

prompt = input("You: ")

#i'll take diferent temps and generate responses..
def start(text,n):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=n,
    )
    return response.choices[0].text
# completions list:
ans=[]

# differnt temps:
nums=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]

n_=0
for n in nums:
  n_+=1
  ans.append(start(prompt,n))
  print(f'epoch {count}/9')
print("Here's the responses---\n")
print(ans)
