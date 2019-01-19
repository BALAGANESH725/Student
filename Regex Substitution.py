import sys
if sys.version_info[0]>=3: raw_input = input
for _ in range(int(raw_input())):
    print(raw_input().replace(' || ',' or ').replace(' && ',' and ').replace(' || ',' or').replace(' && ',' and '))
