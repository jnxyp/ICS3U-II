def print_horizontal_bar_chart(data):
    for num in data:
        print('#' * num)

def print_vertical_bar_chart(data):
    for row in range(max(data), 0, -1):
        s = ''
        for col in range(0, len(data)):
            if data[col] >= row:
                s = s + '#'
            else:
                s = s + ' '
            s = s + ' '
        print(s)


print_vertical_bar_chart([1, 2, 3, 4, 5, 6, 7, 8])
print_horizontal_bar_chart([1, 2, 3, 4, 5, 6, 7, 8])
