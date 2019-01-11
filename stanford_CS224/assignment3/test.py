from q1_window import *

data = [([[1,9], [2,9], [3,8], [4,8]], [1, 1, 4, 4])]

start = [5, 8]
end = [6, 8]

print (make_windowed_data(data, start, end, window_size = 1))
