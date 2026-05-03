from sys import argv


def readlines(input_name):
    with open(input_name) as file:
        return file.readlines()


def writelines(output_name, output_matrix):
    with open(output_name, 'w') as file:
        file.writelines(output_matrix)


def get_matrix(input_list):
    matrix = []
    for line in input_list:
        line_list = line.strip().split(',')

        line_list_float = []
        for char in line_list:
            char = float(char)
            line_list_float.append(char)

        matrix.append(line_list_float)
    return matrix


def aply_vec(matrix, input_vec):
    new_matrix = []
    for row in range(len(matrix)):
        new_row = []
        for colom in range(len(matrix)):
            num = matrix[row][colom] * input_vec[colom][0]
            new_row.append(num)
        new_matrix.append(new_row)

    return new_matrix


def sum_rows(matrix):
    output_vec = []
    for row in matrix:
        total = 0
        for num in row:
            total += num
        output_vec.append(total)

    return output_vec


def print_vec(vector):
    for num in vector:
        num = round(num, 3)
        print(f'{num:>8}')


def send_to_output_csv(output_vec_name, output_vec):
    output_vec_str = []
    for num in output_vec:
        num = str(num) + '\n'
        output_vec_str.append(num)
    writelines(output_vec_name, output_vec_str)


def main(matrix_name, input_vec_name, output_vec_name):
    matrix_file = readlines(matrix_name)
    input_vec_file = readlines(input_vec_name)
    matrix = get_matrix(matrix_file)
    input_vec = get_matrix(input_vec_file)
    matrix = aply_vec(matrix, input_vec)
    output_vec = sum_rows(matrix)
    print_vec(output_vec)
    send_to_output_csv(output_vec_name, output_vec)


if __name__ == '__main__':
    main(argv[1], argv[2], argv[3])
