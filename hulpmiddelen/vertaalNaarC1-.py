# Dit Python script helpt om Nederlands te vertalen in de c1-taalset.
# Let op: volgens c6-8 mag je alléén in die richting geautomatiseerde hulpmiddelen maken, niet andersom!

invoer = input('Geef de te vertalen tekst:\n')
c1alfabet = ' !"#$%&\'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~€'
c1tekst = '' 
for i in range(len(invoer)):
    j = c1alfabet.find(invoer[i])
    c1tekst += str(j) if j != 0 else '-'
print('\nIn c6-88, taalset c1- is dit:\nc1-{}c-'.format(c1tekst))
