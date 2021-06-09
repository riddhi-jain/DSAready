// Problem Statement :
// The count and say sequence -> 1,11,21,1211,111221,....
// We are to find the sequnce for the given Nth position
// Time Complexity : O(N*M) M being the longest sequence length

package CodeWithScaler.Week2;

public class CountAndSay {
        
    public static String countAndSay1(int A)
    {
        // First we must check the edge cases
        if(A<=0)
        {
            return null;
        }
        String result = "1"; // We know that result is 1 when greater than 0
        int i = 1;
        while(i<A) // As long as A is greater than 1
        {
        StringBuilder sb = new StringBuilder();
        int count = 1;
        for(int j = 1; j<result.length(); j++)
        {
            if(result.charAt(j)==result.charAt(j-1))
            {
                count++;
            }
            else 
            {
                sb.append(count); 
                sb.append(result.charAt(j-1));
                count = 1;
            }
        }
        // .toString() returns the value given to it in String format
        sb.append(count); // We append the count which is 1
        sb.append(result.charAt(result.length()-1)); // We append 1
        // Remember that the last number we append is always 1
        // Then we assign result as sb which is sb and return it as string
        result = sb.toString();
        i++; 
            
        }
        return result;
    }
    public static void main(String[] args) {
        int n = 3; // Output : 21
        System.out.println(countAndSay1(n));

    }
}




