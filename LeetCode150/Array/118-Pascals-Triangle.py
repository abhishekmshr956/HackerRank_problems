"""https://leetcode.com/problems/pascals-triangle/"""

def pascals(n):
    p = []
    for i in range(n):
        a = []
        for j in range(i+1):
            if j == 0 or j == i:
                a.append(1)
            else:
                a.append(p[i-1][j] + p[i-1][j-1])
        p.append(a)
    return p

def pascals_fast(n):
    p = [[1]*(i+1) for i in range(n)]

    for i in range(n):
        for j in range(1, i):
            p[i][j] = p[i-1][j] + p[i-1][j-1]

    return p

if __name__ == '__main__':
    print(pascals(5))
    print(pascals_fast(5))