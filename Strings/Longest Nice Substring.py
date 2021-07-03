'''
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.

Example:

Input: s = "YazaAay"
Output: "aAa"
Explanation: "aAa" is a nice string because 'A/a' is the only letter of the alphabet in s, and both 'A' and 'a' appear.
"aAa" is the longest nice substring.
'''

class Solution:
    def longestNiceSubstring(self, s: str) -> str:
        self.s = s
        
        def recur(s):
            if len(s) < 2: return ""
            lcase, ucase = [[] for _ in range(26)], [[] for _ in range(26)]
        
            # adding index of all elements of given s into either lcase or ucase accordingly
            for i in range(len(s)):
                # adding lower case letter to lcase 
                if (ord(s[i]) >= 97): lcase[ord(s[i])-97].append(i)
                # adding upper case letter to ucase
                else: ucase[ord(s[i])-65].append(i)
                
            # list of index of elements who appear in either of the lcase or ucase only.
            partition = [-1, len(s)]
        
            for j in range(26):
                if (len(lcase[j])*len(ucase[j]) == 0 and len(lcase[j]) + len(ucase[j]) != 0):
                    for x in ucase[j] + lcase[j]:
                        partition.append(x)   
                        # since x stores the index of elements not the elements
        
            # no such element with only lower or upper case 
            if len(partition) == 2:return s
        
            partition.sort()
        
            ans = ""
        
            # calling a recursion function to split the gievn string at partitions and call the complete process again
            for i in range(len(partition)-1):
                new_s = s[partition[i]+1: partition[i+1]]
                output = recur(new_s)
                if len(output) > len(ans):
                    ans = output
            return ans
        
        return recur(s)
