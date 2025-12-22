def solution(k, dungeons):
    visited = [False] * len(dungeons)
    answer = 0

    def dfs(current_fatigue, count):
        nonlocal answer
        answer = max(answer, count)

        for i in range(len(dungeons)):
            min_need, cost = dungeons[i]
            if not visited[i] and current_fatigue >= min_need:
                visited[i] = True
                dfs(current_fatigue - cost, count + 1)
                visited[i] = False  # 백트래킹

    dfs(k, 0)
    return answer