import pandas as pd  


PS4_sales = pd.read_csv("/Users/specky3512/GitHub/Project 1/Game sales files/PS4_sales.txt", delimiter=',')
Xbox_one_sales = pd.read_csv("/Users/specky3512/GitHub/Project 1/Game sales files/xbox_one_sales.txt", delimiter=',')


PS4_sales.to_csv("/Users/specky3512/GitHub/Project 1/Game sales files/PS4 Sales.csv", index=None)
Xbox_one_sales.to_csv("/Users/specky3512/GitHub/Project 1/Game sales files/Xbox One Sales.csv", index=None)
