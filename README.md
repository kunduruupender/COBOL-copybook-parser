# COBOL-copybook-parser

This code is a Python script that performs some operations on a copybook file. Here is a brief description of the different parts of the code:

1. The script starts by importing the `os` module.
2. There are several functions defined in the code:
   - `removeBeforeAndAfterSeventyTwo(lines)`: This function removes lines containing '*' and trims lines longer than 72 characters. It returns the modified lines.
   - `duplicateField(lines)`: This function checks for duplicate field names in lines and appends a suffix to the duplicate fields to make them unique.
   - `redfination(lines)`: This function splits the lines based on the '.' delimiter, extracts certain information, and redefines the lines accordingly.
   - `indentation(lines)`: This function adds indentation to the lines based on their record type.
   - `maxLengthSeventyTwo(lines, dir_path)`: This function truncates lines longer than 72 characters and writes the modified lines to an output file.
   - `keepBetweenSeventhandSeventySecond(line)`: This function keeps the content of a line between the seventieth and seventy-second characters.
   - `copybookAsset()`: This function serves as the entry point of the script. It takes user input for the file path, reads the file, and performs various transformations on the lines of the copybook.

3. The `copybookAsset()` function is called at the end of the script, initiating the execution of the operations on the copybook file.

Overall, this script aims to parse and modify a copybook file by removing unnecessary lines, handling duplicate fields, redefining certain lines, adding indentation, and ensuring that lines are not longer than 72 characters.
