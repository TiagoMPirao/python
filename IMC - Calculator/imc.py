height = float(input("Altura:"))
weight = int(input("Peso:"))

imcTotal = (weight / (height * height))
print(imcTotal)

if (imcTotal < 22):
    print("Your IMC is " + str(imcTotal) + " you are underweight ")
elif (imcTotal >= 22 <= 28):
    print("Your IMC is " + str(imcTotal) + " you are normal weight ")
elif (imcTotal >= 29 <= 32):
    print("Your IMC is " + str(imcTotal) + " you are slightly overweight ") 
elif (imcTotal >= 33 <= 37):
    print("Your IMC is " + str(imcTotal) + " you are obese ")
elif (imcTotal >38):   
    print("Your IMC is " + str(imcTotal) + " you are clinially obese ")
     