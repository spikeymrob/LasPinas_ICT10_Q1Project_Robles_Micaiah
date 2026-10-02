 
from pyscript import display, document

def SKU_generator(e):
    category = document.getElementById('category').value
    product_name = document.getElementById('item').value
    stock_qty = document.getElementById('quantity').value
    sku = category[:3].upper() + "-" + product_name[:4].upper() + "-" + str(stock_qty)
    display("SKU: ", sku, target='sku_number')

def create_order(e):
    # Get input values
    prod1 = document.getElementById("Juturna - Circa Survive")
    prod2 = document.getElementById("U - underscores")
    prod3 = document.getElementById("All We Know Is Falling - Paramore")
    prod4 = document.getElementById("Wallsocket - underscores")
    prod5 = document.getElementById("Frogstomp - Silverchair")
    
    # Calculate total by multiplying value by checked status (1 or 0)
    # Calculate subtotal, tax, and total
    subtotal = (float(prod1.value) * prod1.checked +
                float(prod2.value) * prod2.checked +
                float(prod3.value) * prod3.checked +
                float(prod4.value) * prod4.checked +
                float(prod5.value) * prod5.checked)
    
    tax_rate = 0.12 # 12% VAT, no need for excise tax. too complicated
    tax = subtotal * tax_rate
    total = subtotal + tax
    
    # display(f"==== Receipt ==== \n Subtotal: ₱ {subtotal:.2f} ", target="show")
    # display(f"Subtotal: ₱ {subtotal:.2f} ", target="show")
    # display(f"VAT: ₱ {tax:.2f} ", target="show")
    # display(f"Total: ₱ {total:.2f} ", target="show")
    
    receipt = f"""==== Receipt ====
Subtotal: ₱{subtotal:.2f}
Tax: ₱{tax:.2f}
Total: ₱{total:.2f}"""

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js"></script>