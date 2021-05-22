/*Given two sorted arrays arr1[] and arr2[] of sizes n and m in non-decreasing order. Merge them in sorted order without using any extra space. Modify arr1 so that it contains the first N elements and modify arr2 so that it contains the last M elements.

Approach-:
Swapping without using extra space 
*/
class Solution
{
    //Function to merge the arrays.
    public static void merge(long arr1[], long arr2[], int n, int m) 
    {
        // code here 
        int i=n-1;int j=0;
        while(i>=0 && j<m){
            if(arr1[i]>arr2[j]){
                arr1[i]=arr1[i]+arr2[j];
                arr2[j]=arr1[i]-arr2[j];
                arr1[i]=arr1[i]-arr2[j];
            }
            i--;
            j++;
        }
        Arrays.sort(arr1);
        Arrays.sort(arr2);
    }
}
