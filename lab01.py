def main():
    cost_per_item = 19.99
    quantity = 5
    tax_rate = 0.13  # tax rate variable to avoid confusion
    
    # Calculate subtotal_cost
    subtotal_cost = cost_per_item * quantity
    
    # Calculate tax on the subtotal_cost
    tax = subtotal_cost * tax_rate
    
    # Calculate total cost (subtotal + tax)
    total_cost = subtotal_cost + tax

    # Print all variables with formatting
    print(f'cost_per_item = ${cost_per_item:0.2f}')
    print(f'quantity = {quantity}')
    print(f'subtotal_cost = ${subtotal_cost:0.2f}')
    print(f'tax = ${tax:0.2f}')
    print(f'total_cost = ${total_cost:0.2f}')

    initial_investment = 1000
    interest_rate = 0.035
    investment = initial_investment

# Apply interest for 5 years
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate
    investment += investment * interest_rate

    print(f'After 5 years, your investment will be worth ' + str((investment)) + ' dollars.')

if __name__ == "__main__":
    main()