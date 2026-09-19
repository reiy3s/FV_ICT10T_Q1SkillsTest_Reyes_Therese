from pyscript import display, document

def create_order(e):
    document.getElementById("receipt").innerHTML = "" # clears previous output

    prod1 = document.getElementById("item1")
    price1 = float(prod1.value) * prod1.checked

    prod2 = document.getElementById("item2")
    price2 = float(prod2.value) * prod2.checked

    prod3 = document.getElementById("item3")
    price3 = float(prod3.value) * prod3.checked

    prod4 = document.getElementById("item4")
    price4 = float(prod4.value) * prod4.checked

    # Calculate
    subtotal = price1 + price2 + price3 + price4
    tax = subtotal * 0.12
    grandtotal = subtotal + tax

    #display(grandtotal, target="output1")

    display(f'⊹ Receipt ⊹', target = "receipt")
    display(f'Subtotal: Php.{subtotal}!', target = "receipt")
    display(f'Tax: Php.{tax}!', target = "receipt")
    display(f'Your total is Php.{grandtotal}!', target = "receipt")