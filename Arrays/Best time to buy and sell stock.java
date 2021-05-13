/*You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.*/

class Solution {
    public int maxProfit(int[] prices) {
        int cp = prices[0];
        int max_profit = 0;
        int n = prices.length;
        
        for(int i = 1; i< n; i++){
            if(prices[i] < cp){
                cp = prices[i];
            }
            else if( prices[i] - cp > max_profit){
                max_profit = prices[i] - cp;
            }
        }
        if(max_profit > 0){
            return max_profit;
        }
        else{
            return 0;
        }
    }
}
