import requests

API_URL = "https://api-inference.huggingface.co/models/cardiffnlp/twitter-roberta-base-sentiment"
headers = {"Authorization": "Bearer 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"}

def query(payload):
	response = requests.post(API_URL, headers=headers, json=payload)
	return response.json()
	
output = query({
	"inputs": "I like you. I love you",
})

print(output)

list_score=[]
list_star=[1,2,3,4,5]
for i in (output):
	for j in i:
		print(j)
		list_score.append(j['score'])
		
print(list_score)