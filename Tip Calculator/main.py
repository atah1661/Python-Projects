food_amount = float(input("Enter food amount $: "))
tip_percentage = float(input("Tip Percentage (1 - 100): ")) / 100

tip_amount = food_amount * tip_percentage
total_amount = food_amount + tip_amount

print("___________________________________")
print(f"Food Amount: ${food_amount} ")
print(f"Tip Amount: ${tip_amount} \n")
print(f"Total Amount: ${total_amount}")
print("___________________________________")
