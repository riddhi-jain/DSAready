/*Given an array of N integers, and an integer K, find the number of pairs of elements in the array whose sum is equal to K.*/

import java.io.*;
import java.util.*;
public class GFG {

    public static void main(String[] args) throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int tc = Integer.parseInt(br.readLine().trim());
        while (tc-- > 0) {
            String[] inputLine;
            inputLine = br.readLine().trim().split(" ");
            int n = Integer.parseInt(inputLine[0]);
            int k = Integer.parseInt(inputLine[1]);
            int[] arr = new int[n];
            inputLine = br.readLine().trim().split(" ");
            for (int i = 0; i < n; i++) {
                arr[i] = Integer.parseInt(inputLine[i]);
            }
            int ans = new Solution().getPairsCount(arr, n, k);
            System.out.println(ans);
        }
    }
}
class Solution {
    int getPairsCount(int[] arr, int n, int k) {
        // code here
        HashMap<Integer, Integer> hash_map = new HashMap<>();
        for(int i = 0; i< n; i++){
            if(!hash_map.containsKey(arr[i])){
                hash_map.put(arr[i], 0);
            }
            hash_map.put(arr[i], hash_map.get(arr[i]) + 1 );
        }
        int count = 0;
        for(int i = 0; i< n; i++){
            if(hash_map.get(k - arr[i]) != null){
                count+= hash_map.get(k - arr[i] );
            }
            if(k - arr[i] == arr[i] ){
                count--;
            }
        }
        int answer = count/2;
        return answer;
    }
}
