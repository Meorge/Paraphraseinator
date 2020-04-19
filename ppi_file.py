from ppi import Paraphraseinator
import sys
import os
from dotenv import load_dotenv

# load the API key from .env
load_dotenv()
KEY = os.getenv('THES_KEY')

def print_usage():
    print("Usage:")
    print("python3 ppi_file.py textfile [output [originality]]")
    print("\ttextfile - the path to the text file to paraphraseinate")
    print("\toutput - the file to output to (prints to console if not specified, or \"None\")")
    print("\toriginality - the originality value to use, between 0 and 1 (defaults to 0.5 if not specified)")
    return

# do the actual stuff
def para(input_file, output_file, orig):
    # if the input file doesn't exist, then exit
    if not os.path.exists(input_file):
        print(f"File {input_file} does not exist!")
        print_usage()
        sys.exit()

    # create the Paraphraseinator
    p = Paraphraseinator(KEY)

    # open the input file, paraphraseinate it
    with open(input_file, "r") as f:
        paraphrased = p.paraphraseinate(f.read(), orig)

        # if output file not specified, print out the paraphraseinated text
        if output_file is None or output_file == "None":
            print(paraphrased)
        else:
            ff = open(output_file, "w")
            ff.write(paraphrased)
            ff.close()
    
    return

if len(sys.argv) == 2: # ppi_file.py textfile
    para(sys.argv[1], None, 0.5)
    sys.exit()

elif len(sys.argv) == 3: # ppi_file.py textfile output
    para(sys.argv[1], sys.argv[2], 0.5)
    sys.exit()

elif len(sys.argv) == 4: # ppi_file.py textfile output originality
    try:
        para(sys.argv[1], sys.argv[2], float(sys.argv[3]))
    except ValueError:
        print(f"Value {sys.argv[3]} couldn't be converted to a float!")
        print_usage()
    sys.exit()

else:
    print("Invalid number of arguments.")
    print_usage()
    sys.exit()

