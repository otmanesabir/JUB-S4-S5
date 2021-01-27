
from mrjob.job import MRJob
from mrjob.step import MRStep

class MRMeanMaxTemp(MRJob):

    def mapper_get_temperatures(self, _, line):
        # yield each word in the line
        date = line[4:9] + "-" + line[15:18] + "-" + line[19:20] + "-" + line[21:22]
        temp = value[87:92]
        if (temp != "+9999"):
         yield(date, int(temp))

    def combiner_get_maximum(self, date, temperatures):
        # sum the words we've seen so far
        yield (date, max(temperatures))

    def mapper_mean_temperatures(self, word, counts):
        # send all (num_occurrences, word) pairs to the same reducer.
        # num_occurrences is so we can easily use Python's max() function.
        old_date_segments = word.split("-");
        new_date = old_date_segments[0] + "-" + old_date_segments[2] + "-" + old_date_segments[3]
        yield (new_key, counts)

    # discard the key; it is just None
    def reducer_find_mean_temperatures(self, dates, counts):
        # each item of word_count_pairs is (count, word),
        # so yielding one results in key=counts, value=word
        yield (new_key, mean(counts))

    def steps(self):
        return [
            MRStep(mapper=self.mapper_get_temperatures,
                   combiner=self.combiner_get_maximum,
                   reducer=self.mapper_mean_temperatures),
            MRStep(reducer=self.reducer_find_mean_temperatures)
        ]

if __name__ == '__main__':
    MRMeanMaxTemp.run()
