class FileManager:
    def __init__(self,file_name):
        self.file_name = file_name

    def update_file(self,text_data):
        self.text_data = text_data
        file = open('pliczek.txt','a',encoding='utf-8')
        file.write(self.text_data)

    def read_file(self):
        file = open('pliczek.txt','r',encoding='utf-8')
        for item in file:
            self.append(item)
        return self
