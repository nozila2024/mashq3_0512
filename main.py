#1-misol
narx = float(input("Narx kirit: "))
tolov = float(input("To'lov kirit: "))

if tolov < 0 and narx < 0:
    print("xatolik!!!")
elif tolov >= narx:
    print(f"Qaytim: {tolov - narx}")
elif tolov < narx:
    print(f"Yetishmaydi: {narx - tolov}")
