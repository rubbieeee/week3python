def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read()  
    
        modified_content = content.upper()
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
        
    except FileNotFoundError:
        print(f"The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

input_filename = 'example.txt'  
output_filename = 'modified_example.txt'

read_and_write_file(input_filename, output_filename)


def read_file_with_error_handling():
    filename = input("Please enter the filename to read: ")
    
    try:
        # Attempt to open and read the file
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def read_and_write_file(input_filename, output_filename):
    try:
        with open(input_filename, 'r') as infile:
            content = infile.read() 
        modified_content = content.upper()
        
        with open(output_filename, 'w') as outfile:
            outfile.write(modified_content)
        
        print(f"Modified content has been written to {output_filename}")
        
    except FileNotFoundError:
        print(f"The file '{input_filename}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")

def read_file_with_error_handling():
    filename = input("Please enter the filename to read: ")
    
    try:
        with open(filename, 'r') as file:
            content = file.read()
            print("File content:")
            print(content)
    
    except FileNotFoundError:
        print(f"The file '{filename}' does not exist.")
    except PermissionError:
        print(f"You do not have permission to read the file '{filename}'.")
    except Exception as e:
        print(f"An error occurred: {e}")


def main():
    print("Choose an option:")
    print("1. Read a file and write a modified version to a new file.")
    print("2. Read a file with error handling.")
    
    choice = input("Enter the number of your choice: ")

    if choice == "1":
        input_filename = input("Enter the name of the file to read from: ")
        output_filename = input("Enter the name of the file to write to: ")
        read_and_write_file(input_filename, output_filename)
    elif choice == "2":
        read_file_with_error_handling()
    else:
        print("Invalid choice. Please enter 1 or 2.")


if __name__ == "__main__":
    main()