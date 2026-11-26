total = 0
for i in range(1,11):
    total+= i

print("sum =",total)

num = 0
while num < 11:
    print(num,end=" ")
    num+=1


scores = [80,92,78,98,88]
total = 0
for score in scores:
    print("Sore:", score)
    total += score
average = total / len(scores)
print("Average:", average)

score = -1

while score <0 or score > 100:
    score = int(input("enter a score from 0 to 100:"))
    if score < 0 or score > 100:
        print ("invalid score. try again.")
print("vaild score:", score)