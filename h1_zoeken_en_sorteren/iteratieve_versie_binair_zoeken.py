

def zoek_binair(rij, getal):
  
  links = 0
  rechts = len(rij)-1
  while links != rechts:
    midden = (links+rechts)//2 # // gehele deling -> dus afronden naar beneden
    if rij[midden] < getal: 
      links = midden +1 # zoeken in rechterhelft
    else:
     rechts = midden # zoeken in linkerhelft ( incl midden)
  #na while: links=rechts: 1 element over
  if rij[links] == getal:
    return links
  else:
    return -1
