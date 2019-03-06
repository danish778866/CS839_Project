from nltk.corpus import wordnet
from nltk.corpus import wordnet as wn

def tag_word(w):
    pos_l = set()
    tags = [0,0,0,0,0]
    for tmp in wn.synsets(w):
        if tmp.name().split('.')[0] == w:
            pos_l.add(tmp.pos())
    for val in pos_l:
        if val  == 'n':
            tags[0]=1;
        elif val  == 'v':
            tags[1]=1;
        elif val ==  'a':
            tags[2]=1;
        elif val  ==  's':
            tags[3]=1;
        elif val == 'r':
            tags[4]=1;
        else:
            print(w, val)
    return tags;

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

def is_missing(path):
    is_missing = []
    with open(path) as list:
        current_line = list.readline()
        while current_line:
            if current_line == "NA":
                is_missing.append(1)
            else:
                is_missing.append(0)
            current_line = list.readline()
    return is_missing

def nvasr(path):
    tags = []
    with open(path) as list:
        current_line = list.readline()
        while current_line:
            print(current_line)
            phrase = current_line.split()
            cur_tag =[0,0,0,0,0]
            for w in phrase:
                print(w)
                this_tag = tag_word(w.lower())
                print(this_tag)
                i=0
                while i<5:
                    if this_tag[i]==1:
                        cur_tag[i]=1
                    i=i+1
                print(cur_tag)
            tags.append(cur_tag)
            current_line = list.readline()
    list.close()
    return tags


valid_cand  = preprocess_labeled_files("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_candidates.txt")
valid_pre = preprocess_labeled_files("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_prefixes.txt")
valid_suff = preprocess_labeled_files("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_suffixes.txt")
is_missing_pre = is_missing("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_prefixes.txt")
is_missing_suf = is_missing("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_suffixes.txt")
nvasr_cand = nvasr("/Users/somya/Desktop/sem2/CS839_Project/data/candidates/all_candidates.txt")

write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_valid_cand.csv", valid_cand)
write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_valid_pre.csv", valid_pre)
write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_valid_suff.csv", valid_suff)
write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_missing_pre.txt", is_missing_pre)
write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/is_missing_suf.txt", is_missing_suf)
write_data("/Users/somya/Desktop/sem2/CS839_Project/data/features/tags_cand.txt",nvasr_cand)

