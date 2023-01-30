##Azeez Olapade
##CS175L
##stocks

NUM_SHARES = 2000
PURCHASE_PRICE = 40
amountPaidForStock = PURCHASE_PRICE * NUM_SHARES
purchaseCommission = amountPaidForStock * 0.03
SELLING_PRICE = 42.75
stockSoldFor = SELLING_PRICE * NUM_SHARES
sellingCommission = stockSoldFor * 0.03
profitOrLoss = stockSoldFor - (amountPaidForStock + purchaseCommission + sellingCommission)

print(f"Amount paid for the stock: ${PURCHASE_PRICE:.2f}")
print(f"Commission paid on the purchase: ${purchaseCommission:.2f}")
print(f"Amount the stock sold for: ${SELLING_PRICE:.2f}")
print(f"Commission paid on the sale: ${sellingCommission:.2f}")
print(f"Profit (or loss if negative): ${profitOrLoss:.2f}")
