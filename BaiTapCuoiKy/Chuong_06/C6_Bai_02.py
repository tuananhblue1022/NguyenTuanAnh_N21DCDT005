array=int(input("Nhap N: "))
arrayA=[]
for i in range(array):
   arrayA.append(int(input(" Nhap A[%d]= "%i)))
print("Mang A: ", arrayA)
array=int(input("Nhap N: "))
arrayB=[]
for i in range(array):
   arrayB.append(int(input(" Nhap B[%d]= "%i)))
print("Mang B: ", arrayB)
arrayC = [x for x in arrayA if x not in arrayB]
arrayC.sort()
print("Mang C: ", arrayC)
