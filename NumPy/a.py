# I. Lặp trên mảng (Iterating Arrays)

#   - Iterating (lặp) nghĩa là đi qua từng phần tử 1 trong một Array (Có thể hiểu là duyệt mảng)
#   - Khi xử lý mảng nhiều chiều trong NumPy, chúng ta có thể duyệt mảng bằng vòng lặp for cơ bản trong Python
# Nếu chúng ta duyệt 1 mảng 1 chiều, nó sẽ đi qua từng phần tử 1 của mảng đó

from os import system
import numpy as np

system('cls')

arr = np.array([1, 2, 3])

for x in arr:
    print(x)

#  II. Duyệt mảng 2 chiều