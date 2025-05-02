code_List = []
price_list = []
integer_List = []


def menu_option():
    print("-----MENU-----")
    print("1. Add Stock Code")
    print("2. Add Stock Item")
    print("3. Display Stock List")
    print("4. Exit")


def add_stock_code():
    if len(code_List) >= 50:
        print("You can't add more stock codes")
        return

    code = input("Enter a stock code: ").strip()
    if code in code_List:
        print("Stock code already exists.")
        return

    try:
        price = float(input("Enter stock price: "))
        if price > 1000.00:
            print("Item price is not advised as it exceeds the limit.")
            return
    except ValueError:
        print("That is an invalid price")
        return

    code_List.append(code)
    price_list.append(price)
    integer_List.append(0)
    print(f"Stock code '{code}' added successfully.")


def search_code(search):
    for pos in range(len(code_List)):
        current_code = code_List[pos]
        if current_code == search:
            print("The code was not found")
            return pos


def add_stock_item():
    code = input("Enter a stock code to add stock to: ").strip()
    loc = search_code(code)

    if loc == -1:
        return

    try:
        item = int(input("How many items do you want to add? "))
        if integer_List[loc] + item > 100:
            print("Cannot exceed the advised 100 items for this stock.")
            return
        integer_List[loc] += item
        print(f"Added {item} items to '{code}'.")
    except ValueError:
        print("Invalid item..")


def display_stock_list():
    print("Stock code, In stock, Price, Stock value")
    total_value = 0
    for i in range(len(code_List)):
        code = code_List[i]
        item = integer_List[i]
        price = price_list[i]
        value = item * price
        total_value += value
        print(f"{code}, {item}, {price:.2f}, {value:.2f}")
    print(f"Total,,, {total_value:.2f}")


while True:
    menu_option()
    try:
        choice = int(input("Enter a choice: "))
    except ValueError:
        print("Please enter a valid choice.")
        continue

    if choice == 1:
        add_stock_code()
    elif choice == 2:
        add_stock_item()
    elif choice == 3:
        display_stock_list()
    elif choice == 4:
        print("Exiting the system.")
        break
    else:
        print("Invalid choice. Please select from 1 to 4.")

if __name__ == "__main__":
    menu_option()
