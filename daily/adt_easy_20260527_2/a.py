import sys
input = sys.stdin.readline

D = input().strip()

op = {
    "N": "S", "S": "N", "E": "W", "W": "E",
    "NE": "SW", "SW": "NE", "NW": "SE", "SE": "NW",
}

print(op[D])