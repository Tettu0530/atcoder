"""
競プロ Python テンプレート（高速入出力）

使い方:
- 1行ずつ読むなら input() を使う（readline 版なので高速）
- 大量データ・グリッドなどはまとめ読み版が速いことも
- 出力は out に溜めて最後に1回だけ flush する
"""
import sys

input = sys.stdin.readline


def main():
    out = []

    T = int(input())
    for _ in range(T):
        s = input().rstrip()  # 行末の改行を除去（readline は \n を含む）
        # ここで1テストケースを処理し、結果を out.append(...) する
        out.append(s)

    sys.stdout.write("\n".join(out) + "\n")


main()
