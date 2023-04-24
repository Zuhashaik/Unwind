import openai as openai2

def key_collector2(instances):
  if instances==2:
   #print("returns2")
   openai2.api_key="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" #prasanna0083

   return openai2
  else:
   openai2.api_key="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" #Sadik Shaik

   #print("returns3")
    
   return openai2

import openai

def key_collector(instances):
 #print("called")
 instances=instances%3
 if instances==1:
  openai.api_key="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" #83here
 else:
  return key_collector2(instances)
 
 #print("returns1")
 return openai

def reply(abc,currnet_query):
    print("YOU :"+currnet_query)

    print("ASSISTANT :",abc.choices[0].message.content)

def bot1(key1,prev):
     previous_query=prev

     # in the above if you didnt put the line  "previous_query=prev" and instead modified bot1(key1,previous_query) error raises....

     print("Transformer activated")
  
     currnet_query=str(input("current You:"))
         
     Transformer_Response=key1.ChatCompletion.create(
         model="gpt-3.5-turbo",
         messages=[{"role":"user","content":"Reply to the following like good therapist and remove all ai elements "+previous_query+" Now,"+currnet_query}]
   
         )
     
     #print(previous_query+ "Now," + currnet_query)
  
     reply(Transformer_Response,currnet_query)
     return currnet_query

k=4
currnet_query=""
previous_query=currnet_query

#context exchanging box

while(True):
    key=key_collector(k)
    #print(type(key))
    #print(key.api_key)
    ''
    previous_query=bot1(key,previous_query)
    k+=1