import random
import sys

# bubble sort algorithm
def bubble_sort(arr):
    n =  len(arr)

    for i in range(n):
        for j in range(0, n):

            if arr[j] > arr[j + 1]:
                temp = arr[j]
                arr[j] = arr[j + 1]
                arr[j + 1] = temp

    return arr
    

# generates random array based on max length and maxmin value
def generate_random_array():
    max_length = 20

    # max value and min value (-max)
    maxmin_value =  100000
    length = random.randint(1,max_length)
    out_arr = [0] * length
    for i in range(length):
        # generate random number
        rand_num = random.randint(-maxmin_value, maxmin_value)
        out_arr[i] = rand_num

    return out_arr


def random_test(iterations):

    # runs the test a certain amount of iterations
    for i in range(iterations):
        try:
            
            rand_arr = generate_random_array()
            print(f"Initial Array:   {rand_arr}\n\n")

            sorted_arr = bubble_sort(rand_arr)
            print(f"After Sort:   {sorted_arr}\n")

            print("No errors found.\n\n")
        except Exception as e:
            print(f"Error: {type(e).__name__} - {e}")
        

def main():
    random_test(10)

main()
