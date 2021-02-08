from google.cloud import vision


class GoogleVisionClient:

    def __init__(self, uri: str):
        self.__client = vision.ImageAnnotatorClient()
        self.__image = vision.Image()
        self.__image.source.image_uri = uri

    def fetch_tags(self):
        response = self.__client.label_detection(image=self.__image)
        annotations_response = response.label_annotations
        self.labels = []
        for response in annotations_response:
            self.labels.append(response.description)


    def validate(self, primary_tag: str):
        if primary_tag in self.labels:
            return True
        else:
            return False
