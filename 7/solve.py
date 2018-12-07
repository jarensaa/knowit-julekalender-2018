import time


numbers = [int(line) for line in open("input-vekksort.txt")]
length = [0 for i in range(len(numbers))]
testNumbers = [1, 1, 2, 3, 4, 5, 3, 4, 4, 4, 4, 5, 5, 7, 6, 6, 7, 8]


def lis(arr):
    startTime = time.time()
    n = len(arr)

    lis = [1]*n

    # Compute optimized LIS values in bottom up manner
    for i in range(1, n):
        if(i % 5000 == 0):
            endTime = time.time()
            print("{} : {:4.2f}".format(i, endTime - startTime))
            startTime = time.time()
        for j in range(0, i):
            if arr[i] >= arr[j] and lis[i] < lis[j] + 1:
                lis[i] = lis[j]+1

    # Initialize maximum to 0 to get the maximum of all
    # LIS
    maximum = 0

    # Pick maximum of all LIS values
    for i in range(n):
        maximum = max(maximum, lis[i])

    return maximum


print(lis(testNumbers))
