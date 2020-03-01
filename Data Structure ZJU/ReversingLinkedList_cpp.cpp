#include <iostream>
#include <algorithm>
#define MAXSIZE 100000
using namespace std;

struct LNode
{
    int data;
    int next;
}node[MAXSIZE];

int List[MAXSIZE];

int main()
{
    int head_addr, n, k;
    cin >> head_addr >> n >> k;

    int addr, data, next;
    for(int i = 0; i < n; i++)
    {
        cin >> addr;
        cin >> data;
        cin >> next;
        node[addr].data = data;
        node[addr].next = next;
    }

    int count = 0;
    int p_next = head_addr;

    while(p_next!=-1)
    {
        List[count] = p_next;
        p_next = node[p_next].next;
        count = count + 1;
    }

    int first = 0;
    while (first + k <= count)
    {
        reverse(&List[first], &List[first + k]);
        first += k;
    }
    
    for(first = 0; first < count-1; first++)
        printf("%05d %d %05d\n", List[first], node[List[first]].data, List[first + 1]);
    printf("%05d %d -1\n", List[first], node[List[first]].data);
    return 0;
}