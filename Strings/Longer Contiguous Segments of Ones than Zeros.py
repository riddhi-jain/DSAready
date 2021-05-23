'''Given a binary string s, return true if the longest contiguous segment of 1s is strictly longer than the longest contiguous segment of 0s in s. Return false otherwise.

For example, in s = "110100010" the longest contiguous segment of 1s has length 2, and the longest contiguous segment of 0s has length 3.
Note that if there are no 0s, then the longest contiguous segment of 0s is considered to have length 0. The same applies if there are no 1s.'''

class Solution:
    def checkZeroOnes(self, l0: str) -> bool:
        self.l0 = l0
        temp = 1
        num_1 = 0
        num_0 = 0
        for i in range(1,len(l0)):
            curr_1 = 0
            curr_0 = 0
            if(int(l0[i]) - int(l0[i-1]) == 0):
                temp+=1
            elif(int(l0[i]) - int(l0[i-1] )== -1):
                curr_1 = temp 
                if(curr_1 > num_1 ):
                    num_1 = curr_1
                temp = 1
            else:
                curr_0 = temp
                if(curr_0 > num_0 ):
                    num_0 = curr_0
                temp = 1
        if(l0[-1] == '0'):
            if(num_0 < temp):
                num_0 = temp
        else:
            if(num_1 < temp):
                num_1 = temp
        
        if(num_1 > num_0):
            return True
        else:return False
        
