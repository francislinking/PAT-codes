#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

struct User {
    int id;
    int total_score;
    int num_full;

    bool operator<(const User &b) {
        if (total_score != b.total_score)
            return b.total_score < total_score;
        if (num_full != b.num_full)
            return b.num_full < num_full;
        return id < b.id;
    }
};


int main() {
    int num_users, num_pro, num_sub;
    scanf("%d%d%d", &num_users, &num_pro, &num_sub);
    // 题目的满分
    int full[num_pro];
    for (int i = 0; i < num_pro; i++)
        scanf("%d", &full[i]);
	// 该不该打印
    bool should_print[num_users + 1];
    for (int i = 0;i<=num_users;i++)
        should_print[i]= false;
	// 每个人每道题的分
    int scores[num_users + 1][num_pro];
    for (int i = 0; i <= num_users; i++) {
        for (int j = 0; j < num_pro; j++)
            scores[i][j] = -2;
    }
    // 读取数据，并更新最高分，更新该不该打印
    for (int i = 0; i < num_sub; i++) {
        int id, pro, score;
        scanf("%d%d%d", &id, &pro, &score);
        if (score != -1)
            should_print[id] = true;
        scores[id][pro - 1] = max(scores[id][pro - 1], score);
    }
    // 统计总分和满分题目数量，并添加到vector中
    vector<User> users;
    for (int i = 1; i <= num_users; i++) {
        int temp_full, temp_total;
        temp_full = 0;
        temp_total = 0;
        for (int j = 0; j < num_pro; j++) {
            if (scores[i][j] > 0) {
                temp_total += scores[i][j];
                if (full[j] == scores[i][j])
                    temp_full += 1;
            }
        }
        users.emplace_back(User{i, temp_total, temp_full});
    }
    // 排序
    sort(users.begin(), users.end());
	// 输出
    int rank = 0;
    for (int i = 0; i < num_users; i++) {
        if (!should_print[users[i].id])
            break;
        if (rank == 0 or users[i].total_score != users[i - 1].total_score)
            rank = i + 1;
        printf("%d %05d %d", rank, users[i].id, users[i].total_score);
        for (int j = 0; j < num_pro; j++) {
            if (scores[users[i].id][j] == -2)
                printf(" -");
            else if (scores[users[i].id][j] == -1)
                printf(" 0");
            else
                printf(" %d", scores[users[i].id][j]);
        }
        printf("\n");
    }
}