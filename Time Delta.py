from datetime import datetime
tf = '%a %d %b %Y %H:%M:%S %z'
t = int(input())
for _ in range(t):
    x1 = datetime.strptime(input(),tf)
    x2 = datetime.strptime(input(),tf)
    dt = x1-x2
    print(int(abs(dt.total_seconds())))
