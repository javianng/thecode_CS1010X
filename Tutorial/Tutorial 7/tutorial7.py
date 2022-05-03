# Question 1

def accumulate(op, init, seq):
    if not seq:
        return init
    else:
        return op(seq[0], accumulate(op, init, seq[1:]))
    
def accumulate_n(op, init, sequences):
    if (not sequences) or (not sequences[0]):
        return type(sequences)()
    else :
        return ([accumulate(op , init , <T1 >)] + accumulate_n(op , init , <T2>))