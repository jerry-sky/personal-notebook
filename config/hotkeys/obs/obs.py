import asyncio
import os
from simpleobsws import WebSocketClient, Request


class OBS(object):

    __ws: WebSocketClient

    async def request(self, command: str, payload: dict = None) -> dict:
        if self.__ws is None:
            raise Exception('`request` has to be run within the `execute` method context')
        r = Request(command, payload)
        result = await self.__ws.call(r)
        print(result.requestStatus)
        return result.responseData

    def execute(self, program):
        async def meta_program():
            # read the WS password
            f = open(os.path.dirname(os.path.realpath(__file__)) + '/.ws')
            # read the first line (without newline at the end)
            password = f.readline()[:-1]
            f.close()
            # connect to the WS
            self.__ws = WebSocketClient(password=password, url='ws://localhost:4455')
            await self.__ws.connect()
            await self.__ws.wait_until_identified()
            # run provided script
            await program()
            # end connection
            await self.__ws.disconnect()

        loop = asyncio.get_event_loop()
        loop.run_until_complete(meta_program())
