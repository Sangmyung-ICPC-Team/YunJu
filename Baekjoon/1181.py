word_list = set()

num = int(input())

for i in range(num):
    word_list.add(input())

answer = sorted(word_list, key = lambda x: (len(x), x))

for i in answer:
    print(i)
