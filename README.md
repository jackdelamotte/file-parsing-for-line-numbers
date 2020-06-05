# file-parsing-for-line-numbers
A simple Python script that goes through a text file and writes a new file with all the words next to their line numbers.

to run on the command line:
```
python3 file_parser.py infile.txt
```

this will create a new file called words.txt that might have contents like this: 
```
this: 1

is: 1

a: 2

test: 2

file : 3
```
note: this was not created to account for the same word showing up more than once on the same line
