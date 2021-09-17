/*
Given a Directed Graph with V vertices (Numbered from 0 to V-1) and E edges, check whether it contains any cycle or not.

Example:
1 -> 2 -> 3
^         |
|         |
0<--------|

Output: 1
Explanation: 3 -> 0 is a cycle

Algorithm: 
- Create the graph using the given number of edges and vertices.
- Create a recursive function that initializes the current index or vertex, visited, and recursion stack.
- Mark the current node as visited and also mark the index in recursion stack.
- Find all the vertices which are not visited and are adjacent to the current node. Recursively call the function for those vertices, If the recursive function returns true, return true.
- If the adjacent vertices are already marked in the recursion stack then return true.
- Create a wrapper class, that calls the recursive function for all the vertices and if any function returns true return true. Else if for all vertices the function returns false return false.
*/

// { Driver Code Starts
#include <bits/stdc++.h>
using namespace std;

 // } Driver Code Ends

class Solution {
    public:
    bool check(vector<int> &vis, vector<int> &curr_flow, vector<int> adj[], int node){
        vis[node] = 1;
        curr_flow[node] = 1;
        for(auto it:adj[node]){
            if(!vis[it]){
                if(check(vis, curr_flow, adj, it)){
                    return true;
                }
            }
            else if (curr_flow[it]){
                return true;
            }
        }
        curr_flow[node] = 0;
        return false;
    }
    
    public:
    // Function to detect cycle in a directed graph.
    bool isCyclic(int V, vector<int> adj[]) {
        // code here
        vector<int> vis(V+1, 0);
        vector<int> curr_flow(V+1, 0);
        for(int i = 0; i < V; i++){
            if(!vis[i]){
                if(check(vis, curr_flow, adj, i)){
                    return true;
                }
            }
        }
        return false;
    }
};

// { Driver Code Starts.

int main() {

    int t;
    cin >> t;
    while (t--) {
        int V, E;
        cin >> V >> E;

        vector<int> adj[V];

        for (int i = 0; i < E; i++) {
            int u, v;
            cin >> u >> v;
            adj[u].push_back(v);
        }

        Solution obj;
        cout << obj.isCyclic(V, adj) << "\n";
    }

    return 0;
}
  // } Driver Code Ends
