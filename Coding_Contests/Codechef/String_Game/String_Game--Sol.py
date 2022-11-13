
def result(x) :
    for i,j in x.items() :
        if j%2 != 0:
            return 'NO'
    return 'YES'

for _ in range(int(input())) :
    n = int(input()) 
    instr = input().strip()
    d_ = {} 
    for i in range(0,len(instr)) :
        if instr[i] not in d_ :
            d_[instr[i]] =  1
        else :
            d_[instr[i]] += 1 
    print(result(d_))
        
