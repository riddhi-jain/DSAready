/*
Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.
Follow up: Could you implement a solution using only O(1) extra space complexity and O(n) runtime complexity?
Example :
Input: nums = [3,0,1]
Output: 2
Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.

Logic :

We will keep a boolean array track and mark the index of what the value in array occurs as 1 and finally the value which don't occur is  0 and we can print it.
*/
#include<iostream>
using namespace std;

int main(){
    int n;
    std::cout<<"Enter the number of Inputs : ";
    std::cin>>n;
    int a[n];
    bool b[n+1]  ={0};
    for(int i=0; i<n; i++){
        std::cin>>a[i];
        b[a[i]] = 1;
    }
    for(int i=0; i<n; i++){
        if(b[i]==0){
            std::cout<<i<<endl;
            break;
        }
    }
}
