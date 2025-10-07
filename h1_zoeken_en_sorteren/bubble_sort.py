def bubble_sort(a):
    n = len(a)
    # buitenste lus: elke iteratie zorgt ervoor dat het grootste element 'naar boven komt'
    for i in range(n - 1):
        # binnenste lus: vergelijkt telkens aangrenzende elementen
        for j in range(n - 1, i, -1):
            if a[j - 1] > a[j]:
                # wissel de twee elementen van plaats
                a[j - 1], a[j] = a[j], a[j - 1]


a = [int(x) for x in input().split()]
bubble_sort(a)
print(a)
