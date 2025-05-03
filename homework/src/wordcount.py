# obtain a list of files in the input directory
import os

def read_all_lines():
    """Read all lines from the input files."""
    all_lines = []
    for filename in os.listdir('data/input/'):
        with open('data/input/' + filename, 'r', encoding='utf-8') as f:
            all_lines.extend(f.readlines())
    return all_lines

def main():
    input_directory_files=os.listdir('data/input/')

    # count the frequency of the words in the files in the input directory
    counter={}
    for filename in input_directory_files:
        with open('data/input/'+filename) as f:
            for l in f:
                for w in l.split( ):
                    w = w.lower().strip(",.!?")
                    counter[w] = counter.get(w, 0) + 1

    # create the directory output/ if it doesn't exist
    write_counts_words(counter)

def write_counts_words(counter):
    if not os.path.exists('data/output'):
        os.makedirs('data/output')

    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
            for key, value in counter.items():
                # write the key and value to the file
                f.write(f"{key}\t{value}\n")

if __name__ == '__main__':
    main()