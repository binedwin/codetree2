#include <string>
#include <vector>

using namespace std;

int visited[200] = {0};

void dfs(int n, vector<vector<int>>& computers, int lev) {

    visited[lev] = 1;

    for (int i = 0; i < n; i++) {

        if (computers[lev][i] == 1 && visited[i] == 0) {

            dfs(n, computers, i);
        }
    }
}

int solution(int n, vector<vector<int>> computers) {

    int answer = 0;

    for (int i = 0; i < n; i++) {

        if (visited[i] == 0) {

            dfs(n, computers, i);

            answer++;
        }
    }

    return answer;
}