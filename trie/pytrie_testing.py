from pytrie import StringTrie
import collections


def pytree_nucleotide_percentage(pytrie_trie, nucleotide_list):
    """retuns the percentage of nucleotide in the trie object
    pytrie_trie - trie object with data
    nucleotide_list - list of nucleotides to find I.E ["A", "G", "C", "T", "N"]"""
    # check if there are no nucleotides in the list
    if len(nucleotide_list) < 1:
        return "No nucleotides to count"

    # if there is only one nucleotide
    elif len(nucleotide_list) == 1:
        # calculate the nucleotide counts and total string lengths in the trie
        counts = [x.count(nucleotide_list) for x in pytrie_trie]
        totals = [len(x) for x in pytrie_trie]

        # return the percentage
        return sum(counts) / sum(totals)

    # otherwise the list is greater than 1 number, calculate it for each nucleotide
    else:
        # holders for our lists to sum
        final_totals = []
        final_counts = []
        # calculate the total lengths seperately ounts for each nucleotide
        # loop over the trie
        for x in pytrie_trie:
            # check if the original item occured more than once and if it did
            if pytrie_trie[x][0] > 1:
                # append totals and counts to our list multiplied by number of occurences
                final_totals.append(len(x) * pytrie_trie[x][0])
                final_counts.append(
                    [
                        x.count(nucleotide) * pytrie_trie[x][0]
                        for nucleotide in nucleotide_list
                    ]
                )
            # if there is a duplicate in our list * pytrie_trie[x][0][0]
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




def run_pytrie(list_to_use, prefix, percentage_list):
    """main func to be imported and run everything"""
    counter = collections.Counter(list_to_use) # just for side by side so this is included with others
    pytrie_object = StringTrie(zip(counter.keys(), [(x,) for x in counter.values()]))
    pytree_nucleotide_percentage(pytrie_object, percentage_list)
    pytrie_object.keys(prefix=prefix)




if __name__ == "__main__":

    # according to the instructions instantiate a memory efficient trie
    # that contains the nucleotide sequences and count of times they occur
    first_nucleotide_list = ["ACTG", "AACT", "TCAGG", "TTGGA"]
    counter = collections.Counter(first_nucleotide_list)
    # values contain times they occur and we save them as tupe objects for the record trie
    tiny_trie = StringTrie(zip(counter.keys(), [(x,) for x in counter.values()]))
    print(tiny_trie)

    # # needs to be 0.44 (8/18)
    print(pytree_nucleotide_percentage(tiny_trie, ["G", "C"]))
    assert round(pytree_nucleotide_percentage(tiny_trie, ["G", "C"]), 2) == 0.44
    # # needs to be 1.0 (18/18)
    print(pytree_nucleotide_percentage(tiny_trie, ["A", "C", "G", "T"]))
    assert (
        round(pytree_nucleotide_percentage(tiny_trie, ["A", "C", "G", "T"]), 1) == 1.0
    )

    # # second set of checking
    second_nucleotide_list = ["ACTG", "AACT", "TCAGG", "ACTG", "ACTG", "GGCG", "TTGGA"]
    counter = collections.Counter(second_nucleotide_list)
    values = [(x,) for x in counter.values()]
    tiny_trie_2 = StringTrie(zip(counter.keys(), [(x,) for x in counter.values()]))
    print(tiny_trie_2)

    # # needs to be 0.53 (16/30)
    print(pytree_nucleotide_percentage(tiny_trie_2, ["G", "C"]))
    assert round(pytree_nucleotide_percentage(tiny_trie_2, ["G", "C"]), 2) == 0.53
