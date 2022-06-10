class Solution {
public:
    vector<int> getSquares(int n) {
        vector<int> sqs;
        int diff = 3, square = 1;
        while (square <= n) {
            sqs.emplace_back(square);
            square += diff;
            diff += 2;
        }
        return sqs;
    }

    int numSquares(int n) {
        int level = 0;
        vector<int> squares = getSquares(n);
        queue<int> q;
        q.push(n);
        vector<int> visited(n+1);
        visited[n] = 1;
        while (!q.empty()) {
            int size = q.size();
            level++;
            while (size-- > 0) {
                int cur = q.front();
                q.pop();
                for (int s: squares) {
                    int nxt = cur - s;
                    if (nxt < 0) break;
                    if (nxt == 0) return level;
                    if (visited[nxt] == 1) continue;
                    visited[nxt] = 1;
                    q.push(nxt);
                }
            }
        }
        return n;
    }

};