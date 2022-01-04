## 10250. ACM 호텔 (01.04)
T = int(input())
for _ in range(T):
    h, w, n = map(int, input().split())
    count = 0
    for nw in range(w):
        for nh in range(h):
            count += 1
            if count == n:
                print("%d%02d" % (nh + 1, nw + 1))
                break
