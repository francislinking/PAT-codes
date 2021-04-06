#include<bits/stdc++.h>
#define ll long long
using namespace std;

struct node{
    double x,y,dx,dy;
    int id;
}p[500];
double dp[400][400][15],X=0,Y=0;
bool cmp(node &a,node &b){
	return (a.x-X)*(b.y-Y)<(a.y-Y)*(b.x-X);
}
vector<int> ans,pth[305][305];
double getS(node a,node b,node c){
	double x1=b.x-a.x,y1=b.y-a.y,x2=b.x-c.x,y2=b.y-c.y;
	return abs(x1*y2-x2*y1)*0.5;
}
int main(){
    int n,m;
    cin>>n>>m;
    for(int i=0;i<n;i++){
        scanf("%lf %lf",&p[i].x,&p[i].y),p[i].id=i;
		X+=p[i].x; Y+=p[i].y;
    }//一定要选用中心点极角排序
	X/=n; Y/=n;//一开始我用第一个点作为基准点排序,错两个test
    sort(p,p+n,cmp);//极角排序
	double M=0; int I,J;
	for(int k=3;k<=m;k++){
		for(int i=0;i<n;i++){//起点
			for(int j=n-1;j>=i+k-1;j--){//结束点 //倒着遍历 方便pth加入路径,不然会被修改
				for(int l=j-1;l>=i+1;l--){//l->中间点
					double S = dp[i][l][k-1]+getS(p[i],p[l],p[j]);
					if(S > dp[i][j][k]){
						dp[i][j][k] = S;	
						pth[i][j] = pth[i][l];//获取路径
						pth[i][j].push_back(l);//加入点l
						if(dp[i][j][k]>M) M=dp[i][j][k],I=i,J=j;//最大值所在路径
					}
				}
			}
		}
	}
	ans.push_back(p[I].id); ans.push_back(p[J].id);
	for(int i=0;i<pth[I][J].size();i++)
		ans.push_back(p[pth[I][J][i]].id);
    sort(ans.begin(),ans.end());
    for(int i=ans.size()-1;i>=0;i--)
        printf("%d%c",ans[i],i==0?'\n':' ');
}