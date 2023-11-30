import objgraph
import random
import inspect

class Dna(object):
    def __init__(self):
        self.val = None
    def __str__(self):
        return "dna – val: {0}".format(self.val)

def f():
    l = []
    for i in range(3):
        dna = Dna()
        #print “id of dna: {0}”.format(id(dna))
        #print “dna is: {0}”.format(dna)
        l.append(dna)
    return l

def main():
    d = {}
    l = f()
    d['k'] = l
    print("list l has {0} objects of type Dna()".format(len(l)))
    objgraph.show_most_common_types()
    objgraph.show_backrefs(random.choice(objgraph.by_type('Dna')),
    filename="dna_refs.png")

    objgraph.show_refs(d, filename='myDna-image.png')

if __name__ == "__main__":
    main()