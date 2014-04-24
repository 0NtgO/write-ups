'''
Allows scoring of text using n-gram probabilities
17/07/12
'''
from math import log10

class ngram_score(object):
	def __init__(self, ngram_list, sep=' '):
		''' load a file containing ngrams and counts, calculate log probabilities '''
		self.ngrams = {}
		for line in ngram_list:
			key, count = line.split(sep)
			self.ngrams[key] = int(count)
		self.L = len(key)
		self.N = sum(self.ngrams.itervalues())
		#calculate log probabilities
		for key in self.ngrams.keys():
			self.ngrams[key] = log10(float(self.ngrams[key]) / self.N)
		self.floor = log10(0.01 / self.N)

	def score(self, text):
		''' compute the score of text '''
		score = 0
		for i in xrange(len(text) - self.L + 1):
			score += self.ngrams.get(text[i:i + self.L], self.floor)
		return score