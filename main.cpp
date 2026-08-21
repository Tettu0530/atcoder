#include <bits/stdc++.h>   // 競プロ用: 主要な標準ライブラリを一括インクルード
using namespace std;       // std:: の省略記法（競プロでは一般的）

int main() {
    // 入出力の高速化（標準入出力の同期を切る / 標準入力の同期を切る）
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

    // 要素の個数 N を読み取る
    int n;
    cin >> n;

    // 長さ n の配列 a を用意し、各要素を入力から読み込む（long long で 64bit 整数）
    vector<long long> a(n);
    for (auto &x : a) cin >> x;   // 各要素を a に格納

    // 全要素の合計を計算
    long long sum = 0;
    for (auto x : a) sum += x;

    // 結果を出力（n・合計・最大値）
    cout << "n = " << n << "\n";
    cout << "sum = " << sum << "\n";
    cout << "max = " << *max_element(a.begin(), a.end()) << "\n";  // <algorithm> の max_element で最大値を取得

    return 0;   // 正常終了
}
