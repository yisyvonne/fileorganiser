import tkinter as tk # The libary responsible for GUI.
from tkinter import filedialog # This will create the folder selection dialogue.
import os # File directory operations
import shutil # Moving files operations

# The dictionary that holds all possible file types and classifies them.
file_cat = {
    # Images
    ".jpg": "Sorted_Images",
    ".jpeg": "Sorted_Images",
    ".png": "Sorted_Images",
    ".gif": "Sorted_Images",
    ".bmp": "Sorted_Images",
    ".tiff": "Sorted_Images",
    ".svg": "Sorted_Images",
    ".ico": "Sorted_Images",
    ".webp": "Sorted_Images",

    # Documents
    ".txt": "Sorted_Text",
    ".pdf": "Sorted_Documents",
    ".doc": "Sorted_Documents",
    ".docx": "Sorted_Documents",
    ".xls": "Sorted_Documents",
    ".xlsx": "Sorted_Documents",
    ".ppt": "Sorted_Documents",
    ".pptx": "Sorted_Documents",
    ".csv": "Sorted_Documents",
    ".rtf": "Sorted_Documents",
    ".odt": "Sorted_Documents",
    ".ods": "Sorted_Documents",
    ".odp": "Sorted_Documents",

    # Executables and Installers
    ".exe": "Sorted_Executables",
    ".msi": "Sorted_Executables",
    ".dmg": "Sorted_Executables",

    # Archives
    ".zip": "Sorted_Archives",
    ".rar": "Sorted_Archives",
    ".tar": "Sorted_Archives",
    ".7z": "Sorted_Archives",
    ".gz": "Sorted_Archives",
    ".bz2": "Sorted_Archives",

    # Videos
    ".mp4": "Sorted_Videos",
    ".avi": "Sorted_Videos",
    ".mkv": "Sorted_Videos",
    ".mov": "Sorted_Videos",
    ".wmv": "Sorted_Videos",
    ".flv": "Sorted_Videos",

    # Music
    ".mp3": "Sorted_Music",
    ".wav": "Sorted_Music",
    ".flac": "Sorted_Music",
    ".aac": "Sorted_Music",
    ".ogg": "Sorted_Music",

    # Other Common Types
    ".py": "Sorted_Python_Scripts",
    ".html": "Sorted_Webpages",
    ".css": "Sorted_Webpages",
    ".js": "Sorted_Webpages",
    ".json": "Sorted_Data",
    ".xml": "Sorted_Data",
    ".iso": "Sorted_Disk_Images",
}

#Creates destination folders for each category if they don't exist.
def create_destination_folders():
    global destination_path, folder_path  # Access global variables
    existing_extensions = {os.path.splitext(file)[1] for file in os.listdir(folder_path)}
    for category, extension in file_cat.items():
        if extension in existing_extensions:  
            folder_path = os.path.join(destination_path, category)
            if not os.path.exists(folder_path):
                os.makedirs(folder_path)


def organise_files(): # Organises files in the selected folder based upon their extension type.

    for filename in os.listdir(folder_path):
        # Gets the file extension including the dot.
        _, extension= os.path.splitext(filename)

        # If extention is in directory, categorise and move it.
        if extension in file_cat:
            category = file_cat[extension]
            destination_folder = os.path.join(destination_path, category)
        
            # Creates the directory folder if it doesn't exist. 
            if not os.path.exists(destination_folder):
                os.makedirs(destination_folder)

            # Move the file
            source_path = os.path.join(folder_path, filename)
            shutil.move(source_path, destination_folder)

            print(f"Moved '{filename}' to '{destination_folder}'")

            # Error handling
            try:
                shutil.move(source_path, destination_folder)
                print(f"Moved '{filename}' to '{destination_folder}'")
            except (PermissionError, shutil.Error) as e:
                print(f"Error moving '{filename}': {e}")

destination_path = None

# Opens the dialogue to select the desired folder to be organised.
def select_folder():
    global folder_path, destination_path 
    folder_path = filedialog.askdirectory()
    print(f"Selected folder: {folder_path}")

    # Sets default destination path to selected folder
    destination_path = folder_path

    # Create destination folders before organizing
    create_destination_folders() 

    # Calls the organise_files function
    organise_files()

    # Close the GUI window after selecting folder
    root.destroy()

# Variable to store the path
folder_path = None


# Creates the main window for the GUI.
root = tk.Tk()
root.title("File Organiser")

# Creates the button for the GUI
button = tk.Button(root, text = "Select the Folder You Wish to Organise")
button.config(command=select_folder) # Configures the button to call the select_folder function when the button is clicked. This passes a reference to the function instead of calling it immediately. 

# Place the button inside of the window.
button.pack()

# Starts the Tkinter event loop.
root.mainloop()

