 def ss2(nlist):
    nlist.remove(min(nlist))
    x = sum(i**2 for i in nlist)
    return x
    
