import ijson
from classes import Pizza
from currrency_format import format_money

def fetch_pizzas():
    pizza_url: str = 'pizzas.json'
    mode: str = 'rb'
    # with open(pizza_url, mode=mode) as f:
    #     for i in ijson.items(f, ''):
    #         print(i['pizzas'])


    pizza_list: list[Pizza] = []
    with open(pizza_url, mode=mode) as f:
        for pizzas in ijson.items(f, 'pizzas'):
            for pizza in pizzas:
                p = Pizza(**pizza)
                pizza_list.append(p)
    return pizza_list


def main():
    pizzas: list[Pizza] = fetch_pizzas()
    for pizza in pizzas:
        print(f'Pizza {pizza.name}, ({format_money(pizza.price)})')


if __name__ == '__main__':
    main()
