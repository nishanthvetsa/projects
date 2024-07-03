#!/bin/bash

# Recursive Bubble Sort function
recursive_bubble_sort() {
    local arr=("$@")

    for ((i = 0; i < ${#arr[@]} - 1; i++)); do
        if [[ ${arr[$i]} -gt ${arr[$((i + 1))]} ]]; then
            # Swap elements
            local temp=${arr[$i]}
            arr[$i]=${arr[$((i + 1))]}
            arr[$((i + 1))]=$temp
        fi
    done

    if [[ ${#arr[@]} -gt 1 ]]; then
        # Recursively call the function
        recursive_bubble_sort "${arr[@]}"
    fi

    echo "${arr[@]}"
}

# Example usage
sorted_array=($(recursive_bubble_sort 5 3 9 1 7))
echo "Sorted Array: ${sorted_array[@]}"
