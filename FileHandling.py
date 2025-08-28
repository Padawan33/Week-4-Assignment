import os

def process_file(input_filename, output_filename):
    """
    Reads a file, converts its content to uppercase, and writes the
    modified content to a new file. It includes error handling for
    file-related issues.

    Args:
        input_filename (str): The name of the file to read from.
        output_filename (str): The name of the file to write to.
    """
    # Use a try-except block to gracefully handle potential errors during file operations.
    try:
        # Check if the input file exists before attempting to open it.
        if not os.path.exists(input_filename):
            # Raise a FileNotFoundError if the file does not exist,
            # which will be caught by our except block.
            raise FileNotFoundError(f"Error: The file '{input_filename}' does not exist.")

        # Open the input file for reading and the output file for writing.
        # The 'with' statement ensures the files are automatically closed,
        # even if an error occurs.
        with open(input_filename, 'r') as infile, open(output_filename, 'w') as outfile:
            print(f"Reading from '{input_filename}' and writing to '{output_filename}'...")
            
            # Read the entire content of the input file.
            content = infile.read()
            
            # Perform the modification: convert all text to uppercase.
            modified_content = content.upper()
            
            # Write the modified content to the output file.
            outfile.write(modified_content)
            
            # Print a success message.
            print("File processing completed successfully!")
            print(f"A new file '{output_filename}' has been created with the modified content.")

    except FileNotFoundError as e:
        # This block catches the specific FileNotFoundError.
        print(e)
    except Exception as e:
        # This block catches any other unexpected errors during the process.
        print(f"An unexpected error occurred: {e}")

# --- Main program execution ---

if __name__ == "__main__":
    # Prompt the user for the input and output filenames.
    input_file = input("Enter the name of the file to read (e.g., 'source.txt'): ")
    output_file = input("Enter the name of the new file to create (e.g., 'destination.txt'): ")
    
    # Call the function to perform the file operations.
    process_file(input_file, output_file)