stock1 = 2000
pps = 40
totalprice1 = pps * stock1
comission1 = totalprice1 * 0.03
stock2 = 2000
pps2 = 42.75
totalprice2 = pps2 * stock2
comission2 = totalprice2 * 0.03
profit = totalprice2 - (totalprice1 + comission1 + comission2)

print(f"Amount paid for the stock: ${totalprice1:.2f}")
print(f"Comission paid on the purchase: ${comission1:.2f}")
print(f"Amount the stock sold for: ${totalprice2:.2f}")
print(f"Comission paid on the sale: ${comission2:.2f}")
print(f"Profit (or loss if negative): ${profit:.2f}")
