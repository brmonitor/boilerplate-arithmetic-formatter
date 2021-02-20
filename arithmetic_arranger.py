def vMax5(p): 
    if len(p)>5:
        return True
    else:
        return False

def vAS(o): # only + or -
    #print(set(o))
    if (set(o) | {'+', '-'}) != {'+', '-'}:   # qq coisa diferente de + - causara uma set union diferente
        return True
    else:
        return False

def arithmetic_arranger(problems):

    if vMax5(problems):
        print('Error: Too many problems.')
        return
    
    n1,o,n2 = [],[],[]
    for p in problems:
        ps = p.split()
        n1.append(int(ps[0]))
        o.append(ps[1])
        n2.append(int(ps[2]))

    if vAS(o):
        print("Error: Operator must be '+' or '-'")
        return
        
    print('problems =',problems)
    print('n1 =', n1)
    
    for n in n1:
        print(f'{n:6d}  ',end='')
    print()
    
    l = len(n2)
    for i in range(l):
        print(f' {o[i]}{n2[i]:4d}  ',end='')
    print()
    print( '  ----  '*4)
    print('o  =', o)
    print('n2 =', n2)
    return #arranged_problems

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"])
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49", "523 - 49", "523 - 49"])
arithmetic_arranger(["32 * 8", "1 - 3801", "9999 / 9999", "523 - 49"])
