from collections import deque
# ----------------------------------------------------------------------------------------------------------------------
def bfs_traversal(adj):
    """
    Uses BFS traversal to find all the different partitions in an adjacency list
    :param adj: adjacency list of which partitions will be found
    :type adj: dictionary
    :return: partitions: set of partitions
    :rtype: partitions: set
    """
    visited = set()
    partitions = []
    for word in adj:                # Go through words in adjacency list
        if word not in visited:
            partition = set()       # creates a new partition for every new non visited element
            q = deque([word])

            while q:                            # fully explores a partition
                curr_word = q.popleft()
                if curr_word not in visited:    # checks if the word is visited
                    visited.add(curr_word)      # adds to visited list
                    partition.add(curr_word)    # adds to current partition
                    if curr_word in adj.keys():
                        for neighbour in adj[curr_word]:
                            q.append(neighbour) #appends all connections of the current word to the queue
            partitions.append(partition)        # when current partition is fully explored append it to list of partitions
    with open("databases/partitions.txt", "w", newline= "\n") as file:
        file.write(str(partitions))             # writes the partitions into a file
    return partitions
# ----------------------------------------------------------------------------------------------------------------------
def load_partitions_from_file(filename):
    """
    This function loads partitions from partition.txt to a list of sets,
    that have a length of over 40 words in a partition.
    :param filename: file containing partitions
    :type filename: str
    :return: list of sets, each set contains words in a partition
    :rtype: list[set[str]]
    """
    with open(filename, "r") as file:
        partitions = eval(file.read())              # evaluate string to Pythong object (list of sets)

    partitions_sets = []                            # list to store the partitions
    for partition in partitions:
        if len(partition) > 40:                     # make sure length iof partition is over 40
            partitions_sets.append(set(partition))  # turn each partition into a set and append to list

    return partitions_sets                          # return all the partitioned sets
# ----------------------------------------------------------------------------------------------------------------------
def filter_partitions_by_word_length(partitions):
    """
    This function filters the partition sets of already over len 40 into a dictionary
    dependnig on the word_lengths it has

    :param partitions: list of partition sets containing words
    :type partitions: list[set[str]]
    :return: Dictionary with keys 4, 5, and 6 for word lengths, each containing a list of partitions
    :rtype: dict[int, list[set[str]]]
    """
    filtered_partitions = {4:[],                # making keys for each word length to store their partitions
                           5:[],
                           6:[]}

    for partition in partitions:                # loop through partitions
        first_word = next(iter(partition))      # get the first element of the partition
        word_len = len(first_word)              # find the length of that word

        if word_len in filtered_partitions:     # make sure that length is already as a key in dictionary
            filtered_partitions[word_len].append(partition) # append the partition to the correct key/word length

    return filtered_partitions
# ----------------------------------------------------------------------------------------------------------------------
def write_partition_to_file(filtered_partitions):
    """
    This function writes the partitions to separate files for 4, 5, and 6-letter words.

    :param filtered_partitions: dictionary containing partitions for word lengths 4, 5, and 6
    :type filtered_partitions: dict[int, list[set[str]]]
    :return: None
    """
    for length in [4,5,6]:                                  # loop through neccesaary word lengths
        filename = f"databases/partitions_{length}.txt"     # create a filename based on length

        with open(filename, "w") as output_file:            # open new file
            for partition in filtered_partitions[length]:   # loop through partitions for x-letter words
                for word in partition:                      # write every word in partition to a new line
                    output_file.write(word.upper().strip() + "\n")
# ----------------------------------------------------------------------------------------------------------------------