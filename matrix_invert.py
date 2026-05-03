import sys


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


def get_unit(num):
    unit_matrix = []
    for row in range(num):
        line = []
        for colum in range(num):
            if row == colum:
                line.append(1.0)
            else:
                line.append(0.0)
        unit_matrix.append(line)
    return unit_matrix


def rowop(matrix, row_dep_num, row_ind_num,
          scail):  # rowop(row that is changing, other row, skail) = new matrix with oparation (assumes float input)
    new_matrix = []
    new_line = []
    row_dep = matrix[row_dep_num]
    row_ind = matrix[row_ind_num]
    for i in range(len(row_dep)):
        new_line.append(row_dep[i] + scail * row_ind[i])

    for row in range(len(matrix)):
        if row == row_dep_num:
            new_matrix.append(new_line)
        else:
            new_matrix.append(matrix[row])

    return new_matrix


def rowscail(matrix, row_num, scail):
    new_matrix = []
    new_row = []
    row_list = matrix[row_num]
    for num in row_list:
        num *= scail
        new_row.append(num)

    for row in range(len(matrix)):
        if row == row_num:
            new_matrix.append(new_row)
        else:
            new_matrix.append(matrix[row])

    return new_matrix


def make_pivet_non_zero(input_matrix, rec_matrix, row):
    for i in range(len(input_matrix) - (row + 1)):
        new_matrix = rowop(input_matrix, row, row + (i + 1), 1)
        new_rec_matrix = rowop(rec_matrix, row, row + (i + 1), 1)
        if new_matrix[row][row] != 0.0:
            return new_matrix, new_rec_matrix
    sys.exit('The matrix can not be inverted')


def row_esh(matrix, unit_matrix):
    rec_matrix = unit_matrix
    for row in range(len(matrix)):
        for i in range(len(matrix) - (row + 1)):
            if matrix[row][row] == 0.0:
                matrix, rec_matrix = make_pivet_non_zero(matrix, rec_matrix, row)
            scail = - (matrix[row + (i + 1)][row] / matrix[row][row])
            matrix = rowop(matrix, row + (i + 1), row, scail)
            rec_matrix = rowop(rec_matrix, row + (i + 1), row, scail)

    if matrix[row][row] == 0.0:
        sys.exit('The matrix can not be inverted')
    else:
        return matrix, rec_matrix


def reduced_row_esh(matrix, rec_matrix):
    for row in range(1, len(matrix)):
        for i in range(row):
            scail = - (matrix[i][row] / matrix[row][row])
            matrix = rowop(matrix, i, row, scail)
            rec_matrix = rowop(rec_matrix, i, row, scail)

    return matrix, rec_matrix


def scail_pivets(matrix, rec_matrix):
    for row in range(len(matrix)):
        scail = 1 / matrix[row][row]
        matrix = rowscail(matrix, row, scail)
        rec_matrix = rowscail(rec_matrix, row, scail)

    return matrix, rec_matrix


def print_matrix(matrix):
    for line_list in matrix:
        line_str = ''
        for num in line_list:
            num = round(num, 3)
            line_str += f'{num:>8}'
        print(line_str)


def send_to_output_csv(rec_matrix, output_name):
    output_matrix = []
    for line_list in rec_matrix:
        line_str_list = []
        for num in line_list:
            num = str(num)
            line_str_list.append(num)
        line_str = ','.join(line_str_list) + '\n'
        output_matrix.append(line_str)
    writelines(output_name, output_matrix)


def main(input_name, output_name):
    input_list = readlines(input_name)
    matrix = get_matrix(input_list)
    unit_matrix = get_unit(len(matrix))
    matrix, rec_matrix = row_esh(matrix, unit_matrix)
    matrix, rec_matrix = reduced_row_esh(matrix, rec_matrix)
    matrix, rec_matrix = scail_pivets(matrix, rec_matrix)
    print_matrix(rec_matrix)
    send_to_output_csv(rec_matrix, output_name)


if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])
