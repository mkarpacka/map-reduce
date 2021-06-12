from filemanager import FileManager
import threading


class MapReduce:
    def __init__(self, file_path, mappers_count, reducers_count):
        self.fileManager = FileManager()
        self.chunks = self.fileManager.split_file(mappers_count, file_path)
        self.mappers_count = mappers_count
        self.reducers_count = reducers_count
        self.mapping_result = []
        self.shuffle_result = []
        self.reduce_result = set()
        self.chunk_for_reducer_count = 0
        self.last_index = 0

    def mapper(self, key, value):
        pass

    def reducer(self, key, values_list):
        pass

    def shuffle(self):
        unique_values = set([list[0] for list in self.mapping_result])
        self.shuffle_result = [[list for list in self.mapping_result if list[0] == value] for value in unique_values]

        self.chunk_for_reducer_count = int(len(self.shuffle_result) / self.reducers_count) + 1

    def reducer_worker(self, i):
        key = i + 1
        calculated_index = self.chunk_for_reducer_count * key
        element_list = self.shuffle_result[self.last_index:calculated_index]
        self.last_index = calculated_index
        for val in element_list:
            values_list = [x[1] for x in val]
            result = None
            for reduce in self.reducer(key, values_list):
                result = reduce
            self.reduce_result.add((val[0][0], result))

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
        self.fileManager.save_txt(self.mapping_result, "mapper.txt")
        print("Shuffle:")
        print(self.shuffle_result)
        self.fileManager.save_txt(self.shuffle_result, "shuffle.txt")
        print("Reduce:")
        print(self.reduce_result)
        self.fileManager.save_txt(self.reduce_result, "reduce.txt")

