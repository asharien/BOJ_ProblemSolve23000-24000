import sys
def fib(N):
    if N == 1 or N == 2: return 1
    else: return (fib(N-1) + fib(N-2))
def fibonacci(N, DP, C):
    for i in range(3, N+1):
        DP[i] = DP[i-1]+DP[i-2]
        C +=1
    return [DP[N], C]
def main():
    N = int(sys.stdin.readline())
    DP = [0 for i in range(N+1)]
    DP[0], DP[1], DP[2], DP[3] = 0, 1, 1, 2
    C = 0
    print(*fibonacci(N, DP, C))
if __name__ == "__main__":
    main()

