import math
ti, al, kel, lu=5 ,12 ,30, 30
sb = math.sqrt(al * al + ti * ti) 
print("Diketahui :")
print("Alas = {} cm " .format(ti)) 
print("Tinggi = {} cm" .format(al)) 
print("")
print("Jawab :")
print("Sisi A = {} cm" .format(al)) 
print("Sisi B = {} cm" .format(round(sb)))
print("Sisi C = {} cm" .format(ti))
print("Keliling = {} cm" .format(kel))
print("Luas = {} cm" .format(lu))