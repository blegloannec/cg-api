#!/usr/bin/env python3

import sys, json
import requests

class CG:
    def __init__(self, cgsession=None):
        self.url = 'https://www.codingame.com/services/'
        if cgsession is not None:
            self.cookies = {'cgSession': cgsession}
        else:
            self.cookies = None

    def _call(self, service, data):
        req = requests.post(self.url+service, cookies=self.cookies, data=data)
        if req:
            return req.json()
        else:
            print(req, file=sys.stderr)
            try:
                print(req.json(), file=sys.stderr)
            except:
                pass
            sys.exit(1)

    def findCodinGamerPublicInformations(self, cgid: int):
        data = json.dumps([cgid]).encode()
        return self._call('CodinGamer/findCodinGamerPublicInformations', data)

    def findAllMinimalProgress(self, cgid: int):
        data = json.dumps([cgid]).encode()
        return self._call('Puzzle/findAllMinimalProgress', data)

    def findPuzzleOfTheWeek(self):
        data = json.dumps([]).encode()
        return self._call('Puzzle/findPuzzleOfTheWeek', data)

    def findContribution(self, cgid: int):
        data = json.dumps([cgid, True]).encode()
        return self._call('Contribution/findContribution', data)

    def getAcceptedContributions(self, mode='ALL'):
        # mode = ALL | PUZZLE | CLASHOFCODE
        data = json.dumps([mode]).encode()
        return self._call('Contribution/getAcceptedContributions', data)


if __name__=='__main__':
    session = ''  # session cookie
    cgid    = 0   # cg user id
    api = CG(session)
    print(api.findAllMinimalProgress(cgid))
