//https://github.com/QSCTech-Sange/PAT-in-Python/blob/master/1076-Forwards-on-Weibo.md
#include <iostream>
#include <vector>
#include <queue>

using namespace std;

int main() {
    // 数据读入
    int num_users, max_level;
    scanf("%d%d", &num_users, &max_level);
    vector<int> fans[num_users + 1];
    for (int i = 1; i <= num_users; i++) {
        int num_friends;
        scanf("%d", &num_friends);
        for (int j = 0; j < num_friends; j++) {
            int friend_temp;
            scanf("%d", &friend_temp);
            fans[friend_temp].push_back(i);
        }
    }
    // 对每个输入进行BFS
    int num_que;
    scanf("%d", &num_que);
    for (int i = 0; i < num_que; i++) {
        int id;
        scanf("%d", &id);
        bool visited[num_users + 1];
        for (int j = 0; j <= num_users; j++)
            visited[j] = false;
        visited[id] = true;
        int count = 0;
        int level = 1;
        queue<int> que;
        que.push(id);
        while (!que.empty() and level <= max_level) {
            int length = que.size();
            for (int j = 0; j < length; j++) {
                int star = que.front();
                que.pop();
                for (auto &fan:fans[star]) {
                    if (!visited[fan]) {
                        visited[fan] = true;
                        que.push(fan);
                        count += 1;
                    }
                }
            }
            level += 1;
        }
        printf("%d\n", count);
    }
}