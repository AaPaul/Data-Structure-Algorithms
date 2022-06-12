class Solution {
public:
    vector<pair<int, int>> directions = {{0,1}, {0,-1}, {-1, 0}, {1, 0}};
    int dfs(vector<vector<char>>& g, int x, int y) {
        if( x < 0 || x >= g.size() || y < 0 || y >= g[0].size() || g[x][y] == '0') {
            return 0;
        }
        int area = 1;
        g[x][y] = '0';
        for (auto d: directions) {
            area += dfs(g, x + d.first, y + d.second);
        }
        return area;
    }

    int numIslands(vector<vector<char>>& grid) {
        vector<int> islands;
        for (int i = 0; i < grid.size(); ++i) {
            for (int j = 0; j < grid[0].size(); ++j) {
                if (grid[i][j] == '1') {
                    int t = dfs(grid, i, j);
                    islands.emplace_back(t);
                }
            }
        }
        return islands.size();
    }
};