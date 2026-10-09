berat = float(input("Masukkan berat (kg): "))
tinggi = float(input("Masukkan tinggi (m): "))


bmi = round(berat / tinggi ** 2, 1)

if bmi < 18.5 and bmi != 0:
    status = "UnderWeight"
elif bmi <= 25:
    status = "Normal"
elif bmi <= 30:
    status = "Overweight"
else:
    status = "Obesitas"

print(status)
