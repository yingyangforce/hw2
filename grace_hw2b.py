# +---------------------+
# | hw2b - Isaiah Grace |
# +---------------------+

# Part b - tax adder

def addTaxes(price):
    their_cut = 0.045
    true_cost = float(price) + (float(price) * their_cut)
    return true_cost

buy_1 = addTaxes(input("Cost of first purchase: "))
buy_2 = addTaxes(input("Cost of second purchase: "))
buy_3 = addTaxes(input("Cost of third purchase: "))

print(f"Total purchase cost: {buy_1 + buy_2 + buy_3}")
