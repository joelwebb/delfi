
import timeit
import random
import collections
import random
from pytrie import StringTrie
import marisa_trie
from pytrie_testing import pytree_nucleotide_percentage, run_pytrie
from marissa_testing import marisa_nucleotide_percentage, run_marissa
from simple_trie import simple_trie, find_word, find_prefix, simple_trie_nucleotide_percentage, run_simple

random.seed('42')

def random_length_dnasequence(sequence_length):
	""" 
	# Return random CGTA sequences, set minimum = maximum to get a specified length with N <25% of the time.
	# modified fromhttps://stackoverflow.com/questions/21205836/generating-random-sequences-of-dna
	"""
	actg_distribution = ''.join(random.choice('NATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG') for _x in range(100))
	# approximately 10% of the time randomly add N to the distribution
	return ''.join(random.choice(actg_distribution) for _x in range(sequence_length))


setup = '''
import timeit
import random
import collections
import random
from pytrie import StringTrie
import marisa_trie
from pytrie_testing import pytree_nucleotide_percentage, run_pytrie
from marissa_testing import marisa_nucleotide_percentage, run_marissa
from simple_trie import simple_trie, find_word, find_prefix, simple_trie_nucleotide_percentage, run_simple

random.seed('42')

def random_length_dnasequence(sequence_length):
	""" 
	# Return random CGTA sequences, set minimum = maximum to get a specified length with N <25% of the time.
	# modified fromhttps://stackoverflow.com/questions/21205836/generating-random-sequences-of-dna
	"""
	actg_distribution = ''.join(random.choice('NATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCGATCG') for _x in range(100))
	# approximately 10% of the time randomly add N to the distribution
	return ''.join(random.choice(actg_distribution) for _x in range(sequence_length))

#make a list of 1000 sequences between 10 - 30 characters long for testing
prefix_to_use = "ATG"
percentage_list = ["ATCG", "ATG", "GCC"]
list_of_seqs = [random_length_dnasequence(random.randint(10, 30)) for x in range(1000)]
# counter object for tries to use
counter = collections.Counter(list_of_seqs)

'''

if __name__ == "__main__":
	# run these individually with /usr/bin/time --verbose python3 compare_trie_performance.py
	# lets compare just building the trie structures
	print("marissa")
	print(min(timeit.Timer('marisa_trie.RecordTrie("<H", zip(counter.keys(), [(x,) for x in counter.values()]))', setup=setup).repeat(1, 1000)))
	print(min(timeit.Timer('run_marissa(list_of_seqs, prefix_to_use, percentage_list)', setup=setup).repeat(1, 1000)))
	print("\n") # setup only test run was 3.1 seconds --- (kbytes): 11252 memory
	print("pytrie")
	print(min(timeit.Timer('StringTrie(zip(counter.keys(), [(x,) for x in counter.values()]))', setup=setup).repeat(1, 1000)))
	print(min(timeit.Timer('run_pytrie(list_of_seqs, prefix_to_use, percentage_list)', setup=setup).repeat(1, 1000)))
	print("\n")# setup only test run was 15.2 seconds --- (kbytes): 16568 memory
	print("simple setup")
	print(min(timeit.Timer('simple_trie(list_of_seqs)', setup=setup).repeat(1, 1000)))
	print(min(timeit.Timer('run_simple(list_of_seqs, prefix_to_use, percentage_list)', setup=setup).repeat(1, 1000)))
	print("\n")# setup only test run was 1.23 seconds --- (kbytes): 57676

	# overall the dictionary is the fastest but uses the most memory --- marissa was the most memory efficient