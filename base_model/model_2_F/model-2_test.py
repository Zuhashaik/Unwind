import openai

#  respective api key
openai.api_key = "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"

# Define the model you want to use...
#<curie with data2: curie:ft-personal-2023-03-16-17-46-04>
#<dacinci with data2: davinci:ft-personal-2023-03-16-17-16-59>

model_engine = "davinci:ft-personal-2023-03-16-17-16-59"

# my wife died last year i cannot get through this
prompt = input("You: ")

#i'll take diferent temps and generate responses..
def generate(text,n):
    response = openai.Completion.create(
        engine=model_engine,
        prompt=prompt,
        max_tokens=100,
        n=1,
        stop=None,
        temperature=n,
    )
    return response.choices[0].text

def print_ans(lst):
  for x in lst:
    print(x)


davinci_ans=[]
nums=[0.1,0.2,0.3,0.4,0.5,0.6,0.7,0.8,0.9]
count=0
for n in nums:
  count+=1
  davinci_ans.append(generate(prompt,n))
  print(f'epoch {count}/9')
print("Here's the responses for davinci model---\n")
print_ans(davinci_ans)

#changing model engine to curie...
model_engine = "curie:ft-personal-2023-03-16-17-46-04"

curie_ans=[]
count=0
for n in nums:
  count+=1
  curie_ans.append(generate(prompt,n))
  print(f'epoch {count}/9')
print("Here's the responses for curie model---\n")
print_ans(curie_ans)
