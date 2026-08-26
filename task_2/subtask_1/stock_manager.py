def load_stock():
    stock = {}
    try:
       with open("stock.txt", "r") as file:
         for line in file:
            try:
             parts=line.strip().split(",")
             item = parts[0]
             quan = int (parts[1])
             stock[item]=quan
            except (IndexError,ValueError):
               print("Skipping corrupted line: " , line.strip())
    except FileNotFoundError:
       print("stock.txt not found.starting with an empty stock")        
    return stock


def add_stock(stock):
    show_stock(stock)
    user_input = input("Enter the stock name or id (or a new name to add): ")
    item = resolve_item(stock, user_input)
    if item is None:
        print("Invalid id.")
        return
    try:   
        amount_entered = int (input("enter the amount of item:"))
        if amount_entered < 1:
            print("amount can not be negative")
            return
    except (ValueError): 
        print("enter a valid number")       
        return 
    if item in stock:
        quan=amount_entered+stock[item]
    else: 
        quan=amount_entered    
    stock[item]=quan    
    
    
def resolve_item(stock, user_input):
    if user_input.isdigit():
        index = int(user_input) - 1
        names = list(stock.keys())
        if index>=0 and index<len(names):
            return names[index]
        else :
            return None            
    else:
        return user_input.lower()
    
    

def show_stock(stock):
    for i, (item,quan) in enumerate (stock.items(),start=1):
        print(f"{i}.{item}:{quan}")  
        
                
def remove_stock(stock):
    show_stock(stock)
    user_input = input("Enter the stock name or id: ")
    item = resolve_item(stock, user_input)
    if item not in stock:
        print("Item is not in stock")
        return
    try:
        amount_entered = int (input("enter the amount of item:")) 
    except:
        print("Enter a valid number")
        return
    if  stock[item]-amount_entered<0:
        print("Not enough stock to remove this amount")
        return   
    stock[item]=stock[item]-amount_entered
    
def save_stock(stock):
    with open("stock.txt", "w") as file:
        for item, quan in stock.items():
            file.write(f"{item},{quan}\n")    
            
            
def main(): 
    stock=load_stock()
    while True:
        print("enter 1 to add stock")
        print("enter 2 to remove stock")
        print("enter 3 to show the stock's contents")
        print("enter 4 to exit the program")
        try:   
         choice = int (input("enter your choice:"))
         if choice == 1:
             add_stock(stock)
         elif choice == 2:
            remove_stock(stock)
         elif choice == 3:
            show_stock(stock)
         elif choice == 4:
            save_stock(stock)
            break
         else :  
             print("The input is not valid Enter a number from 1-4") 
        except (ValueError): print("enter a valid choice:")
main()