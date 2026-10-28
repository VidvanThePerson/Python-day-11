import time
def calculate_change(paid, price):
    change = paid - price
    return change
snack_price = 25
print("Snack Vending Machine")
print(f"The snack costs ${snack_price}")
print("Accepted coins: 1,5,10,25\n")
total_inserted = 0
coins_inserted = 0
while True:
    coin = int(input("Insert a coin:1,5,10 or 25:"))
    if coin not in(1,5,10,25):
        print("Invalid coin. try again")
        continue
    total_inserted += coin
    coins_inserted += 1
    print(f"Inserted {coin}. Total so far:{total_inserted}\n")
    if total_inserted >=snack_price:
        time.sleep(1)
        print("Enough money inserted!")
        break
change_due = calculate_change(total_inserted, snack_price)
print("Dispensing your snack...")
time.sleep(1)
if change_due == 0:
    pass
else:
    time.sleep(1)
    print(f"Here is your change: ${change_due}")
time.sleep(1)
print("========================Purchase Summary========================")
time.sleep(1)
print(f"Snack price:{snack_price}")
time.sleep(1)
print(f"Coins inserted:{coins_inserted}")
time.sleep(1)
print(f"Total paid:{total_inserted}")
time.sleep(1)
print(f"Change given:{change_due}")
print("=====================================")
print("Thanks for your purchase!")