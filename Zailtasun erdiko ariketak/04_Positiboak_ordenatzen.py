def positiboak_ordenatu  (num_list):
    # Safe position and value if is =< 0
    non_positive = {}
    for position in range(0,len(num_list)):
        if num_list[position] <= 0:
            non_positive[position] = num_list[position]

    # Sort rest of positive values
    for num in non_positive.values():
        num_list.remove(num)
    num_list = sorted(num_list)

    # Insert first nums
    for position, num in non_positive.items():
        num_list.insert(position, num)

    # Return the final list
    return num_list

def main():
    # Define test values
    num_list = [6, 3, -2, 5, -8, 2, -2]
    
    # Show the result to the user
    print(positiboak_ordenatu(num_list))

if __name__ == "__main__":
    main()