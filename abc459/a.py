x = int(input())
print("".join(r for index, r in enumerate(list("HelloWorld")) if index != x - 1))