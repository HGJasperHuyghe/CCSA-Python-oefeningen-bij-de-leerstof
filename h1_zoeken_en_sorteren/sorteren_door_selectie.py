def selection_sort_vooraan(a):
    pass

def selection_sort(rij):
    n=len(rij)
    
    for i in range(n-1,0,-1):
        max = rij[i]
        max_pos = i
        for j in range(i-1,-1,-1): # lus om max te zoeken
            if rij[j] > max:
                max = rij[j]
                max_pos = j
            #max achteraan plaatsen
            rij[i], rij[max_pos] = max,rij[i]


a = [int(_) for _ in input().split()]
selection_sort_vooraan(a)

