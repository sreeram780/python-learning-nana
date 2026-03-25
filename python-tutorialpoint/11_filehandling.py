# file = open("filename", "mode")
# # Opening a file in read mode
# file = open("example.txt", "r")
# # Opening a file in write mode
# file = open("example.txt", "w")
# # Opening a file in append mode
# file = open("example.txt", "a")
# # Opening a file in binary read mode
# file = open("example.txt", "rb")
# # Open a file
# fo = open("foo.txt", "wb")
# print ("Name of the file: ", fo.name)
# print ("Closed or not: ", fo.closed)
# print ("Opening mode: ", fo.mode)
# fo.close()
#
# # read() − Reads the entire file.
# # readline() − Reads one line at a time.
# # readlines − Reads all lines into a list.
#
# with open("foo.txt", "w") as file:
#    file.write("Hello, World!")
#    print ("Content added Successfully!!")
#
# lines = ["First line\n", "Second line\n", "Third line\n"]
# with open("example.txt", "w") as file:
#    file.writelines(lines)
#    print ("Content added Successfully!!")
#
# file = open("example.txt", "w")
# file.write("This is an example.")
# file.close()
# print ("File closed successfully!!")
#
# with open("example.txt", "w") as file:
#    file.write("This is an example using the with statement.")
#    print ("File closed successfully!!")

try:
   file = open("example.txt", "w")
   file.write("This is an example with exception handling.")
finally:
   file.close()
   print ("File closed successfully!!")

file = open("example.txt", "w")
file.write("Hello, World!")
file.close()
print ("File opened successfully!!")

file = open("example.txt", "a")
file.write("Appending this line.\n")
file.close()
print ("File opened successfully!!")

# Open a file in write mode
with open("example.txt", "w") as file:
   file.write("Hello, World!\n")
   file.write("This is a new line.\n")
print ("File opened successfully!!")

# Open a file in append mode
fo = open("foo.txt", "a")
text = "TutorialsPoint has a fabulous Python tutorial"
fo.write(text)

# Close opened file
fo.close()

# Write initial data to the file
# fo.write("This is a rat race")
# # Move the read/write pointer to the 10th byte
# fo.seek(10, 0)
# # Read 3 bytes from the current position
# data = fo.read(3)
# # Move the read/write pointer back to the 10th byte
# fo.seek(10, 0)
# # Overwrite the existing content with new text
# fo.write('cat')
# # Close the file
# fo.close()

# Open the file in read mode
file = open('example.txt', 'r')
# Read all lines from the file
lines = file.readlines()
# Print the lines
for line in lines:
   print(line, end='')
# Close the file
file.close()

# Using the with statement to open a file
with open('example.txt', 'r') as file:
   content = file.read()
   print(content)

import os

# Current file name
current_name = "oldfile.txt"
# New file name
new_name = "newfile.txt"
# Rename the file
# os.rename(current_name, new_name)
# print(f"File '{current_name}' renamed to '{new_name}' successfully.")

# File to be deleted
file_to_delete = "file_to_delete.txt"
# Delete the file
# os.remove(file_to_delete)
print(f"File '{file_to_delete}' deleted successfully.")

# Relative path − A path relative to the current working directory.
# Absolute path − A complete path starting from the root directory.

import os
directory_path = "D:\\Test\\MyFolder\\"
if os.path.exists(directory_path):
   print(f"The directory '{directory_path}' exists.")
else:
   print(f"The directory '{directory_path}' does not exist.")

import os
new_directory = "new_dir.txt"
try:
   os.makedirs(new_directory)
   print(f"Directory '{new_directory}' created successfully.")
except OSError as e:
   print(f"Error: Failed to create directory '{new_directory}'. {e}")

import os
# Create a directory "test"
os.mkdir("test")
print ("Directory created successfully")

current_directory = os.getcwd()
print(f"Current working directory: {current_directory}")

import os
new_directory = r"D:\MyFolder\Pictures"
try:
    os.chdir(new_directory)
    print(f"Current working directory changed to '{new_directory}'.")
except OSError as e:
    print(f"Error: Failed to change working directory to '{new_directory}'. {e}")

1
file.close()

Close the file. A closed file cannot be read or written any more.

2
file.flush()

Flush the internal buffer, like stdio's fflush. This may be a no-op on some file-like objects.

3
file.fileno()

Returns the integer file descriptor that is used by the underlying implementation to request I/O operations from the operating system.

4
file.isatty()

Returns True if the file is connected to a tty(-like) device, else False.

5
file.next()

Returns the next line from the file each time it is being called.

6
file.read([size])

Reads at most size bytes from the file (less if the read hits EOF before obtaining size bytes).

7
file.readline([size])

Reads one entire line from the file. A trailing newline character is kept in the string.

8
file.readlines([sizehint])

Reads until EOF using readline() and return a list containing the lines. If the optional sizehint argument is present, instead of reading up to EOF, whole lines totalling approximately sizehint bytes (possibly after rounding up to an internal buffer size) are read.

9
file.seek(offset[, whence])

Sets the file's current position

10
file.tell()

Returns the file's current position

11
file.truncate([size])

Truncates the file's size. If the optional size argument is present, the file is truncated to (at most) that size.

12
file.write(str)

Writes a string to the file. There is no return value.

13
file.writelines(sequence)

Writes a sequence of strings to the file. The sequence can be any iterable object producing strings, typically a list of strings.