import collections
import marisa_trie


def marisa_nucleotide_percentage(marissa_trie, nucleotide_list):
    """retuns the percentage of nucleotide in the trie object
    marissa_trie - trie object with data
    nucleotide_list - list of nucleotides to find I.E ["A", "G", "C", "T", "N"]"""
    # check if there are no nucleotides in the list
    if len(nucleotide_list) < 1:
        return "No nucleotides to count"

    # if there is only one nucleotide
    elif len(nucleotide_list) == 1:
        # calculate the nucleotide counts and total string lengths in the trie
        counts = [x.count(nucleotide_list) for x in marissa_trie]
        totals = [len(x) for x in marissa_trie]

        # return the percentage
        return sum(counts) / sum(totals)

    # otherwise the list is greater than 1 number, calculate it for each nucleotide
    else:
        # holders for our lists to sum
        final_totals = []
        final_counts = []
        # calculate the total lengths seperately ounts for each nucleotide
        # loop over the trie
        for x in marissa_trie:
            # check if the original item occured more than once and if it did
            if marissa_trie[x][0][0] > 1:
                # append totals and counts to our list multiplied by number of occurences
                final_totals.append(len(x) * marissa_trie[x][0][0])
                final_counts.append(
                    [
                        x.count(nucleotide) * marissa_trie[x][0][0]
                        for nucleotide in nucleotide_list
                    ]
                )
            # if there is a duplicate in our list * marissa_trie[x][0][0]
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


if __name__ == "__main__":

    # according to the instructions instantiate a memory efficient trie
    # that contains the nucleotide sequences and count of times they occur
    first_nucleotide_list = ["ACTG", "AACT", "TCAGG", "TTGGA"]
    counter = collections.Counter(first_nucleotide_list)
    # values contain times they occur and we save them as tupe objects for the record trie
    marissa = marisa_trie.RecordTrie(
        "<H", zip(counter.keys(), [(x,) for x in counter.values()])
    )

    # needs to be 0.44 (8/18)
    print(marisa_nucleotide_percentage(marissa, ["G", "C"]))
    assert round(marisa_nucleotide_percentage(marissa, ["G", "C"]), 2) == 0.44
    # needs to be 1.0 (18/18)
    print(marisa_nucleotide_percentage(marissa, ["A", "C", "G", "T"]))
    assert round(marisa_nucleotide_percentage(marissa, ["A", "C", "G", "T"]), 1) == 1.0

    # second set of checking
    second_nucleotide_list = ["ACTG", "AACT", "TCAGG", "ACTG", "ACTG", "GGCG", "TTGGA"]
    counter = collections.Counter(second_nucleotide_list)
    values = [(x,) for x in counter.values()]
    marissa_2 = marisa_trie.RecordTrie("<H", zip(counter.keys(), values))
    # needs to be 0.53 (16/30)
    print(marisa_nucleotide_percentage(marissa_2, ["G", "C"]))
    assert round(marisa_nucleotide_percentage(marissa_2, ["G", "C"]), 2) == 0.53
