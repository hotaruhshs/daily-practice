def order_pizza(size="medium", crust="thin", toppings=None):
    if toppings is None:
        toppings = []
    print(f"You ordered a {size} {crust}-crust pizza with {', '.join(toppings) or 'no toppings'}.")

order_pizza()  # all defaults
order_pizza(size="large", toppings=["pepperoni", "mushrooms"])
order_pizza(toppings=["cheese"], crust="stuffed")
