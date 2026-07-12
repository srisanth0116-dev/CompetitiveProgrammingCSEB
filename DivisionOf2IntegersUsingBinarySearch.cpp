#include <cmath>
#include <cstdio>
#include <vector>
#include <iostream>
#include <algorithm>
#include <iostream>
using namespace std;

int main() {

    int n, m;
    cin>>n>>m;

    int sign = 1;

    if ((n<0 && m>0) || (n>0 && m<0))
        sign = -1;

    if (n<0) n = -n;
    if (m<0) m = -m;

    int st = 0;
    int en = n;
    int ans = 0;

    while (st<=en) {

        int mid = st + (en - st) / 2;

        if (mid * m == n) {
            ans = mid;
            break;
        }

        if (mid * m < n) {
            ans = mid;
            st = mid + 1;
        }
        else {
            en = mid - 1;
        }
    }

    cout<<sign*ans;

    return 0;
}