try:
    file = open("example.txt", "r")
    content = file.read()
    print("File Content:\n", content)

except FileNotFoundError:
    print("Error: The file was not found!")

except Exception as e:
    print(f"An unexpected error occurred: {e}")

finally:
    try:
        file.close()  
        print("File closed successfully.")
    except NameError:
        print("File was never opened, so no need to close it.")
