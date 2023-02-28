# ***************************************************
# *  Program Title: Pair Sum Algorithms
# *  Author: Hunter Duffek
# *  Class: CSCI3320,  Fall 2022
# *  Assignment #3
# ****************************************************

import random
import time

# ***************************************************
# *  FUNCTION  getPairsQuad :
# *    Quadratic time complexity function to return pairs of requested sums
# *  INPUT PARAMETERS :
# *    arr - array of random unsorted numbers, N - Size of arr, K - desired sum
# *  OUTPUT :
# *    sum pairs, if such exist, and a statement on whether or not they do
# ****************************************************


def getPairsQuad(arr, N, K):
    count = 0
    # Iterates through every instance in size of array to check for pairs
    for i in range(0, N):
        for j in range(i + 1, N):
            if arr[i] + arr[j] == K:
                print(f', ({arr[i]} + {arr[j]})', end='')
                count += 1
    if count > 0:
        print('\n\nYes, there are two numbers whose sum equals to K')
    else:
        print('\n\nNo, the algorithm could not find two numbers whose sum equals K')



# ***************************************************
# *  FUNCTION  getPairsLog :
# *    Logarithmic time complexity function to return pairs of requested sums
# *  INPUT PARAMETERS :
# *    arr - array of random unsorted numbers, N - Size of arr, K - desired sum
# *  OUTPUT :
# *    sum pairs, if such exist, and a statement on whether or not they do
# ****************************************************


def getPairsLog(arr, N, K):
    # quicksort algorithm to sort array
    quickSort(arr, 0, N - 1)
    l = 0
    r = N - 1
    count = 0
    # while loop that terminates once a pair sum is found, by checking the first and last indices
    while l < r:
        if arr[l] + arr[r] > K:
            r -= 1

        elif arr[l] + arr[r] < K:
            l += 1
        else:
            print(f', ({arr[l]} + {arr[r]})', end='')
            count += 1

            if arr[r - 1] == arr[r] and arr[l + 1] == arr[l]:
                l += 1
                r -= 1

            elif arr[r - 1] == arr[r]:
                r -= 1

            elif arr[l + 1] == arr[l]:
                l += 1

            else:
                l += 1
                r -= 1
    if count > 0:
        print('\n\nYes, there are two numbers whose sum equals to K')
    else:
        print('\n\nNo, the algorithm could not find two numbers whose sum equals K')



# Partitioning function to separate the array into two lists

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            (arr[i], arr[j]) = (arr[j], arr[i])

    (arr[i + 1], arr[high]) = (arr[high], arr[i + 1])

    return i + 1


# Recursive function to arrange array based on pivot positions

def quickSort(arr, low, high):
    if low < high:
        # Find pivot element such that
        # element smaller than pivot are on the left
        # element greater than pivot are on the right
        pi = partition(arr, low, high)

        # Recursive call on the left of pivot
        quickSort(arr, low, pi - 1)

        # Recursive call on the right of pivot
        quickSort(arr, pi + 1, high)


# ***************************************************
# *  FUNCTION  getPairsLin :
# *    Lin time complexity function to return pairs of requested sums
# *  INPUT PARAMETERS :
# *    arr - array of random unsorted numbers, N - Size of arr, K - desired sum
# *  OUTPUT :
# *    sum pairs, if such exist, and a statement on whether or not they do
# ****************************************************


def getPairsLin(arr, N, K):
    hashmap = {}
    count = 0
    # for loop checks for temp value in array
    for i in range(0, N):
        temp = K - arr[i]
        if temp in hashmap:
            print(f', ({arr[i]} + {temp})', end='')
            count += 1
        hashmap[arr[i]] = i

    if count > 0:
        print('\n\nYes, there are two numbers whose sum equals to K')
    else:
        print('\n\nNo, the algorithm could not find two numbers whose sum equals K')


# Driver code for user inputs and function calls

if __name__ == '__main__':
    while True:
        print('\n1.  Quadratic algorithm\n2.  Logarithmic algorithm\n3.  Linear algorithm\n4.  Exit the program\n')
        ch = input('Choose an algorithm: ')

        if ch == '4':
            break

        N = int(input('Enter size of random array: '))
        arr = []

        for i in range(0, N):
            x = random.randint(0, 999999)
            arr.append(x)
            if N < 50:
                print(f'{x} ', end='')

        K = int(input('Enter the K value: '))

        if ch == '1':
            print('Running the O(N^2) algorithm...')
            print(f'K = {K}', end='')
            timeStart = time.time_ns()
            getPairsQuad(arr, N, K)
            timeEnd = time.time_ns()
            print(f'Execution Time in nanoseconds: {timeEnd - timeStart} nanoseconds')

        elif ch == '2':
            print('Running the O(NlogN) algorithm...')
            print(f'K = {K}', end='')
            timeStart = time.time_ns()
            getPairsLog(arr, N, K)
            timeEnd = time.time_ns()
            print(f'Execution Time in nanoseconds: {timeEnd - timeStart} nanoseconds')

        elif ch == '3':
            print('Running the O(N) algorithm...')
            print(f'K = {K}', end='')
            timeStart = time.time_ns()
            getPairsLin(arr, N, K)
            timeEnd = time.time_ns()
            print(f'Execution Time in nanoseconds: {timeEnd - timeStart} nanoseconds')
