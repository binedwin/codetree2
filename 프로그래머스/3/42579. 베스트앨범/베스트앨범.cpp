#include <string>
#include <vector>
#include <unordered_map>
#include <algorithm>

using namespace std;

vector<int> solution(vector<string> genres, vector<int> plays) {

    unordered_map<string, int> total;
    unordered_map<string, vector<pair<int, int>>> songs;

    for (int i = 0; i < genres.size(); i++) {
        total[genres[i]] += plays[i];
        songs[genres[i]].push_back({plays[i], i});
    }

    vector<pair<int, string>> genreOrder;

    for (auto x : total) {
        genreOrder.push_back({x.second, x.first});
    }

    sort(genreOrder.begin(), genreOrder.end(),
        [](auto a, auto b) {
            return a.first > b.first;
        });

    vector<int> answer;

    for (auto genre : genreOrder) {

        string name = genre.second;

        sort(songs[name].begin(), songs[name].end(),
            [](auto a, auto b) {

                if (a.first == b.first)
                    return a.second < b.second;

                return a.first > b.first;
            });

        answer.push_back(songs[name][0].second);

        if (songs[name].size() >= 2) {
            answer.push_back(songs[name][1].second);
        }
    }

    return answer;
}