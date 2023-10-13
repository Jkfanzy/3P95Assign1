import random
import sys

def bubble_sort(arr):
    n =  len(arr)

    for i in range(n):
        for j in range(0, n-i-1):

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr
    

def generate_random_array():
    max_length = 50
    maxmin_value =  1000
    length = random.randint(1,max_length)
    out_arr = [0] * length
    for i in range(length):
        # generate random number
        rand_num = random.randint(-maxmin_value, maxmin_value)
        out_arr[i] = rand_num

    return out_arr

def random_test(iterations):

    for i in range(iterations):
        rand_arr = generate_random_array()
        print(f"Initial Array:   {rand_arr}\n\n")

        sorted_arr = bubble_sort(rand_arr)
        print(f"After Sort:   {sorted_arr}\n")
        

def main():
    random_test(10)

main()
