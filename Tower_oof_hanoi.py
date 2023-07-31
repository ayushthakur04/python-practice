#Tower of hanoi
def toh(n,from_rod,to_rod,aux_rod):
    if n==1:
        
        print("move disk 1 from rod ",from_rod,"to rod ",to_rod)
        return
    else:
        toh(n-1,from_rod,aux_rod,to_rod)
        print ("move disk",n,"from rod ",from_rod,"to rod ",to_rod)
        toh(n-1,aux_rod,to_rod,from_rod)
n=4       
toh(n,'A','C','B')  


move disk 1 from rod  A to rod  B
move disk 2 from rod  A to rod  C
move disk 1 from rod  B to rod  C
move disk 3 from rod  A to rod  B
move disk 1 from rod  C to rod  A
move disk 2 from rod  C to rod  B
move disk 1 from rod  A to rod  B
move disk 4 from rod  A to rod  C
move disk 1 from rod  B to rod  C
move disk 2 from rod  B to rod  A
move disk 1 from rod  C to rod  A
move disk 3 from rod  B to rod  C
move disk 1 from rod  A to rod  B
move disk 2 from rod  A to rod  C
move disk 1 from rod  B to rod  C
​
