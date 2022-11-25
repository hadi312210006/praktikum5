stop = False
i = 0
list= []
while(not stop):

    nama = input("Masukan Nama :")
    nim = input("Masukan Nim :")
    tugas = int(input("Nilai Tugas : "))
    uts = int(input("Nilai UTS : "))
    uas = int(input("Nilai UAS : "))
    nilaiakhir = float(tugas)*30/100+(uts)*35/100+(uas)*35/100
    list.append([nama,nim,tugas,uts,uas,nilaiakhir])


    i+= 1
    tanya = input("Masukan lagi (y/t) : ")
    if(tanya == "t"):
        stop = True

print("====================================================================================");        
print("|  No  |     Nama     |     Nim       |  Tugas  |   UTS   |   UAS   |  Nilai Akhir |");
print("====================================================================================");
i=0
for x in list:
    i+=1
    print("|  {6:2}  |  {0:10}  |   {1:9}   |  {2:7} |  {3:5}  |{4:6} |  {5:11.2f}  |"\
        .format (x[0][:9] , x[1][:9],x[2],x[3],x[4],x[5], i))
print("====================================================================================");

