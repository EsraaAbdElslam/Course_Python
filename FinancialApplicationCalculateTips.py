subtotal, gratuity_rate = eval(input("Enter the subtotal and a gratuity rate: "))
gratuity =(subtotal / 100) * 15
total = subtotal + gratuity
print("The gratuity is ", format(gratuity, ".2f"), " and the total is ", format(total, ".2f"))
