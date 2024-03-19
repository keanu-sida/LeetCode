## 2D array points[i] = [start_i_, end_i_] representing horizontal diameter of spherical balloons on a wall
## Return Integer of # of arrows minimum to pop all balloons

class Solution:
    def popBalloons(points) -> int:
        points.sort(key = lambda x: x[0])               # sort points array by start of interval
        end = points[0][1]                              # initialize end variable as first interval's end, to be checked for overlap
        arrows = 1                                      # initalize # arrows as 1, since len(points) > 0
        for balloon in points[1:]:                      # iterate over all ranges
            if balloon[0] > end:                        # if balloon start > current end, no overlap, so one more arrow required
                arrows += 1                             
                end = balloon[1]
            else:                                       
                end = min(end, balloon[1])              # if balloon start <= current end, no need to add arrow since overlap
        return arrows                                   # after iterating, return number of arrows required
