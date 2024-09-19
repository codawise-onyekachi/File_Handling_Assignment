
def create_and_write_file():
    try:
        # Create and open the file "my_file.txt" in write mode
        with open("my_file.txt", 'w') as new_file:
            
            # Write three lines of text with a mix of strings and numbers
            new_file.write("Hi, this is a new file.\n")
            new_file.write("The number of humans on earth is over 7 billion.\n")
            new_file.write("However, this number may reach about 8 billion by the end of 2025.\n")

        # Notify the user that the file has been created and written
        print("The file 'new_file.txt' has been created and written successfully.")

    except PermissionError:
        print("Error: You don't have permission to write to 'my_file.txt'.")
    
    except Exception as e:
        print(f"An unexpected error occurred while writing to the file: {e}")
    
    finally:
        print("File creation and writing operation complete.")


def read_file():
    try:       

        with open("my_file.txt", 'r') as new_file:
            content = new_file.read()
        print(content)

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    
    except PermissionError:
        print("Error: You don't have permission to read 'my_file.txt'.")
    
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    
    finally:
        print("File read operation complete.")


def append_to_file():
    try:

        with open("my_file.txt", "a") as new_file:
            new_file.write("This trend may continue for years to come\n")
            new_file.write("I think it is neccessary for human existence\n")
            new_file.write("And the benefit is increased human resources\n")
        print("The file 'new_file.txt' has been updatedsuccessfully.")

    except PermissionError:
        print("Error: You don't have permission to append to 'my_file.txt'.")
    
    except Exception as e:
        print(f"An unexpected error occurred while appending to the file: {e}")
    
    finally:
        print("File append operation complete.")


def read_updated_file():
    try:
        with open("my_file.txt", 'r') as new_file:
            outcome = new_file.read()
        print(outcome)

    except FileNotFoundError:
        print("Error: The file 'my_file.txt' was not found.")
    
    except PermissionError:
        print("Error: You don't have permission to read 'my_file.txt'.")
    
    except Exception as e:
        print(f"An unexpected error occurred while reading the file: {e}")
    
    finally:
        print("File read of (append)updated operation complete.")

    
# Run the functions with error handling
create_and_write_file()
read_file()
append_to_file()
read_updated_file()