import collections

n = int(input())
n_list = list(map(int, input().split()))

m = int(input())
m_list = list(map(int, input().split()))

result = collections.Counter(n_list)

for i in m_list:
    print(result[i])