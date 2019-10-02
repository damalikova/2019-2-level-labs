def calculate_frequences(text: str) -> dict:

    punctuation = [
        '.', ',', '!', '?', ';',
        ':', '"', "'", '—', '-',
        '$', '%', '*', '@', '^',
        '&', '~', '*', '+', '='
        ]

    if isinstance(text, str):

        for el in text:
            if el in punctuation or el.isdigit() or el.isspace():
                text = text.replace(el, ' ')
        split_text = text.lower().split()

        frequencies = dict()

        for word in split_text:
            if word not in frequencies:
                frequencies[word] = frequencies.get(word, 0)
            frequencies[word] += 1
        return frequencies

    return {}


def filter_stop_words(frequencies: dict, stop_words: tuple) -> dict:

    if frequencies and stop_words is not None:
        filtered_frequencies = frequencies.copy()

        for key in frequencies:
            if not isinstance(key, str):
                del filtered_frequencies[key]

        for word in stop_words:
            if word in filtered_frequencies:
                del filtered_frequencies[word]
        return filtered_frequencies

    return {}


def get_top_n(filtered_frequencies: dict, top_n: int) -> tuple:

    list_filtered_frequencies = list(filtered_frequencies.items())
    list_filtered_frequencies.sort(key=lambda dict_pair: -dict_pair[1])
    sorted_words = [pair[0] for pair in list_filtered_frequencies]

    if top_n > 0:
        content = tuple(sorted_words[:top_n])
        return content

    return ()


def read_from_file(path_to_file: str, lines_limit: int) -> str:

    with open(path_to_file) as full_text:
        text = full_text.readlines(lines_limit)
        return '\n'.join(text)


def write_to_file(path_to_file: str, content: tuple):

    with open(path_to_file, 'w') as file_to_write:
        file_to_write.write('\n'.join(content))
