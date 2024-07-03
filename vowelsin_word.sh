#!/bin/bash

# Function to count vowels using switch case
count_vowels() {
    local content="$1"
    local count=0

    for ((i = 0; i < ${#content}; i++)); do
        case "${content:$i:1}" in [aeiouAEIOU])
                ((count++))
                ;;
        esac
    done

    echo "Number of vowels: $count"
}

# Example usage
file_content=$(cat example.txt)
count_vowels "$file_content"
