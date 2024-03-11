import sys
def BROKEN(A, S, B, PRV):
    if S == "+":return A+B-PRV
    elif S == "-":return (A-B)*PRV
    elif S == "*":return (A*B)**2
    elif S == "/":
        if A%2 == 0:return A//2
        elif A%2 == 1:return (A+1)//2
def main():
    PRV = 1
    for _ in range(int(sys.stdin.readline())):
        X, S, Y = map(str, sys.stdin.readline().split())
        PRV = BROKEN(int(X), S, int(Y), PRV)
        print(PRV)
if __name__ == "__main__":
    main()


