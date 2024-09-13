def amaiera_amankomuna  (str1, str2):
    # Revert the strings
    str1 = str1[::-1]
    str2 = str2[::-1]

    # See the similarities and save them
    common_str = ""
    for count in range(0,len(str1)):
        try:
            if str1[count] == str2[count]:
                common_str += str1[count]
            else:
                break
        except: 
            break
    # Return the result
    return common_str[::-1]

def main():
    # Ask for the strings
    str1 = input("Sartu lehenengo hitza: ")
    str2 = input("Sartu bigarren hitza: ")

    # Show the final result
    print(amaiera_amankomuna(str1, str2))

if __name__ == "__main__":
    main()