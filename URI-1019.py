N = int(input())

M, S = divmod(N,60)

H, M = divmod(M,60)

print(f"{H}:{M}:{S}")