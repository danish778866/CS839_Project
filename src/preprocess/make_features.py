from nltk.corpus import wordnet
def word(w):
    if not wordnet.synsets(w):
        return False
    else:
        return True

def preprocess_labeled_files(path1):
    valid_cand = []
    with open(path1) as candidates:
        current_line = candidates.readline()
        while current_line:
            cand_words = current_line.split()
            v_c = False
            for w in cand_words:
                v_c = word(w) or v_c
            if v_c == True:
                valid_cand.append(1)
            else:
                valid_cand.append(0)
            current_line = candidates.readline()
    candidates.close()
    return valid_cand

def write_data(path, content):
    f = open(path, "w")
    for line in content:
        f.write(str(line) + "\n")
    f.close()

valid_cand  = preprocess_labeled_files("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_candidates.txt")
valid_pre = preprocess_labeled_files("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_prefixes.txt")
valid_suff = preprocess_labeled_files("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_suffixes.txt")

write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_valid_cand.csv", valid_cand)
write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_valid_pre.csv", valid_pre)
write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_valid_suff.csv", valid_suff)


