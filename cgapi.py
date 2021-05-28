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

    def findContribution(self, handle: str):
        data = json.dumps([handle, True]).encode()
        return self._call('Contribution/findContribution', data)

    def getAcceptedContributions(self, mode='ALL'):
        # mode = ALL | PUZZLE | CLASHOFCODE
        data = json.dumps([mode]).encode()
        return self._call('Contribution/getAcceptedContributions', data)

    def search(self, query: str):
        data = json.dumps([query, 'en', 'props.type']).encode()
        return self._call('search/search', data)

    def findCodingamePointsStatsByHandle(self, cghandle: str):
        data = json.dumps([cghandle]).encode()
        return self._call('CodinGamer/findCodingamePointsStatsByHandle', data)

    def findProgressByIds(self, puzzids, cgid: int):
        data = json.dumps([puzzids, cgid, 2]).encode()
        return self._call('Puzzle/findProgressByIds', data)

    def findProgressByPrettyId(self, puzzname: str, cgid: int):
        data = json.dumps([puzzname, cgid]).encode()
        return self._call('Puzzle/findProgressByPrettyId', data)


if __name__=='__main__':
    session = ''  # session cookie
    api = CG(session)
    #handle = api.search('Niako')[0]['id']
    #cgid = int(api.findCodingamePointsStatsByHandle(handle)['codingamer']['userId'])
    cgid = 1569823
    puzzids = [puzz['id'] for puzz in api.findAllMinimalProgress(cgid)]
    puzzles = api.findProgressByIds(puzzids, cgid)
    for puzz in puzzles:
        print(puzz['id'], puzz['prettyId'])
