# Problem Statement : Given a number A, find the smallest number that has same set of digits as A and is greater than A.
# Time Complexity : O(N) 

def SmallestNumberSameSetOfDigitsAsA(A):
        A_list = list(map(int, A))
        l = len(A_list)
        i = 0
    # First we loop in the reverse order to find if there is an element greater
    # than any previously traversed element
    # If we do find one we break and continue to find the smallest number to the right of the
    # found number but if we don' it means the number is already in descending order
    # So there is no new combination to be found since it is already greater
        for i in range(l-1, 0, -1):
            if A_list[i] > A_list[i-1]:
                break
        if i == 1 and A_list[i] <= A_list[i-1]:
            return -1
        if i == 0: 
            return -1
        # from the executed for loop we have found the index of the number
        #smaller to the previously traversed number to be i-1
        #Now we are to find numbers on right side of i-1 and find the smallest number
        # to swap with the (i-1)th number
        pos = i # The start index for rightmost part of the string after i-1
        x = A_list[i-1]
        for j in range(i+1, l):
            if A_list[j] > x and A_list[j]<A_list[pos]:
                pos = j
        # After finding the smallest element we swap it with the (i-1)th element
        A_list[i-1],A_list[pos] = A_list[pos], A_list[i-1]
        
        # final_A = [str(int) for int in A_list]
        # super_final_A = "".join(final_A)
        super_final_A = 0
        for j in range(i):
            super_final_A = super_final_A* 10 + A_list[j]
        A_list = sorted(A_list[i:])
        for j in range(l-i):
            super_final_A = super_final_A * 10 + A_list[j]
        return super_final_A
A = "1234"
print(SmallestNumberSameSetOfDigitsAsA(A))
# Output : 1243