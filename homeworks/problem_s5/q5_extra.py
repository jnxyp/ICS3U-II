from math import sin


def gen_bar_chart_horizontal(data: list, char: str = '#', width: int = -1, title: str = 'Graph', y_label: str = 'value',
                             x_label: str = 'index'):
    out = ''
    max_index = len(data)
    max_value = max(data)

    if width == -1:
        width = len(str(max_index)) + 1

    out += ' ' + ' ' * (len(str(max_value)) + 1) + ' '
    out += title.center(max_index * width) + ' '
    out += '\n'

    out += ' ' + ' ' * (len(str(max_value)) + 1) + ' '
    out += '-' * (max_index * width) + ' '
    out += '\n'
    out += ' ' + ' ' * (len(str(max_value)) + 1) + '/' + ' '
    out += ' ' * (max_index * width) + '\\'
    out += '\n'

    for line in range(0, max_value):
        # print y-label
        if line < len(y_label):
            out += y_label[line]
        else:
            out += ' '
        # print value label
        out += ' ' * (len(str(max_value)) - len(str(max_value - line)) + 1)
        out += str(max_value - line) + '|' + ' '
        # print each bar
        for col in range (0, max_index):
            if data[col] >= max_value - line:
                out += (char*(width - 1)).center(width)
            else:
                out += ' ' * width
        out += '|' + '\n'

    out += ' ' + ' ' * (len(str(max_value)) + 1) + '\\' + ' '
    for col in range(0, max_index):
        out += str(col).center(width)
    out += '/' + '\n'
    out += ' ' + ' ' * (len(str(max_value)) + 1) + ' '
    out += '-' * (max_index * width) + ' '
    out += '\n'

    out += ' ' + ' ' * (len(str(max_value)) + 1) + ' '
    out += x_label.center(max_index * width) + ' '
    out += '\n'
    return out

print(gen_bar_chart_horizontal([int(sin(x/5) * 20) for x in range(1,100)]))
