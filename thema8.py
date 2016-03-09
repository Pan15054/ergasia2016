f=open('pinakas.txt','r')
list1=f.readlines()
space=' '
pinakas=[[space for x in range(0,8)] for x in range(0,8)]
y='0'
k=0
for i in range(0,8):
    for j in range(0,41):
        if list1[i][j]==y:
            pinakas[i].pop(k)           #αλγοριθμος ο οποιος θα αποθηκευση τον πινακα που περνει 
            pinakas[i].insert(k,y)      #απο το αρχειο
            k+=1
        elif j==40:
            k=0
        elif list1[i][j]==space and list1[i][j-1]=="'":
            k+=1
for i in range(0,8):
    print pinakas[i]
def rotations(pinakas,degree,W):
    j=degree/90
    W[j]=zip(*pinakas[::-1]) #η συναρτηση η οποια θα κανει τον πινακα να περισταφει
    while j!=0:              #αναλογα με το συνολο των μοιρων που θελουμε
        for i in W[j]:
            print i
        j=j-1
        W[j]=zip(*W[j+1][::-1])
W={"1":1,"2":2,"3":3}
rotations(pinakas,270,W)
