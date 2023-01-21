# Даны два файла, в каждом из которых находится запись многочлена. 
# Задача - сформировать файл, содержащий сумму многочленов.

def create_equation_dict(equation: str):
    nq = equation.replace(' ', '').replace('=0', '').replace('+', ' '). \
        replace('-', ' -').split()
    equation_dict = {}
    for item in nq:
        if item.startswith('x') or item.startswith('-x'):
            equation_dict[int(item[-1])] = 1
        elif item.endswith('x'):
            equation_dict[1] = int(item.split('*x')[0])
        elif item.isdigit():
            equation_dict[0] = int(item)
        else:
            equation_dict[int(item[-1])] = int(item.split('*x')[0])
    return equation_dict


def sum_polynomial_dict(equation1: dict, equation2: dict):
    equation_sum = {}
    for k in equation1.keys():
        for key in equation2.keys():
            if not key in equation1.keys():
                equation_sum[key] = equation2.get(key)
            elif not k in equation2.keys():
                equation_sum[k] = equation1.get(k)
            else:
                equation_sum[k] = equation1.get(k, 0) + equation2.get(k, 0)

    equation_sum_list = list(equation_sum.items())

    # БЫЛО
    # index_tuple = 0
    # for i in range(0, len(equation_sum_list)):
    #     for j in range(0, len(equation_sum_list) - i - 1):
    #         if equation_sum_list[j][index_tuple] < equation_sum_list[j + 1][index_tuple]:
    #             equation_sum_list[j], equation_sum_list[j + 1] = equation_sum_list[j + 1], equation_sum_list[j]
    #
    # sorted_equation_sum = dict(equation_sum_list)

    # СТАЛО
    sorted_equation_sum = dict(sorted(equation_sum_list, key=lambda x: x[0], reverse=True))

    return sorted_equation_sum


def polynomial_list(equation: dict):
    eq_str = ''
    for k, v in equation.items():
        if v > 1:
            if k == 1:
                eq_str += f'{v}*x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'{v}*x**{k}+'
        elif v == 1:
            if k == 1:
                eq_str += f'x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'x**{k}+'
        elif v == 0:
            eq_str += ''
        elif v == - 1:
            if k == 1:
                eq_str += f'-x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'-x**{k}+'
        else:
            if k == 1:
                eq_str += f'{v}*x+'
            elif k == 0:
                eq_str += f'{v}+'
            else:
                eq_str += f'{v}*x**{k}+'
    else:
        eq_str = eq_str[:-1]

    equation_dict = eq_str.replace('+', ' ').replace('-', ' -').split()
    return equation_dict


def polynomial_str(equation: list):
    equation_new = []
    for item in equation:
        if item == equation[0]:
            equation_new.append(item)
        elif item.startswith('-'):
            equation_new.append(item)
        else:
            equation_new.append('+')
            equation_new.append(item)
    equation_new = ''.join(equation_new)
    return equation_new


with open('polynomial1.txt', 'r') as equation1:
    equation1 = ''.join(equation1)
    print(f'Equation1: {equation1}')
    equation_dict1 = create_equation_dict(equation1)

print()

with open('polynomial2.txt', 'r') as equation2:
    equation2 = ''.join(equation2)
    print(f'Equation2: {equation2}')
    equation_dict2 = create_equation_dict(equation2)

print()

polynomial_sum_dict = sum_polynomial_dict(equation_dict1, equation_dict2)
polynomial_sum_list = polynomial_list(polynomial_sum_dict)

with open('sum_polynomial.txt', 'w') as sum_polynomial:
    sum_polynomial.write(polynomial_str(polynomial_sum_list) + '=0')

with open('sum_polynomial.txt', 'r') as sum_polynomial:
    for line in sum_polynomial:
        print(f'Sum of equations: {line}')
