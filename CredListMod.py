import os
import re
import argparse
from datetime import datetime


def complexity(argalpha=False, argul=False, argnum=False, argspec=False, argmin=6, argmax=256):
    alpha = ''
    num = ''
    spec = ''
    
    if argalpha or argul: # Building alphabet requirements
        if argul: # If Upper AND Lower are required
            alpha = r'(?=.*[a-z])(?=.*[A-Z])'
        else: # If Upper OR Lower are required
            alpha = r'(?=.*[a-zA-Z])' 
    if argnum: #If numbers are required
        num = r'(?=.*[0-9])'
    if argspec: # If special characters are required
        spec = r'(?=.*[^a-zA-Z0-9_])'
    regex = f"{alpha}{num}{spec}.{{{argmin},{argmax}}}"
    return re.compile(regex)


def process(wordlists, requirements, output):
    lread = 0 # Total lines Read
    lwrite = 0 # Total lines wrote

    try:
        # Open the output file for writing
        with open(output, "w", encoding="utf-8") as file_out:
            #Process each list
            for wordlist in wordlists:
                print(f"Processing {wordlist}")
                with open(wordlist, "r", encoding="utf-8", errors="replace") as file_in:
                    for line in file_in:
                        lread += 1
                        if requirements.match(line.strip()):  # If line matches the password requirements
                            lwrite += 1
                            file_out.write(line.strip() + '\n')  # Write matching line to output file
    except FileNotFoundError as e:
        print(f"Error: The file '{e.filename}' was not found.")
        exit(1)
    except Exception as e:
        print(f"An error occurred: {e}")
        exit(1)
    return lread, lwrite


def results(lread,lwrite,out,start):
    end = datetime.now()
    runtime = end - start
    # Extract hours, minutes, and seconds from the timedelta
    hours, remainder = divmod(runtime.total_seconds(), 3600)
    minutes, seconds = divmod(remainder, 60)

    print(f"Processing completed at {end.hour}:{end.minute}:{end.second} ")
    print(f"New wordlist {out} created.")
    print(f"Total # of lines processed: {lread}.")
    # If no matching lines, report
    if lwrite <= 0:
        print("No lines matched requirements. Please verify your settings and run again.")
    else:
        print(f"Total # of lines matching requirements: {lwrite}")
    print(f"Total runtime: {int(hours)} hours, {int(minutes)} minutes, {seconds:.2f} seconds")


def main():
    starttime = datetime.now()
    print(f'Starting: {starttime.strftime("%H:%M:%S")}')

    # Command-line argument parser
    parser = argparse.ArgumentParser(prog='CredListMod', description='Parses wordlists against password requirements and creates new list.')

    # Complexity requirements
    parser.add_argument('--alphabet', '-a', action='store_true', help='Require at least one upper or lowercase letter')
    parser.add_argument('--capital', '-c', action='store_true', help='Require both uppercase and lowercase letters')
    parser.add_argument('--number', '-n', action='store_true', help='Require at least one number')
    parser.add_argument('--special', '-s', action='store_true', help='Require at least one special character')
    parser.add_argument('--minimum', '-m', type=int, default=6, help='Minimum password length (default is 6)')
    parser.add_argument('--maximum', '-M',  type=int, default=256, help='Maximum password length (default is 256)')
    # File arguments
    parser.add_argument('--wordlist', '-w', nargs='+', required=True, help='Wordlist to parse')
    parser.add_argument('--output', '-o', required=True, help='Output file')

    # Parsing the command-line arguments
    args = parser.parse_args()

    # Check if the output file already exists
    if os.path.exists(args.output):
        response = input(f"The output file '{args.output}' already exists. Do you want to overwrite it? (y/N): ").strip().lower()
        if response != 'y':
            print("Operation aborted by the user.")
            exit(0)

    # Creating the Requirements pattern
    pattern = complexity(argalpha=args.alphabet, argul=args.capital, argnum=args.number, argspec=args.special, argmin=args.minimum, argmax=args.maximum)

    # Processes input wordlist and creates output
    lread, lwrite = process(args.wordlist, pattern, args.output)

    # Prints results to the screen
    results(lread, lwrite, args.output, starttime) 


if __name__ == "__main__":
    main()
