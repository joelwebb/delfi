from itertools import takewhile
import collections
from sortedcontainers import SortedDict

def simple_trie_nucleotide_percentage(simple_trie, nucleotide_list):
    """retuns the percentage of nucleotide in the trie object
    simple_trie - trie object with data
    nucleotide_list - list of nucleotides to find I.E ["A", "G", "C", "T", "N"]"""
    # check if there are no nucleotides in the list
    if len(nucleotide_list) < 1:
        return "No nucleotides to count"

    # if there is only one nucleotide
    elif len(nucleotide_list) == 1:
        # calculate the nucleotide counts and total string lengths in the trie
        counts = [x.count(nucleotide_list) for x in simple_trie]
        totals = [len(x) for x in simple_trie]

        # return the percentage
        return sum(counts) / sum(totals)

    # otherwise the list is greater than 1 number, calculate it for each nucleotide
    else:
        # holders for our lists to sum
        final_totals = []
        final_counts = []
        # calculate the total lengths seperately ounts for each nucleotide
        # loop over the trie
        for x in simple_trie:
            # check if the original item occured more than once and if it did
            if simple_trie[x] > 1:
                # append totals and counts to our list multiplied by number of occurences
                final_totals.append(len(x) * simple_trie[x])
                final_counts.append(
                    [
                        x.count(nucleotide) * simple_trie[x]
                        for nucleotide in nucleotide_list
                    ]
                )
            # if there is a duplicate in our list * simple_trie[x][0][0]
            else:
                # append totals and counts to our list
                final_totals.append(len(x))
                final_counts.append(
                    [x.count(nucleotide) for nucleotide in nucleotide_list]
                )

        # calculate the sums where the counts are not zero and return the percentage
        return sum(
            [item for sublist in final_counts for item in sublist if item > 0]
        ) / sum(final_totals)


def simple_trie(words):
    """uses a list of words to make a dictionary for a trie"""
    # make a dictionary
    d = {}
    # loop over the words we want to add
    for word in sorted(words):
        # if it ins't there, add a 0 to count occurences
        if word not in d:
            d[word] = 1
        # if it is there already, increase times it showed up
        else:
            d[word] += 1
    # returns a sorted dictionary for decreasing processing time
    return SortedDict(d)


def find_word(trie, word):
    """searches for a full word"""
    # loop through keys
    for key in trie.keys():
        # check if it is an exact match
        if word == key:
            return trie[key]
        else:
            pass
    return "Word {} doesn't exist in trie".format(word)


def find_prefix(trie, prefix):
    """searches for a prefix and returns all words in dictionary with prefix"""
    # returns a list of all keys in the dictionary that start with the prefix using a left bisect
    return [
        trie[k]
        for k in takewhile(
            lambda x: x.startswith(prefix),
            trie.irange(trie.iloc[trie.bisect_left(prefix)]),
        )
    ]


def run_simple(list_to_use, prefix, percentage_list):
    """main func to be imported and run everything"""
    counter = collections.Counter(list_to_use) # just for side by side so this is included with others
    simple_trie_object = simple_trie(list_to_use)
    simple_trie_nucleotide_percentage(simple_trie_object, percentage_list)
    find_prefix(simple_trie_object, prefix)


if __name__ == "__main__":
    # not the most efficient because dictionaries are way worse than other trie packages
    # simple_trie_object = simple_trie(["ACTG", "AACT", "TCAGG", "ACTG", "ACTG", "GGCG", "TTGGA"])
    # basic trie functionalit
    # print(find_word(simple_trie_object, "ACTG"))
    # print(find_prefix(simple_trie_object, "A"))

    # according to the instructions instantiate a memory efficient trie
    # that contains the nucleotide sequences and count of times they occur
    first_nucleotide_list = ["ACTG", "AACT", "TCAGG", "TTGGA"]
    counter = collections.Counter(first_nucleotide_list)
    # values contain times they occur and we save them as tupe objects for the record trie
    simple_trie_object = simple_trie(["ACTG", "AACT", "TCAGG", "TTGGA"])
    print(simple_trie_object)

    # needs to be 0.44 (8/18)
    print(simple_trie_nucleotide_percentage(simple_trie_object, ["G", "C"]))
    # assert round(simple_trie_nucleotide_percentage(simple_trie, ["G", "C"]), 2) ==  0.44
    # needs to be 1.0 (18/18)
    print(simple_trie_nucleotide_percentage(simple_trie_object, ["A", "C", "G", "T"]))
    # assert round(simple_trie_nucleotide_percentage(simple_trie, ["A", "C", "G", "T"]), 1) ==  1.0

    # second set of checking
    second_nucleotide_list = ["ACTG", "AACT", "TCAGG", "ACTG", "ACTG", "GGCG", "TTGGA"]
    simple_trie_2 = simple_trie(second_nucleotide_list)
    print(simple_trie_2)

    # needs to be 0.53 (16/30)
    print(simple_trie_nucleotide_percentage(simple_trie_2, ["G", "C"]))
    # assert round(simple_trie_nucleotide_percentage(simple_trie_2, ["G", "C"]), 2) ==  0.53
