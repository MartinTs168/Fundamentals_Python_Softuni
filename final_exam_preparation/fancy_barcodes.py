import re

pattern = r"@#{1,}([A-Z][a-z0-9A-Z]{4,}[A-Z])@#{1,}"
num_barcodes = int(input())
for _ in range(num_barcodes):
    product_group = ""
    current_barcode = input()
    match = re.findall(pattern, current_barcode)
    if match:
        for character in current_barcode:
            if character.isdigit():
                product_group += character
        if product_group == "":
            product_group = "00"
        print(f"Product group: {product_group}")
    else:
        print("Invalid barcode")