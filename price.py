price = float(input("Enter the price: "))
category = float(input("Enter the category(Food.1/Goods.2/snacks.3): "))
if category == "Food":
   gst = price * 0.05
elif category == "Goods":
   gst = price * 0.18
elif category == "Snacks":
   gst = price * 0.12
else:
    print("Invalid category")
    gst = 0

net_price = price + gst
print("GST:", gst)
print("Net price:", net_price)
