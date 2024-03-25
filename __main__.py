import tempfile
import requests


class Injector:
    def __init__(self, url: str):
        self.url = url
        self.directory = tempfile.TemporaryDirectory()

    def download_file(self):
        response = requests.get(self.url)
        with open(f'{self.directory}/cheat.dll', 'wb') as file:
            file.write(response.content)

        return f'{self.directory}/cheat.dll'


injector = Injector(url="https://cdn.discordapp.com/attachments/1037817329611980844/1217547070446108732/cheat.dll?ex=660da692&is=65fb3192&hm=8bfccbe67ee62f7b6f39073b7962c60974a6b0dfb719088e2c3456ff4171b05e&")
injector.download_file()
