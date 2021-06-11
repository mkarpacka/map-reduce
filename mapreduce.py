from filemanager import FileManager
import threading


class MapReduce:
    def __init__(self, file_path, mappers_count, reducers_count):
        self.chunks = FileManager(file_path).split_file(mappers_count)
        self.mappers_count = mappers_count
        self.reducers_count = reducers_count
        self.mapping_result = []
        self.shuffle_result = []
        self.reduce_result = []

    def mapper(self, key, value):
        pass

    def reducer(self, key, values_list):
        pass

    def shuffle(self):
        unique_values = set([list[0] for list in self.mapping_result])
        self.shuffle_result = [[list for list in self.mapping_result if list[0] == value] for value in unique_values]

    def reducer_worker(self, i):
        pass

    def mapper_worker(self, i):
        key = i
        value = self.chunks[i]
        for result in self.mapper(key, value):
            self.mapping_result.append(result)

    def run(self):
        mapper_threads = []
        reducer_threads = []

        for i in range(self.mappers_count):
            t = threading.Thread(target=self.mapper_worker, args=(i,))
            mapper_threads.append(t)
            t.start()
        [t.join() for t in mapper_threads]

        self.shuffle()

        for i in range(self.reducers_count):
            t = threading.Thread(target=self.reducer_worker, args=(i,))
            reducer_threads.append(t)
            t.start()
        [t.join() for t in reducer_threads]

        print("Mapper:")
        print(self.mapping_result)
        print("Shuffle:")
        print(self.shuffle_result)
