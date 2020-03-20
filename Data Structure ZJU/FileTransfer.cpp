#include<cstdio>

const int maxn = 10010;
typedef int ElementType;
typedef int setName;
typedef int setType[maxn];

void Initialization(setType s,int n);
int Find(setType s,ElementType x);
void Input_connection(setType s);
void Check_connection(setType s);
void Check_network(setType s,int n);

int main(){
    int n;
    char in;
    setType s;
    scanf("%d\n",&n);    
    Initialization(s,n);
    do{
        scanf("%c",&in);
        switch(in){
            case 'I':Input_connection(s);break;
            case 'C':Check_connection(s);break;
            case 'S':Check_network(s,n);break;
        }
    }while(in != 'S');
    return 0;
}

void Input_connection(setType s){
    ElementType u,v;
    scanf("%d%d",&u,&v);
    setName root1,root2;
    root1 = Find(s,u-1);
    root2 = Find(s,v-1);
    if(root1 != root2) s[root1] = root2;
}

void Initialization(setType s,int n){
    for(int i = 0; i < n; i++){
        s[i] = -1;
    }
}

void Check_connection(setType s){
    ElementType u,v;
    scanf("%d%d",&u,&v);
    setName root1 = Find(s,u-1);
    setName root2 = Find(s,v-1);
    if(root1 != root2) printf("no\n");
    else printf("yes\n");
}

void Check_network(setType s,int n){
    int cnt = 0;
    for(int i = 0; i < n; i++){
        if(s[i] < 0) cnt++;
    }
    if(cnt == 1) printf("The network is connected.\n");
    else printf("There are %d components.",cnt);
}

int Find(setType s,ElementType x){
    if(s[x] < 0) return x;
    else return s[x] = Find(s,s[x]);
}