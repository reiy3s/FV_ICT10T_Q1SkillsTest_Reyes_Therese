from pyscript import display, document

def create_order(e):
    document.getElementById("output2").innerHTML = "" # clears previous output
    prod1 = document.getElementById("item1")
    prod2 = document.getElementById("item2")
    prod3 = document.getElementById("item3")
    prod4 = document.getElementById("item4")

    # Calculate
    subtotal = float(prod1.value) * prod1.checked + float(prod2.value) * prod2.checked + float(prod3.value) * prod3.checked + float(prod4.value) * prod4.checked
    size = document.querySelector('input[name="size"]:checked')
    size_price = float(size.value)
    grandtotal = subtotal + size_price

    #display(grandtotal, target="output1")

def create_order(e):
    document.getElementById("output2").innerHTML = "" # clears previous output
    coffee = document.getElementById("coffee")
    coffee_price = float(coffee.value)
    display(f'Pay {coffee_price}', target = "output2")