/*
There is a room with n bulbs, numbered from 1 to n, arranged in a row from left to right. Initially, all the bulbs are turned off.

At moment k (for k from 0 to n - 1), we turn on the light[k] bulb. A bulb change color to blue only if it is on and all the previous bulbs (to the left) are turned on too.

Return the number of moments in which all turned on bulbs are blue.

Example:
Input: light = [3,2,4,1,5]
Output: 2
Explanation: All bulbs turned on, are blue at the moment 3, and 4 (index-0).
*/

#include <bits/stdc++.h>
using namespace std;
int main()
{
    int n; //number of bulbs in room
    cin >> n;

    int sum1 = 0;  // sum due to on-bulbs
    int sum2 = 0;  // sum of elements of sorted array (0,1,2...)
    int total = 0; // number of moments in which all turned on bulbs are blue
    int light[n];
    for (int j = 0; j < n; j++)
        cin >> light[j];
    for (int i = 0; i < n; i++)
    {
        sum1 += light[i] - 1;
        sum2 += i;
        if (sum1 == sum2)
            total++;
    }
    cout << total << endl;
}


