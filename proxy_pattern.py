class Image:
    def dispaly(self):
        pass


class RealImage(Image):
    def __init__(self, file_name: 'str'):
        self.file_name = file_name
        self.load_from_disk(file_name)

    def dispaly(self):
        print("Displaying : " + self.file_name)

    def load_from_disk(self, file_name: 'str'):
        print('loading ' + file_name)

class ProxyImage(Image):
    def __init__(self, file_name: 'str'):
        self.file_name = file_name
        self.real_image = None

    def dispaly(self):
        if self.real_image is None:
            self.real_image = RealImage(self.file_name)
        self.real_image.dispaly()

image = ProxyImage('test_img')
image.dispaly()
image.dispaly()





