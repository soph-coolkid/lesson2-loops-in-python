word=input("Type any word")
count=0
for i in word:
    if i in "aeiou":
        count=count+1
print("vowels=",count) 
count=0
for q in word:
    if q in "qwrtypsdfghjklzxcvbnm":
        count=count+1
print("consents=",count)
       