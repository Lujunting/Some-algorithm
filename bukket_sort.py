# bucket sort
list_num = [4,1,5,2,7]

bucket = []

for k in range (10):
    bucket.append(0)    # [0,0....,0]


for num in list_num:
    bucket[num] = bucket[num] + 1        # <---關鍵
# 4號桶 1票
# 1號桶 1票
# ...
index = 0
for k in range(10):
    if bucket[k] != 0:
        for j in range(bukket[k]):
            list_num[index] = k
            index += 1

print(list_num)