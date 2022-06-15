import sys

h,m,s = map(int, sys.stdin.readline().split())
time = int(input())

def koi(h,m,s,time):
    if time >= 60:
        if time // 60 >= 60:
            s += time % 60
            time = time // 60
            m += time % 60
            h +=  time // 60
        else :
            m += time // 60
            s += time % 60
    
    if s >= 60: 
        m += s // 60
        s = s % 60
    if m >= 60:
        h += m // 60
        m = m % 60
    if h >= 24:
        h = h - 24

def koi1(h,m,s,time):
    s += time % 60
    time = time // 60
    if s >= 60:
        s -= 60
        m += 1

    m += time % 60
    time = time // 60
    if m >= 60:
        m -= 60
        h += 1

    h += time % 24
    if h >= 24:
        h -= 24

    result = f"{h} {m} {s}"
    return result


print(koi1(h,m,s,time))