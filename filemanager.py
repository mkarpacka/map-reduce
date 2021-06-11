class FileManager:
    def __init__(self, file_path):
        self.file_path = file_path

    def read_file(self):
        with open(self.file_path) as file:
            return file.read()

    def split_file(self, parts):
        content = self.read_file()
        chunk_size = int(len(content) / parts) + 1
        content_in_chunks = []
        chunk_content = ""
        last_index = 0
        for i, character in enumerate(content):
            if i % chunk_size == 0 and i != 0:
                content_in_chunks.append(chunk_content)
                chunk_content = ""
                last_index = i
            chunk_content += character

        if last_index < len(content):
            content_in_chunks.append(content[last_index:])

        return content_in_chunks


# f = FileManager('data.txt')
# f.read_file()
# f.split_file(3)
