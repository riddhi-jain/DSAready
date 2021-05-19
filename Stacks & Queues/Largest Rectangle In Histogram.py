'''
Given an array of integers heights representing the histogram's bar
height where the width of each bar is 1, return the area of the
largest rectangle in the histogram.
'''

def Largest_Rectangle_In_Histogram(height):
    height.append(0)
    res = 0
    st = [-1]
    for i in range(len(height)):
        # store the heights in increasing order in the stack
        while height[i]<height[st[-1]]:
            h = height[st.pop()]
            w = i - st[-1] - 1
            res = max(res,h*w)
        st.append(i)
    height.pop()
    return res

height = [2,1,5,6,2,3]
print(Largest_Rectangle_In_Histogram(height))
