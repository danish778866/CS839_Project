from nltk.corpus import wordnet
def word(w):
    if not wordnet.synsets(w):
        return False
    else:
        return True

def preprocess_labeled_files(path1, path2, path3):
    valid_cand = []
    valid_pre = []
    valid_suff  = []
    
    with open(path1) as candidates:
        current_line = candidates.read()
        cand_words = current_line.split()
        v_c = True
        for w in cand_words:
            v_c = word(w) or v_c
        if v_c == True:
            valid_cand.append(1)
        else:
            valid_cand.append(0)
    candidates.close()

    with open(path2) as prefix:
        current_line = prefix.read()
        pre_words = current_line.split()
        v_p = True
            for w in pre_words:
                v_p = word(w) or v_p
        if v_p == True:
            valid_pre.append(1)
        else:
            valid_pre.append(0)
    prefix.close()

    with open(path3) as suffix:
        current_line = suffix.read()
        suf_words = current_line.split()
        v_s = True
            for w in suf_words:
                v_s = word(w) or v_s
        if v_s == True:
            valid_suff.append(1)
            else:
                valid_suff.append(0)
    suffix.close()

    return valid_cand, valid_pre, valid_suff

def write_data(path, content):
    f = open(path, "w")
    for line in content:
        f.write(str(line) + "\n")
    f.close()

valid_cand, valid_pre, valid_suff  = preprocess_labeled_files(

