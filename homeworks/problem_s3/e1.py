# Course Code: ICS3U
# Author: jn_xyp
# Version: 2017-10-10
# Problem Set 3 - Extra 1


def calc_overlap_area(_xa1: int, _ya1: int, _xa2: int, _ya2: int, _xb1: int, _yb1: int,
                      _xb2: int, _yb2: int):
    return max(min(_xa2, _xb2) - max(_xa1, _xb1),0) * max(min(_ya2, _yb2) - max(_ya1, _yb1), 0)



# Normal overlap
print(calc_overlap_area(1, 1, 3, 3, 2, 2, 4, 4))
# Switch position with another rectangle
print(calc_overlap_area(2, 2, 4, 4, 1, 1, 3, 3))
# One includes another
print(calc_overlap_area(-2, -2, 4, 4, 1, 1, 3, 3))
# One inserts another
print(calc_overlap_area(2, 2, 4, 4, 3, 0, 5, 5))
# No Overlap
print(calc_overlap_area(-2, -2, 0, 0, 1, 1, 3, 3))