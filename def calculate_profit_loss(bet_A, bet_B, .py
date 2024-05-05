def calculate_profit_loss(bet_A, bet_B, payout_A, payout_B):
    max_profit = 0
    max_loss = 0
    cashout_amount = 0
    max_profit_scenario = ""
    max_loss_scenario = ""

    # Scenario 1: Both hit six and A wins
    profit_scenario_1 = payout_A + 2000 - bet_A - bet_B
    if profit_scenario_1 > max_profit:
        max_profit = profit_scenario_1
        max_profit_scenario = "Both hit six and A wins"
    max_loss = min(max_loss, 0)

    # Scenario 2: Both hit six and B wins
    profit_scenario_2 = payout_B + 2000 - bet_A - bet_B
    if profit_scenario_2 > max_profit:
        max_profit = profit_scenario_2
        max_profit_scenario = "Both hit six and B wins"
    max_loss = min(max_loss, 0)

    # Scenario 3: Only A hits six and A wins
    profit_scenario_3 = payout_A - bet_A - bet_B
    if profit_scenario_3 > max_profit:
        max_profit = profit_scenario_3
        max_profit_scenario = "Only A hits six and A wins"
    max_loss = min(max_loss, 0)

    # Scenario 4: Only A hits six and B wins
    profit_scenario_4 = payout_B - bet_A - bet_B
    if profit_scenario_4 > max_profit:
        max_profit = profit_scenario_4
        max_profit_scenario = "Only A hits six and B wins"
    if profit_scenario_4 < max_loss:
        max_loss = profit_scenario_4
        max_loss_scenario = "Only A hits six and B wins"
    
    # Scenario 5: Only B hits six and B wins
    profit_scenario_5 = payout_B - bet_A - bet_B
    if profit_scenario_5 > max_profit:
        max_profit = profit_scenario_5
        max_profit_scenario = "Only B hits six and B wins"
    max_loss = min(max_loss, 0)

    # Scenario 6: Only B hits six and A wins
    profit_scenario_6 = payout_A + 2000 - bet_A - bet_B
    if profit_scenario_6 > max_profit:
        max_profit = profit_scenario_6
        max_profit_scenario = "Only B hits six and A wins"
    max_loss = min(max_loss, 0)

    # Scenario 7: No one hits six and A wins
    profit_scenario_7 = payout_A - bet_A - bet_B
    if profit_scenario_7 > max_profit:
        max_profit = profit_scenario_7
        max_profit_scenario = "Neither team hits six and A wins"
    max_loss = min(max_loss, 0)

    # Scenario 8: No one hits six and B wins
    profit_scenario_8 = payout_B - bet_A - bet_B
    if profit_scenario_8 > max_profit:
        max_profit = profit_scenario_8
        max_profit_scenario = "Neither team hits six and B wins"
    if profit_scenario_8 < max_loss:
        max_loss = profit_scenario_8
        max_loss_scenario = "Neither team hits six and B wins"

    # Calculate cashout amount for minimum loss
    cashout_amount = bet_A + bet_B

    return max_profit, max_loss, cashout_amount, max_profit_scenario, max_loss_scenario


# Input parameters
bet_A = float(input("Enter betting amount for Team A: "))
bet_B = float(input("Enter betting amount for Team B: "))
payout_A = float(input("Enter estimated payout for Team A: "))
payout_B = float(input("Enter estimated payout for Team B: "))

# Calculate maximum profit, maximum loss, and cashout amount
max_profit, max_loss, cashout_amount, max_profit_scenario, max_loss_scenario = calculate_profit_loss(bet_A, bet_B, payout_A, payout_B)

print("Maximum Profit:", max_profit)
print("Maximum Loss:", max_loss)
print("Cashout Amount to Minimize Loss:", cashout_amount)
print("Scenario for Maximum Profit:", max_profit_scenario)
print("Scenario for Maximum Loss:", max_loss_scenario)
