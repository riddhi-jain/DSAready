/*An array contains both positive and negative numbers in random order.
Rearrange the array elements so that all negative numbers appear before all positive numbers.*/

import java.io.*;
import java.util.*;

class GFG {
    static void rearrange(int arr[], int n)
    {
        int j = 0,temp;
        for (int i = 0; i<n;i++)
        {
            if(arr[i] < 0)
            {
                temp = arr[i];
                arr[i] = arr[j];
                arr[j] = temp;
                j = j+1;
            }
        }
    }
    public static void main(String args[])
    {
        int arr[] = {-1,2,-3,4,5,6,-7,8,9};
        int n = arr.length;
        rearrange(arr, n);
        for(int i =0; i<n; i++){
        System.out.print(arr[i] + " ");
        }
    }
}