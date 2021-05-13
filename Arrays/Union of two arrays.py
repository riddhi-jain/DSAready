#Given two arrays a[] and b[] of size n and n respectively. 
#The task is to find no. of elements in union between these two arrays.

class Solution:    
    #Function to return the count of number of elements in union of two arrays.
    def doUnion(self,a,n,b,m):
        d = {x: a.count(x) for x in a}
        e = {x: b.count(x) for x in b}
        if n>m:
            sum = len(d.keys())
            for key in e.keys():
                if key in d:pass
                else:sum+=1
        else:
            sum = len(e.keys())
            for key in d.keys():
                if key in e:pass
                else: sum+=1
        return sum
        
        
if __name__=='__main__':
    t=int(input())
    for _ in range(t):
        
        n,m=[int(x) for x in input().strip().split()]
        
        a=[int(x) for x in input().strip().split()]
        b=[int(x) for x in input().strip().split()]
        ob=Solution()
        
        print(ob.doUnion(a,n,b,m))
