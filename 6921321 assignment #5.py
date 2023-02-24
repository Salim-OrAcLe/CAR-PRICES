Salim-OrAcLe
#Script for car prices
#prices of cars are in US dollars
# Script for car prices
# Prices of cars are in US dollars
car_prices = {
    'cheverolet': 43500,
    'lamborghini': 16000,
    'ford': 32000,
    'tesla': 86700,
    'kia': 150400,
    'posche': 58000,
    'honda': 105000,
    'cadillac': 33500,
    'alphaRomeo': 120000,
    'hyundai': 77000,
    'mazda': 910000,
    'nissan': 14300,
    'mini': 42000,
    'maserati': 35400,
    'bmw': 56000,
    'toyota': 25000,
    'landRover': 67000,
    'mitsubishi': 70000,
    'buick': 92000,
    'porche': 83500,
    'audi': 13000,
    'chevrolet': 56000,
    'rangeRover': 2000,
    'bugatti': 39000,
    'rollsRoyce': 9000,
    'volkswagen': 89000,
    'jaguar': 53000,
    'pagani': 50000,
    'astonMartin': 30000,
    'ferrari': 175000
}

car_brand = input('Enter car brand: ').lower()

if car_brand in car_prices:
    print(f"The price of {car_brand} is ${car_prices[car_brand]:,}")
else:
    print(f"Sorry, {car_brand} is not in our list.")
