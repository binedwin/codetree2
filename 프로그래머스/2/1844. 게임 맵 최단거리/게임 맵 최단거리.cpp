#include <vector>
#include <queue>

using namespace std;

struct Edge {
    int y;
    int x;
    int dist;
};

int dy[4] = {-1, 1, 0, 0};
int dx[4] = {0, 0, -1, 1};

int bfs(vector<vector<int>> maps, int sy, int sx) {

    int n = maps.size();
    int m = maps[0].size();

    queue<Edge> q;
    q.push({sy, sx, 1});

    maps[sy][sx] = 0;  // 방문 처리

    while (!q.empty()) {

        Edge now = q.front();
        q.pop();

        // 목적지 도착
        if (now.y == n - 1 && now.x == m - 1) {
            return now.dist;
        }

        for (int i = 0; i < 4; i++) {

            int ny = now.y + dy[i];
            int nx = now.x + dx[i];

            // 맵 밖
            if (ny < 0 || nx < 0 || ny >= n || nx >= m)
                continue;

            // 벽이거나 이미 방문
            if (maps[ny][nx] == 0)
                continue;

            maps[ny][nx] = 0;

            q.push({
                ny,
                nx,
                now.dist + 1
            });
        }
    }

    return -1;
}

int solution(vector<vector<int>> maps)
{
    int sy = 0;
    int sx = 0;

    int answer = bfs(maps, sy, sx);

    return answer;
}