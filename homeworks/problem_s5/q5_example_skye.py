
data = [1,2,3,4,5,6,7,8,9]
# 标题
print('Graph'.center(len(data) * 2))
# 上面的横线
print('-' * len(data) * 2)
# 条形图部分
for row in range(max(data), 0, -1):
    s = ''
    for col in range(0, len(data)):
        if data[col] >= row:
            s = s + '#'
        else:
            s = s + ' '
        s = s + ' '
    print(s)
# 横轴数字
s = ''
for index in range(1, len(data) + 1):
    s = s + str(index) + ' '
print(s)
# 下面的横线
print('-' * len(data) * 2)
# 横轴标签
print('Index'.center(len(data) * 2))