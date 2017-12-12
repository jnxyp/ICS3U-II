# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-10-11
# Problem Set 3 - Question 6


def count_collatz_steps(n: int): return n / 2 if n % 2 == 0 else 3 * n + 1


def count_collatz_loop(n: int):
    nums = [n]
    while n != 1:
        nums.append(count_collatz_steps(n))
        n = nums[-1]
    return nums


def count_collatz_steps_2(n):
    # if n is even
    if n % 2 == 0:
        return n / 2
    # if n is odd
    else:
        return n * 3 + 1

def count_collatz_loop_2(n):
    step = ''
    # while n is not equal to 1
    while n != 1:
        step += str(n) + ','
        n = count_collatz_steps_2(n)
    return step + str(n)

def count_collatz_judge(n):
    '''
    (int) -> bool

    '''
    count = 0
    while n != 1:
        n = count_collatz_steps_2(n)
        count = count + 1
        if count > 1000:
            return False
    return True
for i in range(1,201):
    print(count_collatz_loop(i))



