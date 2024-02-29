month=int(input("\tEnter a month(1-12): "))
if month<1 or month>12:
    print("\n\tInvalid Input !!!!")
else:
    if month==2:
        year=int(input("\tEnter a year: "))
        if (year%4==0) and (year%100==0) or (year%400==0):
            num_days=29
        else:
            num_days=28
    elif month in (1,3,5,7,8,10,12):
        num_days=31
    else:
        num_days=30
    print("\n\tThere are ",num_days,"days in ",month,"month")