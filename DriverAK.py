from ProgramExerciseAK import shopping


def items():
    items_list = []

    user_input_amount = int(input("How many items do you want to order?: "))

    while user_input_amount < 1:    
        print("Please input a valid amount.")

        user_input_amount =  int(input("How many items do you want to order?: "))

    for i in range(user_input_amount):
        user_input_food = str(input("Enter the food: "))
        user_input_pounds = int(input("Please input the amount in pounds: "))
        while user_input_pounds < 1:    
            print("Please input a valid amount.")
            user_input_pounds =  int(input("Please input the amount in pounds: "))
        
        food_items = shopping(user_input_food, user_input_pounds)
        items_list.append(food_items)
    
    return items_list

def display_list(food_list):
    print("Items Purchased")
    print("------")
    for food_items in food_list:
        print(food_items)
        
def main():
    myitems_list = items()
    display_list(myitems_list)

main()
    