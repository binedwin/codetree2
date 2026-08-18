#include <vector>

using namespace std;

int cnt = 0;

void dfs(int lev, int sum, const vector<int>& numbers, int target) {

    if (lev == numbers.size()) {
        if (sum == target) {
            cnt++;
        }
        return;
    }

    dfs(lev + 1, sum + numbers[lev], numbers, target);
    dfs(lev + 1, sum - numbers[lev], numbers, target);
}

int solution(vector<int> numbers, int target) {
    cnt = 0;

    dfs(0, 0, numbers, target);

    return cnt;
}