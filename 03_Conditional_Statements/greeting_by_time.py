import time
timenow= time.strftime('%H:%M:%S')
print(timenow)
hournow= int(time.strftime('%H'))
print(hournow)
if 5 <= hournow < 12:
    print("Good Morning!")
elif 12 <= hournow < 17:
    print("Good Afternoon!")
elif 17 <= hournow < 21:
    print("Good Evening!")
else:
    print("Good Night!")   

      