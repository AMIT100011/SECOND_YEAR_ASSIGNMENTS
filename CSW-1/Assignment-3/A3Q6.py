def filter_high_sales(sales,threshold):
  for sale in sales:
    if sale >= threshold:
      yield sale

sales = [250, 800, 450, 1200, 600]
threshold = 500
print("Daily Sales:", sales)
print("Threshold:", threshold)
print("High Sales:")
for v in filter_high_sales(sales, threshold):
    print(v)