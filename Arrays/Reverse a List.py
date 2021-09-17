#Problem Statement : Reversing a List.

#Approach : 
"""
Step1 : Find the "mid" of the List.
Step2 : Take two pointers. initial >> start pointer , last >> end pointer
Step3 : Keep running the loop until initial < last or mid-1 does not equals to zero.
Step4 : Swap the element at initial position with the element at the last position.
Step5 : increment mid, initial by 1 and decrement last by 1.

Note : It will reverse the existing list, won't take a new list.
"""
#Below is the code:

List = [23 , 12, 11, 10 , 76]
mid = len(List) // 2
initial = 0
last = -1
while (mid-1) > -1:
    temp = List[initial]
    List[initial] = List[last]
    List[last] = temp
    mid -= 1
    last -=1 
    initial += 1
print(List)