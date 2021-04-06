// https://blog.nowcoder.net/n/b75730750cc24778bd2ee666f74b0e78
#include<iostream>
#include<cstdio>
#include<string>

template<typename T>
class BPlusTree
{
private:
enum { RANK = 3, MINSIZE = ((RANK + 1) >> 1) };
typedef enum { leaf, nonleaf }type;

class treeNode {
public:
treeNode* parent;
int size;
virtual type getType()const = 0; //得到类型:叶结点、内部结点
virtual T getKey(int i)const = 0; //得到下标为i的key
virtual void setKey(T x, int i) = 0; //设置下标为i的key值
virtual void setChild(treeNode* t, int i) { }
virtual void setBlock(int num, int i) { }
virtual void setNext(treeNode* t) { }
virtual treeNode* getChild(int i)const { return nullptr; }
virtual treeNode* getNext()const { return nullptr; }
virtual int getBlock(int i)const { return 0; }
};

class internalNode :public treeNode {
public:
T key[RANK - 1];
treeNode* child[RANK];

virtual type getType()const { return nonleaf; }
virtual T getKey(int i)const { return key[i]; }
virtual void setKey(T x, int i) { key[i] = x; }
virtual void setChild(treeNode* t, int i) { child[i] = t; }
virtual treeNode* getChild(int i)const { return child[i]; }
internalNode(int size = 1) {
this->size = size;
for (int i = 0; i < RANK; i++)child[i] = nullptr;
}
virtual ~internalNode() { };
};

class leafNode :public treeNode {
public:
T key[RANK];
leafNode* next;
int blockNum[RANK];

virtual type getType()const { return leaf; }
virtual T getKey(int i)const { return key[i]; }
virtual void setKey(T x, int i) { key[i] = x; }
virtual void setBlock(int num, int i) { blockNum[i] = num; }
virtual int getBlock(int i)const { return blockNum[i]; }
virtual void setNext(treeNode* t) { next = dynamic_cast<leafNode*>(t); }
virtual treeNode* getNext()const { return next; }
leafNode(int size = 1) { this->size = size; next = nullptr; }
virtual ~leafNode() { };
};

treeNode* root;

void insertIntoLeaf(treeNode* p, int i, T x, int y) {
while (i >= 1 && x <= p->getKey(i - 1)) {
p->setKey(p->getKey(i - 1), i);
p->setBlock(p->getBlock(i - 1), i);
i--;
}
//找到插入的位置
p->setKey(x, i);
p->setBlock(y, i);
p->size++;
return;
}

T findKey(treeNode* t) {
while (t->getType() == nonleaf) {

t = t->getChild(0);
}
return t->getKey(0);
}

treeNode* findLeafNode(T x) {  //找到x所在的叶结点
treeNode *p = root;
while (p->getType() == nonleaf) {
//在已知p为内部结点时，向下造型为内部结点
internalNode* t = dynamic_cast<internalNode*>(p);
if (x < t->getKey(0)) {
p = t->getChild(0);
}
else {
for (int i = 0; i < t->size - 1; i++) {
if (x > t->getKey(i) && x < t->getKey(i + 1)) {
p = t->child[i + 1];
break;
}
else if (x == t->getKey(i)) {

return nullptr;
}
}
if (x > t->getKey(t->size - 1)) {
p = t->child[t->size];
}
else if (x == t->getKey(t->size - 1)) {

return nullptr;
}
}
}
return p;
}
treeNode* queue[10000];
int front, rear;
void enqueue(treeNode* t)
{
front = (front + 1) % 10000;
queue[front] = t;
}

treeNode* dequeue()
{
rear = (rear + 1) % 10000;
return queue[rear];
}

public:

BPlusTree() { root = nullptr; front = rear = 0; }
void insert(T x, int y) {
if (!root) {
root = new leafNode(1);
root->setKey(x, 0);
root->setBlock(y, 0);
root->setNext(nullptr);
root->parent = nullptr;
return;
}
//找到叶结点
leafNode* p = dynamic_cast<leafNode*>(findLeafNode(x));
if (!p) { printf("Key %d is duplicated\n", x); return; }
for (int j = 0; j < p->size; j++) {
if (x == p->getKey(j)) {
printf("Key %d is duplicated\n",x);
return;
}
}
//叶结点非满，直接插入
if (p->size != RANK) {
insertIntoLeaf(p, p->size, x, y);
}
//叶结点满
else {
//分裂叶结点

//将p分裂
leafNode* newNode = new leafNode();

struct childNode {
T k;
int num;
}a[RANK + 1];

//将所有数据预存在结构数组a中
for (int i = 0; i < RANK; i++) {
a[i].k = p->getKey(i);
a[i].num = p->getBlock(i);
}

int j = RANK - 1;

//将新的数据插入数组a
for (; x < a[j].k && j >= 0; j--) {
a[j + 1] = a[j];
}
a[j + 1].k = x;
a[j + 1].num = y;

//将数组a的数据复制到node1和node2中
for (int i = 0; i < MINSIZE; i++) {
p->setKey(a[i].k, i);
p->setBlock(a[i].num, i);
}
p->size = MINSIZE;
int cnt = 0;
for (int i = MINSIZE; i < RANK + 1; i++) {
newNode->setKey(a[i].k, cnt);
newNode->setBlock(a[i].num, cnt++);
}
newNode->size = RANK - MINSIZE + 1;
newNode->next = p->next;
p->next = newNode;
internalNode* parent = nullptr;
internalNode* newNode2 = nullptr;
treeNode* node[RANK + 1];
treeNode* t = p;
while (t != nullptr) {
parent = dynamic_cast<internalNode*>(t->parent);
if (!newNode2) {
if (parent) {
leafNode* tmp = dynamic_cast<leafNode*>(parent->getChild(0));
for (int i = 0; i<parent->size + 2; i++) {
node[i] = tmp;
tmp = tmp->next;
}
}
else {
node[0] = t;
node[1] = newNode;
}
}
else {
if (parent) {
int count = 0;//2
bool flag = false;
internalNode* tmp;
for (int i = 0; i <parent->size + 2; i++) {
if (count<parent->size + 1)tmp = dynamic_cast<internalNode*>(parent->child[count]);
if (!flag && (newNode2->key[0] < tmp->key[0] || i == parent->size + 1)) {
node[i] = newNode2;
flag = true;
}
else {
node[i] = parent->child[count++];
}
}
}
else {
node[0] = t;
node[1] = newNode2;
}
}

//case 1: 当前结点是根节点，根节点长高
if (!parent) {

internalNode* r = new internalNode(1);
for (int i = 0; i < 2; i++) {
r->child[i] = node[i];
r->child[i]->parent = r;
}

r->key[0] = findKey(r->child[1]);
root = r;
break;
}

//case 2 :当前结点的父节点不满
else if (parent->size < RANK - 1) {
for (int i = 0; i < parent->size + 2; i++) {
parent->child[i] = node[i];
parent->child[i]->parent = parent;
}
for (int i = 0; i < parent->size + 1; i++) {
parent->key[i] = findKey(parent->child[i + 1]);
}
parent->size++;
break;
}

//case 3 :当前父节点已满，分裂父节点
else if (parent->size == RANK - 1) {
newNode2 = new internalNode(MINSIZE - 1);
for (int i = 0; i < MINSIZE; i++) {
parent->child[i] = node[i];
parent->child[i]->parent = parent;
}
for (int i = 0; i < MINSIZE - 1; i++) {
parent->key[i] = findKey(parent->child[i + 1]);
}
parent->size = MINSIZE - 1;
int count = 0;
for (int i = MINSIZE; i < RANK + 1; i++) {
newNode2->child[count] = node[i];
newNode2->child[count++]->parent = newNode2;
}
count = 0;
for (int i = MINSIZE; i < RANK; i++) {
newNode2->key[count] = findKey(newNode2->child[count + 1]);
count++;
}
t = parent;
}
}
}
return;
}

void print()
{
if (!root)return;
treeNode* tmp;
enqueue(root);

int cur = 1;
int curnum = 1;
int nextnum = 0;
while (front != rear) {
tmp = dequeue();
if (tmp->getType() == nonleaf) {
curnum--;
printf("[");
for (int i = 0; i < tmp->size - 1; i++) {
std::cout << tmp->getKey(i) << ",";
}
std::cout << tmp->getKey(tmp->size - 1);
printf("]");
for (int i = 0; i < tmp->size + 1; i++) {
if (tmp->getChild(i)) {
enqueue(tmp->getChild(i));
nextnum++;
}
}
if (curnum == 0) {
printf("\n");
cur++;
curnum = nextnum;
nextnum = 0;
}

}
else {
printf("[");
for (int i = 0; i < tmp->size - 1; i++) {
std::cout << tmp->getKey(i) << ",";
}
std::cout << tmp->getKey(tmp->size - 1);
printf("]");
}
}
std::cout << std::endl;
}
};

int main()
{
BPlusTree<int> *p = new BPlusTree<int>;
int n;
scanf("%d", &n);
for (int i = 0; i <n; i++) {
int x;
scanf("%d", &x);
p->insert(x, 2);
}
p->print();
system("pause");
return 0;
}