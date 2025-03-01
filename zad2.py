def affine_function_value(inputs, a, b_list):
    result = a
    for i in range(len(inputs)):
        result ^= (b_list[i] & inputs[i])
    return result

def create_affine_truth_table(num_arguments, a, b_list):
    power = pow(2, num_arguments)
    truth_table = []
    for i in range(power):
        binary_representation = bin(i)[2:].zfill(num_arguments)
        inputs = [int(bit) for bit in binary_representation]
        function_value = affine_function_value(inputs, a, b_list)
        truth_table.append(str(function_value))
    return truth_table

def truth_table_to_decimal(truth_table):
    binary_string = "".join(truth_table)
    return int(binary_string, 2)

def generate_all_affine_functions(num_arguments):
    all_affine_functions = []
    num_coefficients = num_arguments
    total_combinations = pow(2, num_coefficients + 1)

    for i in range(total_combinations):
        binary_representation = bin(i)[2:].zfill(num_coefficients + 1)
        a = int(binary_representation[0])
        b_list = [int(bit) for bit in binary_representation[1:]]

        truth_table = create_affine_truth_table(num_arguments, a, b_list)
        binary_truth_table = "".join(truth_table)

        decimal_index = truth_table_to_decimal(truth_table)

        all_affine_functions.append((a, b_list, decimal_index, binary_truth_table))

    return all_affine_functions

num_arguments = 3
affine_functions = generate_all_affine_functions(num_arguments)

print(f"Wszystkie funkcje afiniczne dla {num_arguments} argumentów:")
for a, b_list, decimal_index, binary_truth_table in affine_functions:
    print(f"  a = {a}, b_list = {b_list}, decimal_index = {decimal_index}, binary_truth_table = {binary_truth_table}")