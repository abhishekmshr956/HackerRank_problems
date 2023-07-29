def second_highest(n: int, arr: list):
    """ returns second highest number in a list of numbers"""
    a = sorted(list(set(arr)))
    print(a[-1])

if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    second_highest(n, arr)
    