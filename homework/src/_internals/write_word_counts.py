import os


def write_word_counts(counter,output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    # save the results using tsv format
    with open("data/output/results.tsv", "w", encoding="utf-8") as f:
            for key, value in counter.items():
                # write the key and value to the file
                f.write(f"{key}\t{value}\n")