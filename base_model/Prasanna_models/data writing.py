import csv
import datetime

filename = "aapl.csv"

i=0
while(i<4):


 with open(filename, 'r') as csvfile:
       reader = csv.reader(csvfile)
       rows = list(reader)

       print(rows[0])

       count=int(rows[-1][2])+1


       stack=[]    
       stack.append(x) 
       stack.append(count)
       stack.append("oombu")
       print(stack)
       i+=1

 with open(filename, 'w') as csvfile:
    # creating a csv writer object
    x = datetime.datetime.now()
    x=str(x).split(" ")

    csvwriter = csv.writer(csvfile)

    dateobj=x[0]
    print("rows",len(rows))
    csvwriter.writerows(stack)