// https://github.com/QSCTech-Sange/PAT-in-Python/blob/master/1067-Sort-with-Swap-0-i.md
#include <iostream>
using namespace std;
int main() {
    int num, temp, count = 0;
    scanf("%d",&num);
    int index[num];
    for(int i = 0; i < num; i++){
        scanf("%d",&temp);
        index[temp] = i;
    }
    for(int i = 1; i < num; i++) {
        if(i != index[i]) {
            while(index[0] != 0) {
                swap(index[0],index[index[0]]);
                count++;
            }
            if(i != index[i]) {
                swap(index[0],index[i]);
                count++;
            }
        }
    }
    printf("%d\n",count);
    return 0;
}