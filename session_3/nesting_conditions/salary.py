permanent_employee_salary = 1000000
honorary_employee_salary = 750000

bonus_permanent_employee_group_a = 200000
bonus_permanent_employee_group_b = 400000
bonus_permanent_employee_group_c = 550000

bonus_honorary_employee_group_a = 150000
bonus_honorary_employee_group_b = 275000
bonus_honorary_employee_group_c = 480000

name = input("Masukkan nama: ")
nik = input("Masukkan NIK: ")

while True:
    status = input("Masukkan status pegawai (Tetap/Honorer): ").lower()
    if status in ["tetap", "honorer"]:
        break
    print("Status tidak valid. Harap masukkan 'Tetap' atau 'Honorer'.")

if status == "tetap":
    salary = permanent_employee_salary
else:
    salary = honorary_employee_salary

while True:
    group = input("Masukkan golongan (A/B/C): ").lower()
    if group in ["a", "b", "c"]:
        break
    print("Golongan tidak valid. Harap masukkan 'A', 'B', atau 'C'.")

if status == "tetap":
    if group == "a":
        bonus = bonus_permanent_employee_group_a
    elif group == "b":
        bonus = bonus_permanent_employee_group_b
    elif group == "c":
        bonus = bonus_permanent_employee_group_c
else:
    if group == "a":
        bonus = bonus_honorary_employee_group_a
    elif group == "b":
        bonus = bonus_honorary_employee_group_b
    elif group == "c":
        bonus = bonus_honorary_employee_group_c

print(f"\nNama: {name}")
print(f"NIK: {nik}")
print(f"Status pegawai: {status}")
print(f"Golongan: {group}")
print(f"Gaji: Rp {salary:,}")
print(f"Bonus: Rp {bonus:,}")
print(f"Total: Rp {salary + bonus:,}")
