class FileManager:
    # def __init__(self, file_path):
    #     self.file_path = file_path

    def read_file(self, file_path):
        with open(file_path) as file:
            return file.read()

    def split_file(self, parts, file_path):
        content = self.read_file(file_path)
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

    def save_txt(self, content, file_path):
        file = open(file_path, "w")
        file.write(str(content))
        file.close()
