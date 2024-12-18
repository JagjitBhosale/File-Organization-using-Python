# File-Organization-using-Python
This Python script automates the organization of files in a directory by categorizing them into subfolders based on their file types. The script uses the os and shutil libraries to handle file operations and ensures error handling for smooth execution

# File Organization Tool

This Python script automates the organization of files in a specified directory by categorizing them into subfolders based on their file types (extensions). The script uses the `os` and `shutil` libraries for file operations and ensures proper handling of exceptions.

---

## Features

- **Dynamic File Organization**:
  - Scans a given directory (`unorganizedFolder`) for files.
  - Classifies files into subfolders based on their file type/extensions (e.g., `.txt`, `.jpg`, `.pdf`).
  - Creates a folder named `organized` and organizes files into subfolders for each file type (e.g., `organized/txt`, `organized/jpg`).

- **Cross-Platform Compatibility**:
  - Supports both Windows and UNIX-based systems.
  - Uses `os.path.join()` for constructing paths to ensure compatibility.

- **Error Handling**:
  - Catches and logs errors for missing files or issues during file movement.

---

## Prerequisites

- Python 3.x installed on your system.
- Ensure the `unorganizedFolder` directory exists and contains files to organize.

---

## Installation

1. Clone the repository:

   ```bash
   git clone <repository-url>
   cd <repository-name>
   ```
2. Keep the python file in that folder where there is a unorganizedfolder and run the python code
2. Run the script:

   ```bash
   python organizeFile.py
   ```

---

## Usage

- Place the script in a directory containing files to organize (`unorganizedFolder`).
- Ensure the source directory (`unorganizedFolder`) contains files that need to be categorized.
- After running the script, an `organized` directory will be created with subfolders for each file type.

---

## Code Overview

### Function: `move_file(source_path, destination_path)`

Moves a file from `source_path` to `destination_path`. Handles exceptions like `FileNotFoundError`.

```python
import shutil
import os

def move_file(source_path, destination_path):
    try:
        shutil.move(source_path, destination_path)
        print(f"File moved from '{source_path}' to '{destination_path}'")
    except FileNotFoundError:
        print(f"Error: File not found at '{source_path}'")
    except Exception as e:
        print(f"Error moving file: {e}")
```

### Main Script Logic

```python
directory = 'unorganizedFolder'

for filename in os.listdir(directory):
    f = os.path.join(directory, filename)
    if os.path.isfile(f):
        filetype = f.split(".")[-1]
        destination_path = f"organized/{filetype}"
        os.makedirs(destination_path, exist_ok=True)
        move_file(f, destination_path)
```

---

This project is licensed under the [MIT License](LICENSE). Feel free to use and modify the code as per your needs.

---

You can copy this simpler version without big headings and any other formatting!
