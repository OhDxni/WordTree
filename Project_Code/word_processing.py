from collections import deque
from Project_Code.helper_functions import save_json, load_json
from pathlib import Path

project_root = str(Path(__file__).resolve().parents[2])

class WordProcessing:
    def __init__(self):
        self.origin_data_4 = f"{project_root}/databases/4letterwords.txt"
        self.origin_data_5 = f"{project_root}/databases/370k_Word_File.csv"
        self.origin_data_6 = f"{project_root}/databases/370k_Word_File.csv"
        self.output_directory = f"{project_root}/databases"
        
        self.all_words = None

        self.partitions = None
        self.pruned_partitions = None
        self.filtered_partitions = None

    def _process_words(self, input_file, word_length):
        """
        This function reads words from an input file containing ONLY 4-letter words
        and writes them to a new file where one word on every line, also making them lower case.

        :param input_file: input file containing words
        :type input_file: str
        :return: processed_data_4
        """
        with open(input_file, 'r') as f:
            words = f.read().strip().split()  # Split by spaces to get individual words\

        processed_words = []
        for word in words:
            if len(word) == word_length:
                processed_words.append(word.strip().upper())
        return processed_words

    def create_all_words(self):
        """
        This function merges 4-, 5-, and 6-letter words from different files into a single file.

        :param four: file containing 4-letter words
        :type four: str
        :param five: file containing 5-letter words
        :type five: str
        :param six: file containing 6-letter words
        :type six: str
        :return: None
        """
        words_4 = self._process_words(self.origin_data_4, word_length=4)
        words_5 = self._process_words(self.origin_data_5, word_length=5)
        words_6 = self._process_words(self.origin_data_6, word_length=6)

        all_words = set()
        for file in (words_4, words_5, words_6):
            for line in file:
                all_words.add(line.strip().upper())

        self.all_words = all_words
        return self.all_words

    def save_all_words(self):
        save_json(list(self.all_words), f"{project_root}/databases/all_words.json")  # List, otherwise JSON gets upset

    def load_all_words(self):
        try:
            self.all_words = load_json(f"{project_root}/databases/all_words.json")
        except (AttributeError, FileNotFoundError):
            if self.all_words is None:
                self.all_words = self.create_all_words()
                self.save_all_words()

    def all_words_to_partitions(self, adj_list): # Previously bfs_traversal
        """
        Uses BFS traversal to find all the different partitions in an adjacency list
        :param adj: adjacency list of which partitions will be found
        :type adj: dictionary
        :return: partitions: set of partitions
        :rtype: partitions: set
        """
        if adj_list is None:
            raise ValueError("Adjacency list is not present!")

        visited = set()
        partitions = []

        for word in adj_list:  # Go through words in adjacency list
            if word not in visited:
                partition = set()  # creates a new partition for every new non visited element
                q = deque([word])

                while q:  # fully explores a partition
                    curr_word = q.popleft()
                    if curr_word not in visited:  # checks if the word is visited
                        visited.add(curr_word)  # adds to visited list
                        partition.add(curr_word)  # adds to current partition
                        if curr_word in adj_list.keys():
                            for neighbour in adj_list[curr_word]:
                                q.append(neighbour)  # appends all connections of the current word to the queue
                partitions.append(partition)  # when current partition is fully explored append it to list of partitions

        self.partitions = partitions
        return self.partitions

    def prune_partitions(self):
        """
        This function loads partitions from partition.txt to a list of sets,
        that have a length of over 40 words in a partition.
        :param filename: file containing partitions
        :type filename: str
        :return: list of sets, each set contains words in a partition
        :rtype: list[set[str]]
        """
        if self.partitions is None:
            raise ValueError("Partitions is not present; run all_words_to_partitions!")

        partitions_sets = []  # list to store the partitions
        for partition in self.partitions:
            if len(partition) > 40:  # make sure length iof partition is over 40
                partitions_sets.append(set(partition))  # turn each partition into a set and append to list

        self.pruned_partitions = partitions_sets
        return self.pruned_partitions, print("Pruned")  # return all the partitioned sets

    def filter_partitions(self):
        """
        This function filters the partition sets of already over len 40 into a dictionary
        depending on the word_lengths it has

        :param partitions: list of partition sets containing words
        :type partitions: list[set[str]]
        :return: Dictionary with keys 4, 5, and 6 for word lengths, each containing a list of partitions
        :rtype: dict[int, list[set[str]]]
        """
        if self.pruned_partitions is None:
            raise ValueError("Pruned partitions is not present; run prune_partitions!")

        filtered_partitions = {4: [],  # making keys for each word length to store their partitions
                               5: [],
                               6: []}

        for partition in self.pruned_partitions:  # loop through partitions
            first_word = next(iter(partition))  # get the first element of the partition
            word_len = len(first_word)  # find the length of that word

            if word_len in filtered_partitions:  # make sure that length is already as a key in dictionary
                filtered_partitions[word_len].append(partition)  # append the partition to the correct key/word length

        self.filtered_partitions = filtered_partitions
        return self.filtered_partitions, print("Filtered!")

    def write_partitions(self):
        """
        This function writes the partitions to separate files for 4, 5, and 6-letter words.

        :param filtered_partitions: dictionary containing partitions for word lengths 4, 5, and 6
        :type filtered_partitions: dict[int, list[set[str]]]
        :return: None
        """
        if self.filtered_partitions is None:
            raise ValueError("Filtered partitions is not present; run filter_partitions!")

        for length in [4, 5, 6]:  # loop through necessary word lengths
            filename = f"{project_root}/databases/partitions_{length}.json"  # create a filename based on length

            for partition in self.filtered_partitions[length]:  # loop through partitions for x-letter words
                save_json(list(partition), filename)
        print("Written!")