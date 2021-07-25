/*

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, 
such as pow(x, 0.5) or x ** 0.5.
 
Logic :

Start iterating with a variable say i = 1 . If i*i = n then return n
else find smallest i which is strictly greater than n and Apply Procedure 
similar as Binary Search Algorithm.
Check the halfs of the choosen range by Recurrsion.

*/

#include<iostream>
using namespace std;

double root(double n, double left, double right){
    double mid = (left+right)/2;
    double mul = mid*mid;
    if(mul==n){
        return mid;
    }else if(mul<n){
        return root(n,mid,right); 
    }else{
        return root(n,left,mid);
    }
}

int main(){
    double n;
    std::cin>>n;
    double i = 1;
    bool check = 0;
    while(check==0){
        if(i*i==n){
            check = 1;
            std::cout<<i;
        }else if(i*i>n){
            double ans = root(n,i-1,i);
            std::cout<<ans;
            check = 1;
        }
        i++;
    }
    return 0;
}