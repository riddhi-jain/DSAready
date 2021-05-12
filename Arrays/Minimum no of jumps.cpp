/*Given an array of integers where each element represents the max number of steps that can be made forward from that element. 
Find the minimum number of jumps to reach the end of the array (starting from the first element).
If an element is 0, then you cannot move through that element.
Print -1 if it is impossible to reach the end.*/

/*Algorithm: 

Variables to be used: 
1.maxReach = arr[0] : The variable maxReach stores at all time the maximal reachable index in the array.
2.step = arr[0] : The variable step stores the number of steps we can still take(and is initialized with value at index 0, i.e. initial number of steps)
3.jump = 1 : jump stores the amount of jumps necessary to reach that maximal reachable position.

starting from index 1,
1.First we test whether we have reached the end of the array, in that case we just need to return the jump variable.
2.Next we update the maxReach. This is equal to the maximum of maxReach and i+arr[i](the number of steps we can take from the current position). 
3.We used up a step to get to the current index, so steps has to be decreased. 
4.If no more steps are remaining (i.e. steps=0, then we must have used a jump. Therefore increase jump. Since we know that it is possible somehow to reach maxReach, we again initialize the steps to the number of steps to reach maxReach from position i.
But before re-initializing step, we also check whether a step is becoming zero or negative. In this case, It is not possible to reach further. */


#include<bits/stdc++.h>
using namespace std;

class Solution{
  public:
    int max(int x, int y){
            return (x>y) ? x :y;
        }
    int minJumps(int arr[], int n)
    {
        // Your code here
        if(arr[0] == 0){
            return -1;
        }
        if(n <= 1){
            return 0;
        }
        int maxReach = arr[0];
        int steps = arr[0];
        int jumps = 1;
        for (int i = 1; i<n; i++){
            if(i == n-1){
                return jumps;
            }
            maxReach = max(maxReach, i + arr[i]);
            steps--;
            if(steps == 0){
                jumps++;
                if(i >= maxReach){
                    return -1;
                }
                steps = maxReach - i;
            }
            
        }
        return -1;
        }
int main()
{
    int t;
    cin>>t;
    while(t--)
    {
        int n,i,j;
        cin>>n;
        int arr[n];
        for(int i=0; i<n; i++)
            cin>>arr[i];
        Solution obj;
        cout<<obj.minJumps(arr, n)<<endl;
    }
    return 0;
}

