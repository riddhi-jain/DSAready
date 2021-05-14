'''Given an array of positive and negative numbers, 
arrange them in an alternate fashion such that every positive number is followed by negative and vice-versa maintaining the order of appearance. 
Number of positive and negative numbers need not be equal. 
If there are more positive numbers they appear at the end of the array. If there are more negative numbers, they too appear in the end of the array.
MAKE SURE YOU USE ONLY O(1) EXTRA SPACE'''

arr = list(map(int, input().split()))
n = len(arr)
print(arr)
neg = 0
prev = 0
for i in range(n):
    if(arr[i] < 0):
        neg+=1 
for i in range(n):
    if(neg>0):
        if(arr[i] < 0 and i%2 == 1):
            for j in range(i+1, n):
                curr = arr[j]
                if(arr[j] >= 0):
                    arr.pop(j)
                    arr.insert(prev+1, curr)
                    break
        elif(arr[i] >= 0 and i%2 == 0):
            for j in range(i+1, n):
                curr = arr[j]
                if(arr[j] < 0):
                    arr.pop(j)
                    arr.insert(prev+2, curr)
                    break
            neg-=1 
            prev = i 
        elif(arr[i] < 0 and i%2 == 0):
            neg-=1 
            prev = i 
print(arr)
    
