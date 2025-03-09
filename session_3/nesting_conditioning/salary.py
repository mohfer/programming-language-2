permanent_salary = 1000000
honorary_salary = 750000

permanent_bonus_a = 200000
permanent_bonus_b = 400000
permanent_bonus_c = 550000

honorary_bonus_a = 150000
honorary_bonus_b = 275000
honorary_bonus_c = 480000

name = input("Masukkan nama: ")
nik = input("Masukkan NIK: ")
status = input("Masukkan status pegawai (Tetap/Honorer): ").lower()
group = input("Masukkan golongan (A/B/C): ").lower()

if status == "tetap":
    salary = permanent_salary
    if group == "a":
        bonus = permanent_bonus_a
    elif group == "b":
        bonus = permanent_bonus_b
    elif group == "c":
        bonus = permanent_bonus_c
    else:
        print("Golongan tidak valid!")
        exit()
elif status == "honorer":
    salary = honorary_salary
    if group == "a":
        bonus = honorary_bonus_a
    elif group == "b":
        bonus = honorary_bonus_b
    elif group == "c":
        bonus = honorary_bonus_c
    else:
        print("Golongan tidak valid!")
        exit()
else:
    print("Status pegawai tidak valid!")
    exit()

print(f"\nNama: {name}")
print(f"NIK: {nik}")
print(f"Status pegawai: {status}")
print(f"Golongan: {group}")
print(f"Gaji: Rp {salary:,}")
print(f"Bonus: Rp {bonus:,}")
print(f"Total: Rp {salary + bonus:,}")
