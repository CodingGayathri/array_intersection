arr1=[1,45,3,67,89,46,3,4,66,7,4,]
arr2=[1,66,4,67,46,45,89]
arr1_sorted=sorted (arr1)
arr2_sorted=sorted(arr2)
print(arr1_sorted, arr2_sorted)
i,j=0,0
intersection=[]

while i < len(arr1_sorted) and j < len(arr2_sorted):
    if arr1_sorted[i]==arr2_sorted[j]:
        intersection.append(arr1_sorted[i])
        i+=1
        j+=1
    elif arr1_sorted[i]<arr2_sorted[j]:
        i+=1
    else:
        j+=1
print(f"intersection elemts in both arr1 and arr2 are {intersection} ")