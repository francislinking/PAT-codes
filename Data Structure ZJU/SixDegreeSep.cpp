'''
https://zyxhangzhou.github.io/2017/10/30/PTA-Six-Degrees-of-Separation/
'''
#include <cstdio>
#include <cstring>
#include <vector>
#include <queue>
#define MAXV 10005
//int g[MAXV][MAXV] = { 0 };
std::vector<int> v[MAXV];
int inq[MAXV] = { 0 };
int count;
int BFS(int x) {
	int last = x, tail, level = 0;;
	std::queue<int> q;
	inq[x] = 1;
	q.push(x); count = 1;
	while (!q.empty()) {
		int now = q.front();
		q.pop();
		for (auto i=v[now].begin(); i != v[now].end(); ++i) {
			if (!inq[*i]) {
				q.push(*i);
				count++;
				inq[*i] = 1;
				tail = *i;
			}
		}
		if(now == last) {
			level++;
			last = tail;
		}
		if(level==6) break;
	}
	return count;
}
int main() {
	//freopen("text.txt", "r", stdin);
	int n, m;
	scanf("%d %d", &n, &m);
	for (int i = 0; i<m; ++i) {
		int tx, ty;
		scanf("%d %d", &tx, &ty);
		v[tx].push_back(ty);
		v[ty].push_back(tx);
	}
	for(int i=1; i<=n; ++i) {
		double tmp = BFS(i)*100.0/n;
		printf("%d: %.2f%\n", i, tmp);
		if(1!=n) memset(inq, 0, sizeof(inq));
	}
	return 0;
}