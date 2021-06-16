/*Question-:Given an array, rotate the array by one position in clock-wise direction.
Input:
N = 5
A[] = {1, 2, 3, 4, 5}
Output:
5 1 2 3 4

Approach:-
Store the first element in a temp variable and shift the elements by one in clockwise direction
*/

class Compute {
    
    public void rotate(long arr[], long n)
    {
        long temp=arr[arr.length-1];
     for(int i=arr.length-2;i>=0;i--){
         arr[i+1]=arr[i];
     }
     arr[0]=temp;
    }
}
