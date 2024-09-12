# CredListMod

CredListMod is a Python script that parses wordlists against specified password requirements and creates a new list containing only the passwords that meet those requirements.

## Features

- Filter wordlists based on various password complexity requirements
- Support for multiple input wordlists
- Customizable password length constraints
- Output matching passwords to a new file

## Requirements

- Python 3.x

## Installation

1. Clone this repository or download the `credlistmod.py` script.
2. Ensure you have Python 3.x installed on your system.

## Usage

Run the script from the command line with the following syntax:

```
python credlistmod.py [OPTIONS] --wordlist WORDLIST [WORDLIST ...] --output OUTPUT
```

### Options

- `--alphabet`, `-a`: Require at least one upper or lowercase letter
- `--capital`, `-c`: Require both uppercase and lowercase letters
- `--number`, `-n`: Require at least one number
- `--special`, `-s`: Require at least one special character
- `--minimum MINIMUM`, `-m MINIMUM`: Minimum password length (default is 6)
- `--maximum MAXIMUM`, `-M MAXIMUM`: Maximum password length (default is 256)
- `--wordlist WORDLIST [WORDLIST ...]`, `-w WORDLIST [WORDLIST ...]`: Input wordlist(s) to parse (required)
- `--output OUTPUT`, `-o OUTPUT`: Output file for matching passwords (required)

### Examples

1. Basic usage with default settings:
   ```
   python credlistmod.py -w input_wordlist.txt -o output_wordlist.txt
   ```

2. Require uppercase and lowercase letters, numbers, and set minimum length to 8:
   ```
   python credlistmod.py -c -n -m 8 -w input_wordlist.txt -o output_wordlist.txt
   ```

3. Process multiple wordlists with special characters required:
   ```
   python credlistmod.py -s -w wordlist1.txt wordlist2.txt -o combined_output.txt
   ```

## Output

The script will create a new file (specified by the `--output` option) containing only the passwords from the input wordlist(s) that meet the specified requirements. 


## Notes

- If the output file already exists, the script will prompt for confirmation before overwriting it.
- The script uses UTF-8 encoding for reading and writing files.

