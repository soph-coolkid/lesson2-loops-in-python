word=input("Type any word")
count=0
for i in word:
    if i in "aeiou":
        count=count+1
print("vowels=",count)        