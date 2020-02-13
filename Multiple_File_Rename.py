# Importing the os module
import os

if __name__ == '__main__':

    # Defining the path of folder from which you want to renames all the files
    source_folder_path = "FOLDER PATH WHICH CONTAINS THE FILES"

    # Defining the path of folder in which you wish to keep renamed files  # This can be same as source_folder_path
    destination_folder_path = "FOLDER PATH IN WHICH YOU WISH TO SAVE THE FILES"

    # Initializing a count variable to 0
    count = 1

    # Looping through all the files present in the folder
    for files in os.listdir(source_folder_path):

        # Getting the extension of the file
        file_extension = os.path.splitext(files)[1]

        # Defining a new name for the file with its extension
        new_name = "USER_INPUT_NAME " + str(count) + " " + file_extension

        # Getting the source address of the file
        source = source_folder_path + files
        # Defining the destination address to save the file with new name
        destination = destination_folder_path + new_name

        # Renaming the files the source files present in the directory
        os.rename(source, destination)

        # Incrementing the count variable
        count += 1

    print("\nALL THE FILES HAVE BEEN RENAMED SUCCESSFULLY")
