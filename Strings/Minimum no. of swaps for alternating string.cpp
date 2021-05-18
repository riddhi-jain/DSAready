/*Given a binary string s, return the minimum number of character swaps to make it alternating, or -1 if it is impossible.
The string is called alternating if no two adjacent characters are equal. For example, the strings "010" and "1010" are alternating, while the string "0100" is not.
Any two characters may be swapped, even if they are not adjacent.

APPROACH:

The only possible resulting strings are '01010.....' and '10101....'
Creating both possible strings of length of given string.
If no. of 0 > no. of 1 in given string : resulting string is '0101....'
If no. of 1 > no. of 0 in given string : resulting string is '1010....'
If If no. of 1 > no. of 0 in given string : resulting string is '1010....'
If no. of 1 = no. of 0 in given string : resulting string could be either
Compare the given string and consequent resulting string to count no. of mismatches.
no. of swaps is half the no. of mismatches.*/


class Solution {
public:
    int minSwaps(string s) {
        int one = 0; //one count
        int zero = 0; //zero count
        int n = s.length();
        // counting number of zeros and ones in s
        for(int i = 0; i < n; i++){
            if(s[i] == '0')
                zero++;
            else
                one++;
        }
        // impossible event
        if (abs(zero - one) > 1)
            return -1;
        // creating types of output string
        string s1 ="", s2 = "";
        for(int i = 0; i< n; i++)
            if(i%2 == 0){
                s1+='0';
                s2+='1';
            }
            else{
                s1+='1';
                s2+='0';
            }
        // variables to track no. of swaps
        int c1=0,c2=0;
        if(zero == one){
            for(int i=0; i<n; i++){
                if(s[i]!=s1[i]) c1++;
                if(s[i]!=s2[i]) c2++;
            }
            return min(c1/2, c2/2);
        }
        if(one > zero) s1=s2;
        for(int i=0; i<n; i++)
            if(s[i]!=s1[i]) c1++;
        return c1/2;
    }
};
