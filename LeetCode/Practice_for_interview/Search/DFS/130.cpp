class Solution {
    int m, n;
    vector<vector<int>> dirs = {{0, 1}, {0, -1}, {1, 0}, {-1, 0}};
public:
    void dfs(vector<vector<char>>& b, int x, int y) {
        if (x < 0 || x >= m || y < 0 || y >= n || b[x][y] != 'O') return;
        b[x][y] = 'T';
        
        for (auto d: dirs) {
            dfs(b, x+d[0], y+d[1]);
        }
    }
    void solve(vector<vector<char>>& board) {
        m = board.size();
        n = board[0].size();
        
        for (int i = 0; i < m; ++i) {
            dfs(board, i, 0);
            dfs(board, i, n-1);
        }
        for (int j = 0; j < n; ++j) {
            dfs(board, 0, j);
            dfs(board, m-1, j);
        }
        
        for (int i = 0; i < m; ++i) {
            for (int j = 0; j < n; ++j) {
                if (board[i][j] == 'T') board[i][j] = 'O';
                else if (board[i][j] == 'O') board[i][j] = 'X';
            }
        }
    }
};