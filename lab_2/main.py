"""
Labour work #2. Levenshtein distance.
"""


def generate_edit_matrix(num_rows: int, num_cols: int) -> list:

    if isinstance(num_rows, int) and isinstance(num_cols, int):
        edit_matrix = [[0 for j in range(num_cols)] for i in range(num_rows)]

        return edit_matrix

    return []


def initialize_edit_matrix(edit_matrix: tuple,
                           add_weight: int,
                           remove_weight: int) -> list:

    if not edit_matrix or edit_matrix.count([]) > 0:
        return list(edit_matrix)

    elif isinstance(add_weight, int) and isinstance(remove_weight, int):

        for i in range(1, len(edit_matrix)):
            edit_matrix[i][0] = edit_matrix[i - 1][0] + remove_weight

        for j in range(1, len(edit_matrix[0])):
            edit_matrix[0][j] = edit_matrix[0][j - 1] + add_weight

        return list(edit_matrix)

    return list(edit_matrix)


def minimum_value(numbers: tuple) -> int:
    return min(numbers)


def fill_edit_matrix(edit_matrix: tuple,
                     add_weight: int,
                     remove_weight: int,
                     substitute_weight: int,
                     original_word: str,
                     target_word: str) -> list:

    if not edit_matrix:
        return []

    if edit_matrix.count([]) > 0 or \
            not isinstance(original_word, str) or \
            not isinstance(target_word, str):

        return list(edit_matrix)

    if not isinstance(remove_weight, int) or \
            not isinstance(add_weight, int) or \
            not isinstance(substitute_weight, int):

        return list(edit_matrix)

    for i in range(1, len(edit_matrix)):
        for j in range(1, len(edit_matrix[i])):

            if original_word[i - 1] != target_word[j - 1]:
                diagonal_weight = substitute_weight

            else:
                diagonal_weight = 0

            values = (edit_matrix[i - 1][j] + remove_weight,
                      edit_matrix[i][j - 1] + add_weight,
                      edit_matrix[i - 1][j - 1] + diagonal_weight,)

            edit_matrix[i][j] = minimum_value(values)

    return list(edit_matrix)


def find_distance(original_word: str,
                  target_word: str,
                  add_weight: int,
                  remove_weight: int,
                  substitute_weight: int) -> int:

    if not isinstance(remove_weight, int) or \
            not isinstance(add_weight, int) or \
            not isinstance(substitute_weight, int):

        return -1

    if not isinstance(original_word, str) or not isinstance(target_word, str):
        return -1

    if not original_word:
        return len(target_word) * add_weight

    if not target_word:
        return len(original_word) * remove_weight

    generated_matrix = generate_edit_matrix(num_rows=len(original_word) + 1,
                                            num_cols=len(target_word) + 1)

    initialized_matrix = initialize_edit_matrix(tuple(generated_matrix),
                                                add_weight,
                                                remove_weight)

    filled_matrix = fill_edit_matrix(tuple(initialized_matrix),
                                     add_weight,
                                     remove_weight,
                                     substitute_weight,
                                     original_word,
                                     target_word)

    result = filled_matrix[len(original_word)][len(target_word)]

    return result


def save_to_csv(edit_matrix: tuple, path_to_file: str) -> None:

    zero_matrix = []

    for row in edit_matrix:
        ','.join(str(row))
        zero_matrix.append(row)

    with open(path_to_file, 'w') as file_to_write:
        file_to_write.write(str(zero_matrix))


def load_from_csv(path_to_file: str) -> list:

    with open(path_to_file) as content:

        edit_matrix = []

        for line in content:
            line = list(line)
            edit_matrix.append(line)

        return edit_matrix
