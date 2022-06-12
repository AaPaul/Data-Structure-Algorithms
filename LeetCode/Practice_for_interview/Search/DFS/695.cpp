class Solution {
public:
    vector<pair<int, int>> dir = {{0,1}, {0,-1}, {1,0}, {-1, 0}};
    int dfs(vector<vector<int>> &g, int x, int y) {
        if (x < 0 || x >= g.size() || y < 0 || y >= g[0].size() ||g[x][y] == 0) return 0;
        int ans = 1;
        g[x][y] = 0;
        for (auto d: dir) {
            ans += dfs(g, x+d.first, y+d.second);    
        }
        return ans;


    }
    int maxAreaOfIsland(vector<vector<int>>& grid) {
        int ans = 0;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                int t = dfs(grid, i, j);
                ans = max(ans, t);
            }
        }
        return ans;
    }
};