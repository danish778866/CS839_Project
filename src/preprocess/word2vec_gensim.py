from gensim.models import KeyedVectors
import os
project_dir = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

def word2vec(path):
    filename = project_dir+os.sep+"src"+os.sep+"models"+os.sep+"third_party"+os.sep+"GoogleNews-vectors-negative300.bin"
    model = KeyedVectors.load_word2vec_format(filename, binary=True)
    vec = []
    #return vec
    with open(path) as list:
        num=0
        current_line = list.readline()
        while current_line:
            num=num+1
            print(num)
            phrase = current_line.split()
            cur_tag = [0]*300
            j = 0
            for w in phrase:
                this_tag=[0]*300
                if w in model.vocab:
                    this_tag = model[w]
                i=0
                while i<len(this_tag):
                    cur_tag[i]=cur_tag[i]+this_tag[i]
                    i=i+1
                j=j+1
            i=0
            while i<len(cur_tag):
                cur_tag[i]=cur_tag[i]/j
                i=i+1
            vec.append(cur_tag)
            current_line = list.readline()
    list.close()
    return vec

def write_array(path, content, header):
    f = open(path, "w")
    f.write(str(header)+"\n")
    for line in content:
        f.write(','.join(str(var) for var in line) + "\n")
    f.close()

a = "w2v"
under = "_"
comma= ","
head=""
i=0
while i<299:
    cnt = str(i)
    head=head+a+under+cnt+comma
    i=i+1
ctr = "299"
head=head+a+under+ctr
writeTO = project_dir+os.sep+"data"+os.sep+"features"+os.sep+"word2vec.csv"
candFile = project_dir+os.sep+"data"+os.sep+"candidates"+os.sep+"candidates.csv"
write_array(writeTO,word2vec(candFile),head)

