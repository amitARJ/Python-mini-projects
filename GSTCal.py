CP=float(input("\n\tEnter the Cost of Product: "))
CGST=float(input("\n\tEnter tax % imposed by Center, i.e., CGST: "))
SGST=float(input("\tEnter tax % imposed by State, i.e., SGST: "))
total=0
Amount_CGST =((CGST/100)*CP)
Amount_SGST =((SGST/100)*CP)
total=CP+Amount_CGST+Amount_SGST
print("\n\tTotal Cost of Product : Rs",total)
print("\tTotal Tax : Rs",(total-CP))
