/*There are 2 sorted arrays A and B of size n each. Write an algorithm to find the median of the array obtained after merging the above 2 arrays(i.e. array of length 2n). The complexity should be O(log(n)).
Approach :
1) Take the union of the input arrays ar1[] and ar2[].
2) Sort ar1[] and ar2[] respectively.
3) The median will be the last element of ar1[] + the first
   element of ar2[] divided by 2. */


import java.io.*;
import java.util.*;
class GFG
{
public static int getMedian(int ar1[],
							int ar2[], int n)
{
	int j = 0;
	int i = n - 1;
	while (ar1[i] > ar2[j] && j < n && i > -1)
	{
	int temp = ar1[i];
	ar1[i] = ar2[j];
	ar2[j] = temp;
	i--; j++;
	}
	Arrays.sort(ar1);
	Arrays.sort(ar2);
	return (ar1[n - 1] + ar2[0]) / 2;
}

// Driver code
public static void main (String[] args)
{
	int ar1[] = { 1, 12, 15, 26, 38 };
	int ar2[] = { 2, 13, 17, 30, 45 };

	int n1 = 5;
	int n2 = 5;
	if (n1 == n2)
	System.out.println("Median is "+ getMedian(ar1, ar2, n1));
	else
	System.out.println("Doesn't work for arrays of unequal size");
}
}
