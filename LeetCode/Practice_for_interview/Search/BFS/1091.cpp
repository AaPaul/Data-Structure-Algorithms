class Solution {
public:
    int shortestPathBinaryMatrix(vector<vector<int>>& grid) {
        if (grid.empty() || grid.size() == 0 || grid[0].size() == 0) {
            return -1;
        }
        int n = grid.size();
        vector<pair<int,int>> directions = {{0,1}, {0, -1}, {1, 0}, {1, -1}, {1, 1}, {-1, 0}, {-1, 1}, {-1, -1}};
        queue<pair<int, int>> mq;
        mq.push({0, 0});
        int ans = 0;
        while (!mq.empty()) {
            int size = mq.size();
            // update the length of path here, so that there would be no effect if we iterate the next items in the queue.
            ans++;
            while (size-- > 0) {
                pair<int, int> curr = mq.front();
                mq.pop();
                int x = curr.first, y = curr.second;
                if (grid[x][y] == 1) {
                    continue;
                }
                if (x == n-1 && y == n-1) {
                    return ans;
                }
                grid[x][y] = 1;
                for (auto d: directions){
                    int nx = x + d.first;
                    int ny = y + d.second;
                    if (nx < 0 || nx >= n || ny < 0 || ny >= n) {
                        continue;
                    }
                    mq.push({nx, ny});
                }
            }
        }
        return -1;
    }
};