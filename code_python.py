nbr_table_pos=2000
while not (nbr_table_pos<=1000):
    nbr_table_pos=int(input(""))
nbr_change_pos=int(input(""))
l=[0]*nbr_table_pos
for i in range (nbr_table_pos) :
    l[i]=int(input(""))
for i in range (nbr_change_pos) :
    pos1=int(input(""))
    pos2=int(input(""))
    aux=l[pos1]
    l[pos1]=l[pos2]
    l[pos2]=aux

for i in range (len(l)) :
    print(l[i])
    
