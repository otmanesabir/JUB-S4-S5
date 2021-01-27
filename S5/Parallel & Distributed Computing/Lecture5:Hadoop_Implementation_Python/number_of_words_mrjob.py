
from mrjob.job import MRJob

import re

class WordCount(MRJob):
   def mapper(self, key, value):
      words = value.split()
      yield("#S", len(words))

   def reducer(self, key, values):
      yield(key, sum(values))

if __name__ == '__main__':
   WordCount.run()
