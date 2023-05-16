def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2
        mid_val = arr[mid]

        if mid_val == target:
            return mid
        elif mid_val < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1


def main():
    # Input the list of numbers separated by spaces
    input_list = input("Enter the list of numbers separated by spaces: ").split()
    # Convert the input string elements to integers
    numbers = [int(num) for num in input_list]

    # Sort the list
    sorted_numbers = sorted(numbers)

    # Input the target number to search
    target = int(input("Enter the number to search: "))

    # Perform binary search
    result = binary_search(sorted_numbers, target)

    # Print the result
    if result != -1:
        print(f"The number {target} is found in the list.")
    else:
        print(f"The number {target} is not found in the list.")


if __name__ == '__main__':
    main()
