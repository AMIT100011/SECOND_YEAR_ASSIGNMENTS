def generate_bill(item,price,quantity=1,discount=0,tax_rate=0.05):
  subtotal = price * quantity
  disc_amt = subtotal * discount/100
  disc_total = subtotal - disc_amt

  tax_amt = disc_total * tax_rate
  final_total = disc_total + tax_amt

  print("----- BILL SUMMARY -----")
  print(f"Item Name   : {item}")
  print(f"Quantity    : {quantity}")
  print(f"Price/Item  : ₹{price}")
  print(f"Discount    : {discount}% (-₹{disc_amt:.2f})")
  print(f"Tax Rate    : {tax_rate*100}% (+₹{tax_amt:.2f})")
  print(f"Total Bill  : ₹{final_total:.2f}")
  print("------------------------\n")

generate_bill("Laptop",50000)

generate_bill("Pen",50,2)

generate_bill("Headphones", 2000, discount=10, tax_rate=0.12)
generate_bill("PC", 50000, 2, 10, 0.05)

