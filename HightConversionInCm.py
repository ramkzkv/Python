Hight=float(input("Enter your hight in CMs"))
Conversion=Hight/30.48
Cstr=str(Conversion)
Splt=Cstr.split(".",1)
print("Your Hight is",Splt[0],"Feet",Splt[1],"inches",)
