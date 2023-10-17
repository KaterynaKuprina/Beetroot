class Mathematician:
    def square_nums(self, new_list):
        return [i**2 for i in new_list]

    def remove_positives(self, second_list):
        return [i for i in second_list if i < 0]

    def filter_leaps(self, leap_year):
        return [i for i in leap_year if i % 4 == 0]


m = Mathematician()

print(m.square_nums([7, 11, 5, 4]))

print(m.remove_positives([26, -11, -8, 13, -90]))

print(m.filter_leaps([2001, 1884, 1995, 2003, 2020]))