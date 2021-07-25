/*

Given a non-negative integer x, compute and return the square root of x.
Since the return type is an integer, the decimal digits are truncated, 
and only the integer part of the result is returned.
Note: You are not allowed to use any built-in exponent function or operator, 
such as pow(x, 0.5) or x ** 0.5.
 
Logic :

Square Root of any number is less than its half. sqrt(n) <= (n/2)
We will keep storing the half of number in a temp variable and update the root 
variable to the other half which falls in the range and this keeps on shrinking the Range.

*/

#include<iostream>
using namespace std;

int main(){
    double n;
    std::cin>>n;
    
    double root = n/2;
    double temp = 0;

    while(root!=temp){
        temp = root;
        root = ( (n/temp) + temp ) / 2;
       // std::cout<<temp<<" "<<root<<endl; //Use this line to get inner insight of the math behind this.
    }
    printf("%f",root);
}