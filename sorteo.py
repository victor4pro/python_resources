# -*- coding: utf-8 -*-
import random


def assign_random_number_to_list(list_of_names):
    if list_of_names:
        """
        This function takes a list of names as input and returns a list of lists,
        each containing a name and a randomly assigned number.
        If the input list is empty, it prints a #message indicating that no list of names has been provided.
        """
        range_of_list = len(list_of_names)
        new_list = []
        test_list = list(range(1, range_of_list + 1))
        repeated_numbers = []
        for name in list_of_names:
            num1 = random.choice([ele for ele in test_list if ele not in repeated_numbers])
            new_list.append([name, num1])
            repeated_numbers.append(num1)
        return sorted(new_list, key=lambda x: x[1])
    else:
        print("No se ha proporcionado ninguna lista de nombres")


if __name__ == '__main__':
    list_of_names = ["Frodo Bolsón", "Harry Potter", "Luke Skywalker",
                     "Katniss Everdeen", "Sherlock Holmes", "Darth Vader", "Hermione Granger"]
    result = assign_random_number_to_list(list_of_names)
    for name in result:
        print(name)
