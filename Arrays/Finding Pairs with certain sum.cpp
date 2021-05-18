/*You are given two integer arrays nums1 and nums2. You are tasked to implement a data structure that supports queries of two types:

Add a positive integer to an element of a given index in the array nums2.
Count the number of pairs (i, j) such that nums1[i] + nums2[j] equals a given value (0 <= i < nums1.length and 0 <= j < nums2.length).*/

class FindSumPairs {
public:
    map<int,int> hm;
    vector<int> v1, v2;
    FindSumPairs(vector<int>& nums1, vector<int>& nums2) {
        
        v1 = nums1;
        v2 = nums2;
        for(int i = 0; i< v2.size(); i++){
            hm[v2[i]]++;
        }
    }
    
    void add(int index, int val) {
        hm[v2[index]]--;
        if(hm[v2[index]] == 0){
            hm.erase(v2[index]);
        }
        v2[index] += val;
        hm[v2[index]]++;
    }
    
    int count(int tot) {
        int counter = 0;
        for(int i = 0; i < v1.size(); i++){
            if(v1[i] <= tot){
                counter += hm[tot - v1[i]];
            }
        }
        return counter;
    }
};

/**
 * Your FindSumPairs object will be instantiated and called as such:
 * FindSumPairs* obj = new FindSumPairs(nums1, nums2);
 * obj->add(index,val);
 * int param_2 = obj->count(tot);
 */
