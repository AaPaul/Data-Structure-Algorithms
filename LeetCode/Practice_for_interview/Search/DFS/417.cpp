class Solution {
    vector<vector<int>> dirs = {{0, 1}, {1, 0}, {-1, 0}, {0, -1}};
    int m, n;
    
public:
    void dfs(vector<vector<int>>& h, int x, int y, vector<vector<bool>>& canReach) {
        if (canReach[x][y]) return;
        
        canReach[x][y] = true;
        int curr = h[x][y];
        for (auto d: dirs) {
            int xi = x + d[0], yi = y + d[1];
            if (xi < 0 || xi >= m || yi < 0 || yi >= n || h[x][y] > h[xi][yi]) continue;
            dfs(h, xi, yi, canReach);

        }
    }
    vector<vector<int>> pacificAtlantic(vector<vector<int>>& heights) {
        m = heights.size();
        n = heights[0].size();
        vector<vector<int>> ret;
        vector<vector<bool>> canReachP(m, vector<bool>(n, false));
        vector<vector<bool>> canReachA(m, vector<bool>(n, false));

        for (int i = 0; i < m; ++i) {
            dfs(heights, i, 0, canReachA);
            dfs(heights, i, n-1, canReachP);
        }

        for (int j = 0; j < n; ++j) {
            dfs(heights, 0, j, canReachA);
            dfs(heights, m-1, j, canReachP);
        }

        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (canReachA[i][j] && canReachP[i][j]) {
                    vector<int> t;
                    t.emplace_back(i);
                    t.emplace_back(j);
                    ret.emplace_back(t);
                }
            }
        }
        return ret;
    }
};