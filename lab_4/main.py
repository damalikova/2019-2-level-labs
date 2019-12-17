"""
lab_4
"""

from math import log

REFERENCE_TEXTS = []


def clean_tokenize_corpus(docs: list) -> list:
    tokenized_corpus = []

    if docs:
        for doc in docs:
            if isinstance(doc, str):

                if '<br />' in doc:
                    doc = doc.replace('<br />', ' ')

                for element in doc:
                    if not element.isalpha() and element != ' ':
                        doc = doc.replace(element, '')

                tokenized_text = doc.lower().split()
                tokenized_corpus.append(tokenized_text)

    return tokenized_corpus


class TfIdfCalculator:
    def __init__(self, corpus):

        self.corpus = corpus
        self.tf_values = []
        self.idf_values = {}
        self.tf_idf_values = []
        self.file_names = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']

    def calculate_tf(self):

        if not self.corpus:
            return self.tf_values

        for doc in self.corpus:

            if not doc:
                continue

            tf_dict = dict()

            for word in doc:

                if not isinstance(word, str):
                    continue

                if word not in tf_dict:
                    tf_dict[word] = 1
                else:
                    tf_dict[word] += 1

            sum_of_frequencies = sum(tf_dict.values())

            for word, frequency in tf_dict.items():
                tf_dict[word] = frequency / sum_of_frequencies

            self.tf_values.append(tf_dict)

            return self.tf_values

    def calculate_idf(self):

        if not self.corpus:
            return self.idf_values

        total_n_of_docs = len(self.corpus)
        idf_dict = dict()

        for doc_index, doc in enumerate(self.corpus):

            if not doc:
                total_n_of_docs -= 1
                continue

            for word in doc:

                if not isinstance(word, str):
                    continue

                if total_n_of_docs is 1:

                    if word not in idf_dict:
                        idf_dict[word] = 1
                    else:
                        continue

                else:
                    if word in idf_dict:
                        idf_dict[word] = 1 + doc_index
                    else:
                        idf_dict[word] = 1

        for key, actual_n_of_docs in idf_dict.items():
            idf_dict[key] = log(total_n_of_docs / actual_n_of_docs)

        self.idf_values.update(idf_dict)

    def calculate(self):

        if not self.tf_values or not self.idf_values:
            return self.tf_idf_values

        for tf_dict in self.tf_values:

            tf_idf_dict = tf_dict.copy()

            for idf_key, idf_value in self.idf_values.items():

                if idf_key in tf_idf_dict:
                    tf_idf_dict[idf_key] *= idf_value

            self.tf_idf_values.append(tf_idf_dict)

    def report_on(self, word, document_index):

        try:
            tf_idf_dict = self.tf_idf_values[document_index]
        except (TypeError, IndexError):
            return ()

        list_of_pairs = []

        for key in tf_idf_dict:
            key_value_pair = (tf_idf_dict.get(key), key,)
            list_of_pairs.append(key_value_pair)

        list_of_pairs.sort(key=lambda x: (-x[0], x[1]))

        for pair in list_of_pairs:
            if word in pair:
                tf_idf_report = tf_idf_dict.get(word)
                position_report = list_of_pairs.index(pair)

                return tf_idf_report, position_report

    def dump_report_csv(self):

        with open('report.csv', 'w') as file_to:

            heading = 'word'

            for i_for_tf in range(len(self.file_names)):
                tf_column = ',tf_' + self.file_names[i_for_tf]
                heading += tf_column

            heading += ',idf'

            for i_for_tf_idf in range(len(self.file_names)):
                tf_idf_column = ',tf_idf_' + self.file_names[i_for_tf_idf]
                heading += tf_idf_column

            heading += '\n'

            file_to.write(heading)

            for word, idf_value in self.idf_values.items():

                csv_line = list()
                csv_line.append(idf_value)

                for i in range(len(self.file_names)):

                    if word in self.tf_values[i]:
                        csv_line.insert(i, self.tf_values[i][word])
                    else:
                        csv_line.insert(i, 0)

                tf_values_in_csv = csv_line[:4]
                tf_idf_values_in_csv = [0 for _k in range(len(self.file_names))]

                for tf_index, tf_value in enumerate(tf_values_in_csv):

                    if tf_value != 0:

                        tf_idf_dict = self.tf_idf_values[tf_index]
                        tf_idf_value = tf_idf_dict[word]
                        tf_idf_values_in_csv.insert(tf_index, tf_idf_value)
                        tf_idf_values_in_csv = tf_idf_values_in_csv[:len(self.file_names)]

                csv_line.extend(tf_idf_values_in_csv)
                line_to_write = word

                for value in csv_line:
                    line_to_write += ',' + str(round(value, 4))

                line_to_write += '\n'

                file_to.write(line_to_write)


if __name__ == '__main__':
    TEXTS = ['5_7.txt', '15_2.txt', '10547_3.txt', '12230_7.txt']
    for text in TEXTS:
        with open(text, 'r') as f:
            REFERENCE_TEXTS.append(f.read())
    # scenario to check your work
    TEST_TEXTS = clean_tokenize_corpus(REFERENCE_TEXTS)
    TF_IDF = TfIdfCalculator(TEST_TEXTS)
    TF_IDF.calculate_tf()
    TF_IDF.calculate_idf()
    TF_IDF.calculate()
    TF_IDF.dump_report_csv()
    print(TF_IDF.report_on('good', 0))
    print(TF_IDF.report_on('and', 1))
