N = int(input("N = "))

print(f"Введіть елементи масиву кількістью {N}:")

arr = [int(input()) for _ in range(N)]

print("Введений масив: ", arr)
sumParni = 0
for i in range(0,N,2):
  sumParni+=arr[i]
print("Сума елементів масиву з парними індексами" , sumParni)