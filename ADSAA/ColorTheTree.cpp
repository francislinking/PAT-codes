#include <bits/stdc++.h>
using namespace std;
typedef long long ll;
const int maxn=111;
struct node
{
    int l,r,tol;
}stu[maxn];
int n,a[maxn],root,tot;
void handle(int l,int r,int pre)
{
    if(l==r) return ;
    int pos=r;
    for(int i=r-1;i>=l;--i) if(a[i]>a[r]) pos=i;
    if(pos==r){
        int cnt=++tot;
        stu[cnt].l=0;
        stu[cnt].r=0;
        handle(l,pos-1,cnt);
        stu[pre].l=cnt;
    }
    else if(pos==l){
        int cnt=++tot;
        stu[cnt].l=0;
        stu[cnt].r=0;
        handle(pos,r-1,cnt);
        stu[pre].r=cnt;
    }
    else{
        int cnt=++tot;
        stu[cnt].l=0;
        stu[cnt].r=0;
        handle(l,pos-1,cnt);
        stu[pre].l=cnt;
        cnt=++tot;
        stu[cnt].l=0;
        stu[cnt].r=0;
        handle(pos,r-1,cnt);
        stu[pre].r=cnt;
    }
}
vector<int> solve(vector<int> p,vector<int> q)
{
    vector<int> res;
    res.clear();
    for(int i=0;i<(int)p.size();++i){
        int u=p[i];
        for(int j=0;j<(int)q.size();++j){
            if(u==q[j]){
                res.push_back(u);
                break;
            }
        }
    }
    return res;
}
int tol;
vector<int> red[maxn],black[maxn];
bool flag;
void dfs(int cur)
{
    if(flag==false) return ;
    if(stu[cur].l>0 && stu[cur].r>0){
        dfs(stu[cur].l);
        if(flag==false) return ;
        dfs(stu[cur].r);
        if(flag==false) return ;
        vector<int> x=solve(black[stu[stu[cur].l].tol],black[stu[stu[cur].r].tol]);
        int cnt=++tol;
        stu[cur].tol=cnt;
        red[cnt]=x;
        black[cnt].clear();
        vector<int> y=solve(black[stu[stu[cur].l].tol],red[stu[stu[cur].r].tol]);
        vector<int> z=solve(red[stu[stu[cur].l].tol],black[stu[stu[cur].r].tol]);
        vector<int> w=solve(red[stu[stu[cur].l].tol],red[stu[stu[cur].r].tol]);
        set<int> se;
        se.clear();
        for(int i=0;i<(int)x.size();++i) se.insert(x[i]);
        for(int i=0;i<(int)y.size();++i) se.insert(y[i]);
        for(int i=0;i<(int)z.size();++i) se.insert(z[i]);
        for(int i=0;i<(int)w.size();++i) se.insert(w[i]);
        set<int>::iterator it;
        for(it=se.begin();it!=se.end();++it){
            black[cnt].push_back((*it)+1);
        }
        if((int)red[cnt].size()==0 && (int)black[cnt].size()==0){
            flag=false;
            return ;
        }
    }
    else if(stu[cur].l>0){
        dfs(stu[cur].l);
        if(flag==false) return ;
        int id=stu[stu[cur].l].tol;
        bool have0=false;
        for(int i=0;i<(int)red[id].size();++i){
            if(red[id][i]==0){
                have0=true;
                break;
            }
        }
        if(have0==false){
            flag=false;
            return ;
        }
        int cnt=++tol;
        stu[cur].tol=cnt;
        red[cnt].clear();
        black[cnt].clear();
        black[cnt].push_back(1);
    }
    else if(stu[cur].r>0){
        dfs(stu[cur].r);
        if(flag==false) return ;
        int id=stu[stu[cur].r].tol;
        bool have0=false;
        for(int i=0;i<(int)red[id].size();++i){
            if(red[id][i]==0){
                have0=true;
                break;
            }
        }
        if(have0==false){
            flag=false;
            return ;
        }
        int cnt=++tol;
        stu[cur].tol=cnt;
        red[cnt].clear();
        black[cnt].clear();
        black[cnt].push_back(1);
    }
    else{
        int cnt=++tol;
        stu[cur].tol=cnt;
        red[cnt].clear();
        red[cnt].push_back(0);
        black[cnt].clear();
        black[cnt].push_back(1);
    }
}
int main()
{
    int t;
    for(scanf("%d",&t);t;--t){
        scanf("%d",&n);
        for(int i=1;i<=n;++i){
            scanf("%d",&a[i]);
        }
        tot=0;
        root=++tot;
        stu[root].l=0;
        stu[root].r=0;
        handle(1,n,1);
        flag=true;
        tol=0;
        dfs(root);
        if(flag) printf("Yes\n");
        else printf("No\n");
    }
    return 0;
}