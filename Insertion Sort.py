def insertionsort (arr):
  for i in range (1, len(arr)):
    key = arr[i]
    j = i-1 
    while j>=0 and key < arr[j]:
          arr[j+ 1] = arr[j] 
          j= j-1 
    arr[j+1] = key

arr = [5, 2, 3, 4, 1]
insertionsort(arr)
for i in range (len(arr)):
    print("% d" % arr [i])
