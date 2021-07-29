'''
An array nums of length n is beautiful if:

nums is a permutation of the integers in the range [1, n].
For every 0 <= i < j < n, there is no index k with i < k < j where 2 * nums[k] == nums[i] + nums[j].
Given the integer n, return any beautiful array nums of length n. There will be at least one valid answer for the given n.

Example :

Input: n = 4
Output: [2,1,4,3]

Beautiful Array Properties
Saying that an array is beautiful,
there is no i < k < j,
such that A[k] * 2 = A[i] + A[j]

Apply these 3 following changes a beautiful array,
we can get a new beautiful array


1. Deletion
Easy to prove.

2. Addition
If we have A[k] * 2 != A[i] + A[j],
(A[k] + x) * 2 = A[k] * 2 + 2x != A[i] + A[j] + 2x = (A[i] + x) + (A[j] + x)

E.g: [1,3,2] + 1 = [2,4,3].

3. Multiplication
If we have A[k] * 2 != A[i] + A[j],
for any x != 0,
(A[k] * x) * 2 = A[k] * 2 * x != (A[i] + A[j]) * x = (A[i] * x) + (A[j] * x)

E.g: [1,3,2] * 2 = [2,6,4]


Explanation
With the observations above, we can easily construct any beautiful array.
Assume we have a beautiful array A with length N

A1 = A * 2 - 1 is beautiful with only odds from 1 to N * 2 -1
A2 = A * 2 is beautiful with only even from 2 to N * 2
B = A1 + A2 beautiful array with length N * 2

E.g:

A = [2, 1, 4, 5, 3]
A1 = [3, 1, 7, 9, 5]
A2 = [4, 2, 8, 10, 6]
B = A1 + A2 = [3, 1, 7, 9, 5, 4, 2, 8, 10, 6]

'''

    public int[] beautifulArray(int N) {
        ArrayList<Integer> res = new ArrayList<>();
        res.add(1);
        while (res.size() < N) {
            ArrayList<Integer> tmp = new ArrayList<>();
            for (int i : res) if (i * 2 - 1 <= N) tmp.add(i * 2 - 1);
            for (int i : res) if (i * 2 <= N) tmp.add(i * 2);
            res = tmp;
        }
        return res.stream().mapToInt(i -> i).toArray();
    }
