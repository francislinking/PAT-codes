#include <iostream>
#include <algorithm>
#include <vector>
using namespace std;

// define infinty
const int inf = 99999999;
struct station {
    double price, dis;
};
bool cmp1(station a, station b) {
    return a.dis < b.dis;
}
int main() {
    //get input
    double cmax, d, davg;
    int n;
    scanf("%lf%lf%lf%d", &cmax, &d, &davg, &n);
    
    //using strucure vector
    vector<station> sta(n + 1); //STL point
    sta[0] = {0.0, d};
    for(int i = 1; i <= n; i++)
        scanf("%lf%lf", &sta[i].price, &sta[i].dis);
    sort(sta.begin(), sta.end(), cmp1); //STL point
    
    //Initial, get start, leftdis=how far can go with gas left in tank
    double nowdis = 0.0, maxdis = 0.0, nowprice = 0.0, totalPrice = 0.0, leftdis = 0.0;
    if(sta[0].dis != 0) {
        printf("The maximum travel distance = 0.00"); // no station at begin, nowhere can go
        return 0;
    } else {
        nowprice = sta[0].price;
    }

    //enter loop
    while(nowdis < d) {
        maxdis = nowdis + cmax * davg;
        double minPriceDis = 0, minPrice = inf;
        int flag = 0;
        //search farther station in now max distance 
        for(int i = 1; i <= n && sta[i].dis <= maxdis; i++) {
            if(sta[i].dis <= nowdis) continue; // not farther, neglect, jump out
            //find lower price, add gas at this station, just enough reach goal station
            if(sta[i].price < nowprice) {
                totalPrice += (sta[i].dis - nowdis - leftdis) * nowprice / davg; 
                leftdis = 0.0;
                nowprice = sta[i].price;
                nowdis = sta[i].dis;
                flag = 1; //find
                break;
            }
            //update minPrice
            if(sta[i].price < minPrice) {
                minPrice = sta[i].price;
                minPriceDis = sta[i].dis;
            }
        }
        // not found, but exist farther station
        if(flag == 0 && minPrice != inf) {
            totalPrice += (nowprice * (cmax - leftdis / davg));
            leftdis = cmax * davg - (minPriceDis - nowdis);
            nowprice = minPrice;
            nowdis = minPriceDis;     
        }
        // not found, but no farther station
        if(flag == 0 && minPrice == inf) {
            nowdis += cmax * davg; //drive with full gas from this station
            printf("The maximum travel distance = %.2f", nowdis);
            return 0;
        }
    }
    printf("%.2f", totalPrice);
    return 0;
}