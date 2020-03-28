from math import acos, asin, atan
stop = False
while not stop:
    sign, val = input(
        "Enter:\n\tt -> tan inverse \n\tc -> cos inverse\n\ts -> sin inverse then space followed by the value\n").split()
    if val == "-1":
        stop = True
        continue
    if sign == "t":
        print(f"Tan-1 {float(val)}={atan(float(val))}")
    elif sign == "c":
        print(f"Cos-1 {float(val)}={acos(float(val))}")
    elif sign == "s":
        print(f"Sin-1 {float(val)}={asin(float(val))}")
