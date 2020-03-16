def percentageOf(value, percent):
    return value * percent / 100

# input
buyingCost = 198.1
investment = 297_151
profit = 3000  # to get 1000 RUB by selling stocks
commission = 0.3  # percentage

stocksAmount = investment // buyingCost
expenses = stocksAmount * buyingCost
buyingCommission = percentageOf(value=expenses, percent=commission)
income = expenses + profit + buyingCommission # we want to sell stocks to get profit and pay over all commissions
sellingCommission = percentageOf(income, commission)
finalStocksCost = income + sellingCommission
finalStockPrice = finalStocksCost / stocksAmount
print(finalStockPrice)

# output
