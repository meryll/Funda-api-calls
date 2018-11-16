from src import core
from tabulate import tabulate


def print_table(agents):
    header = ['real estate agent', 'occurrences']
    print(tabulate(agents, headers=header, tablefmt='orgtbl'))


def get_with_garden(how_many):
    return core.get(if_garden=True, how_many=how_many)


def get_all(how_many):
    return core.get(if_garden=False, how_many=how_many)


# todo it's always a good idea to add some more unit tests
# add flask api

if __name__ == '__main__':
    agents_all = get_all(how_many=10)
    print("ALL object listed for sale")
    print_table(agents=agents_all)

    print("------------")

    agents_with_garden = get_with_garden(how_many=10)
    print("Object listed for sale with garden")
    print_table(agents=agents_all)
