# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-10-18
# Problem Set 4 - Question 2
import io

txt_file = open('mobydick_vol_1.txt')
txt = txt_file.read()
txt_file.close()

print('The book is', len(txt), 'characters long.')
print('The book is', len(txt) - txt.count(' '), 'characters long without spaces.')
txt_low = txt.lower()
print('There are', txt_low.count('a'),'\'a\' in the book.')
print('There are', txt_low.count('the'), '\'the\' in the book.')
print('There are', txt_low.count('the white whale'), '\'the white whale\' in the book.')
year_max = 0
max_freq = 0
for year in range(1800,1901):
    temp = txt.count(str(year))
    if temp > max_freq:
        max_freq = temp
        year_max = year
print('The year', year_max, 'appears most frequently, it appears', max_freq, 'times.')
print('The last time \'the sea\' appear at', txt_low.rfind('the sea'))
print('There are', txt_low.rfind('ahab') - txt_low.find('ahab'), 'characters between first and last \'ahab\'.')