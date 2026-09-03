items = []

while True:

    print("\n-------------SHOPPING BILL----------------")

    name = input("Enter item name :")

    price = float(input("Enter item price :"))

    quantity = int(input("Enter quantity :"))

    total = price * quantity

    item = {
        "name":name,
        "price":price,
        "quantity":quantity,
        "total":total,
    }

    items.append(item)

    print("ITEMS ADD SUCCESSFULLY ")

    again = input("add another item? (yes/no): ")

    if again.lower() == "no":
        break

grand_total = 0

print("\n-------------BILL------------------")

for i, item in enumerate(items,1):

    print(f"{i}. {item["name"]} : ₹{item["price"]} x {item["quantity"]} = ₹{item["total"]}")

    grand_total = grand_total + item["total"]

print("="*40)
print("Grand total: ₹", grand_total)
print("="*40)
print("thank you for shopping")