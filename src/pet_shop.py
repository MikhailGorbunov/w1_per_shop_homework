# WRITE YOUR FUNCTIONS HERE
def get_pet_shop_name(pet_shop):
    # pass
    return pet_shop["name"]

def get_total_cash(pet_shop):
    # pass
    return pet_shop["admin"]["total_cash"]

# def get_total_cash(pet_shop):       
    

    sum = int(pet_shop["admin"]["total_cash"]) + int(10)
    #pet_shop["amount"]
    return sum


def get_total_cash(pet_shop, amount1, amount2):   
    sum = int(pet_shop["admin"]["total_cash"]) - int(10)  #pet_shop["amount"]
    return sum

def get_pets_sold(sell):
    sold = sell["admin"]["pets_sold"]
    return sold 


# def get_pets_sold(sell, increase={2}):
    sold = increase
    return sold 

def get_stock_count(pet_shop):
    count = len(pet_shop["pets"])
    return count

# def get_pets_by_breed(pet_shop, breed):
    pets_by_bread = len(pet_shop["pets"]["breed"])
    return pets_by_bread

