/*Given a square matrix, turn it by 90 degrees in a clockwise direction without using any extra space.

Approach:
In any row, for every decreasing row index i, there exists a constant column index j, such that j = current_row_index. 

This pattern can be printed using 2 nested loops.
(This pattern of writing indices is achieved by writing the exact indices of the desired elements of 
where they actually existed in the original array.)  */


import java.io.*;

class GFG {
	static int N = 4;

	// Function to rotate the matrix 90 degree clockwise
	static void rotate90Clockwise(int arr[][])
	{
		// printing the matrix on the basis of
		// observations made on indices.
		for (int j = 0; j < N; j++)
		{
			for (int i = N - 1; i >= 0; i--)
				System.out.print(arr[i][j] + " ");
			System.out.println();
		}
	}
	public static void main(String[] args)
	{
		int arr[][] = { { 1, 2, 3, 4 },
						{ 5, 6, 7, 8 },
						{ 9, 10, 11, 12 },
						{ 13, 14, 15, 16 } };
		rotate90Clockwise(arr);
	}
}
