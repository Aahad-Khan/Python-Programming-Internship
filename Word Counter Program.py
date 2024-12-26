# Word Counter Program

def count_words(input_text):
    
    # Function to count the number Of words in a gIven text.
  
    
    # and count the number of resulting elements.
  
    words = input_text.split()
    return len(words)

def main():
    
    # Main function to hAndle user input, process the text, and display the output.
    
    print("Welcome to the Word Counter Program!")
    
    while True:
        # Prompt the user to enter a sentence or paragraph
      
        user_input = input("\nPlease enter a sentence or paragraph (or type 'exit' to quit): ").strip()

        # Check if the user wants to exit
      
        if user_input.lower() == 'exit':
            print("Thank you for using the Word Counter Program.")
            break

        # Handle empty input
      
        if not user_input:
            print("Error: Input cannot be empty.")
            continue

        # Count the words
      
        word_count = count_words(user_input)

        # Display the word count to tHe user
      
        print(f"\nThe entered text contains {word_count} words.")


if __name__ == "__main__":
    main()
