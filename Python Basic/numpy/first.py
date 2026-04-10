# import numpy as np
# arr= np.array([1,2,3,4,5])
# print(type(arr))


#  how to fast to python

import numpy as np
import time
import numpy as np
import time

size = 1000000   # define size

# Python list
py_list = list(range(size))

start = time.time()
result = [x * 2 for x in py_list]
end = time.time()

print(f'Python list took {end - start} seconds')


# NumPy array
np_arr = np.arange(size)

start = time.time()
result = np_arr * 2
end = time.time()

print(f'NumPy took {end - start} seconds')
