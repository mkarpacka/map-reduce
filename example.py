from mapreduce import MapReduce


class Example(MapReduce):
    def __init__(self):
        MapReduce.__init__(self, file_path="data.txt", mappers_count=4, reducers_count=3)

    def mapper(self, key, value):
        results = []
        default_count = 1
        for word in value.split():
            results.append((word.lower(), default_count))
        return results

    def reducer(self, key, values):
        wordcount = sum(value for value in values)
        return key, wordcount


e = Example()
e.run()
