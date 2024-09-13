def main():
    # Ask the user for a text
    text = input("Sartu testu bat: ")

    # Save each word of the text in a list
    final_list = list(dict.fromkeys(text.upper().split(" ")))[::-1]

    # Create the resultatn phrase
    phrase = ""
    for word in final_list:
        phrase += word + " "
    
    # Show the result to the user
    print("Emaitza: {}".format(phrase))

if __name__ == "__main__":
    main()