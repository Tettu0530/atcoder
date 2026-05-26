#include <bits/stdc++.h>
using namespace std;

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    int n;
    cin >> n;

    vector<long long> a(n);
    for (auto &x : a) cin >> x;

    long long sum = 0;
    for (auto x : a) sum += x;

    cout << "n = " << n << "\n";
    cout << "sum = " << sum << "\n";
    cout << "max = " << *max_element(a.begin(), a.end()) << "\n";

    return 0;
}
