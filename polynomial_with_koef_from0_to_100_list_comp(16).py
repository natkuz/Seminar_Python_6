# Задана натуральная степень k. 
# Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена 
# и записать в файл многочлен степени k.
# Пример:
# если k = 2, то многочлены могут быть => 2*x² + 4*x + 5 = 0 или x² + 5 = 0 или 10*x² = 0

def random_polynomial_dict(coef_range_min=0, coef_range_max=100):
    import random
    max_power = int(input('Enter max power: '))
    # БЫЛО
    # equation_dict = {}
    # for i in range(max_power, -1, -1):
    #     equation_dict[i] = random.randint(coef_range_min, coef_range_max)

    # СТАЛО
    equation_dict = {i: random.randint(coef_range_min, coef_range_max) for i in range(max_power, -1, -1)}
    return equation_dict


def polynomial_str(equation: dict):
    equation_str = ''
    for k, v in equation.items():
        if v > 1:
            if k == 1:
                equation_str += f'{v} * x + '
            elif k == 0:
                equation_str += f'{v} + '
            else:
                equation_str += f'{v} * x ** {k} + '
        elif v == 1:
            if k == 1:
                equation_str += f'x + '
            elif k == 0:
                equation_str += f'{v} + '
            else:
                equation_str += f'x ** {k} + '
        elif v == 0:
            equation_str += ''
    else:
        equation_str = equation_str[:-3]
    return equation_str


polinom_dict = random_polynomial_dict()
print(f'Degrees and coefficients of a polynomial: {polinom_dict}')
polinom_str = polynomial_str(polinom_dict)

print()

with open('polynomial_with_koef_from0_to_100.txt', 'w') as list_coefficient:
    list_coefficient.write(polinom_str + ' = 0')

with open('polynomial_with_koef_from0_to_100.txt', 'r') as list_coefficient:
    for line in list_coefficient:
        print(line)
