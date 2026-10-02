#include <iostream>
using namespace std;

int gcd(int a, int b) {
    while (b != 0) {
        int temp = b;
        b = a % b;
        a = temp;
    }
    return a;
}

int main() {
    int A, B, T;
    cin >> A >> B >> T;

    if (T == 0) {
        cout << "YES";
    }
    else if (T <= max(A, B) && T % gcd(A, B) == 0) {
        cout << "YES";
    }
    else {
        cout << "NO";
    }

    return 0;
}

