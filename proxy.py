import random
import json


class Proxy():
    proxies = []

    def importProxy(self):
        with open("./proxy.json") as file:
            # Load its content and make a new dictionary
            self.proxies = json.load(file)
        return len(self.proxies)

    def getRandomProxy(self):
        self.importProxy()
        return self.proxies[random.randint(0, (len(self.proxies)-1))]
