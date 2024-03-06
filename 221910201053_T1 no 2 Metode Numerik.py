import math

# Fungsi untuk menghitung akar kuadrat
akar_kuadrat = math.sqrt

print("Masukkan nilai variabel a")
a = float(input())
print("Masukkan nilai variabel b")
b = float(input())
print("Masukkan nilai variabel c")
c = float(input())

# Menghitung diskriminan
d = b ** 2 - 4 * a * c

# Memeriksa apakah akar real atau imaginer
if d >= 0:
    print("Akar persamaan adalah:")
    # Menghitung akar
    x1 = (-b - akar_kuadrat(d)) / (2 * a)
    x2 = (-b + akar_kuadrat(d)) / (2 * a)
    print("x1 =", x1, "dan x2 =", x2)
else:
    print("Akar persamaan adalah imaginer")
