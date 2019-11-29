"""
Labour work #3
WordStorage tests
"""

import unittest

from lab_3.main import WordStorage


class WordStorageTest(unittest.TestCase):
    """Check word storage class functionality"""

    def test_word_storage_put_ideal(self):
        """word is added to storage"""
        word_storage = WordStorage()
        word = 'word'
        num = word_storage.put(word)
        self.assertEqual(word_storage.storage[word], num)

    def test_word_storage_put_word_none(self):
        """none is not added to storage"""
        word_storage = WordStorage()
        word = None
        word_storage.put(word)
        self.assertEqual(word_storage.storage, {})

    def test_word_storage_put_word_not_str(self):
        """non string word is not added to storage"""
        word_storage = WordStorage()
        word = 123
        word_storage.put(word)
        self.assertEqual(word_storage.storage, {})

    def test_word_storage_put_existing(self):
        """existing word is not added to storage"""
        word_storage = WordStorage()
        word = 'word'
        word_storage.storage = {'word': 1}
        word_storage.put(word)
        self.assertEqual(word_storage.storage, {'word': 1})

    def test_word_storage_get_id_of_ideal(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_id_of('word'), 1)

    def test_word_storage_get_id_of_none(self):
        """get_id_of none"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_id_of(None), -1)

    def test_word_storage_get_id_of_not_str(self):
        """id is not str  get_id_of"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_id_of(123), -1)

    def test_word_storage_get_id_of_word_not_in_storage(self):
        """word not in storage"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_id_of('another'), -1)

    def test_word_storage_get_original_by_ideal(self):
        """ideal case for get_original_by"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_original_by(1), 'word')

    def test_word_storage_get_original_by_not_in_storage(self):
        """id not in storage get_original_by"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_original_by(2), 'UNK')

    def test_word_storage_get_original_id_none(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_original_by(None), 'UNK')

    def test_word_storage_get_original_id_not_num(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        word_storage.storage = {'word': 1}
        self.assertEqual(word_storage.get_original_by(None), 'UNK')

    def test_word_storage_from_corpus_ideal(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        sentence = ('<s>', 'mary', 'wanted', 'to', 'swim', '</s>')
        word_storage.from_corpus(sentence)
        self.assertEqual(len(word_storage.storage), 6)

    def test_word_storage_from_corpus_duplicates(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        sentence = ('<s>', 'mary', 'wanted', 'to', 'to', 'swim', '</s>')
        word_storage.from_corpus(sentence)
        self.assertEqual(len(word_storage.storage), 6)

    def test_word_storage_from_corpus_empty(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        sentence = ()
        word_storage.from_corpus(sentence)
        self.assertEqual(word_storage.storage, {})

    def test_word_storage_from_corpus_none(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        sentence = None
        word_storage.from_corpus(sentence)
        self.assertEqual(word_storage.storage, {})

    def test_word_storage_from_corpus_not_tuple(self):
        """ideal case for get_id_of"""
        word_storage = WordStorage()
        sentence = 'Mary wanted to swim'
        word_storage.from_corpus(sentence)
        self.assertEqual(word_storage.storage, {})
