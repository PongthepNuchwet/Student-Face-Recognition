import requests
from module.Staticmethod_controller import StaticMD


class LineNotify:
    def __init__(self) -> None:
        super().__init__()

        self.url = 'https://notify-api.line.me/api/notify'
        self.token = StaticMD.lineToken()

    def Post(self, path, text):
        img = {'imageFile': open(path, 'rb')}
        data = {'message': text}

        headers = {'Authorization': 'Bearer ' + self.token}
        session = requests.Session()
        session_post = session.post(
            self.url, headers=headers, files=img, data=data)
