import asyncio

import structlog

logger = structlog.get_logger(__name__)


class Server(object):
    """
    echo Server

    """

    def __init__(self, config: dict, wait_timeout=None, read_timeout=30):
        self.config = config
        self.writers = []

    async def run(self, host, port: int = 5000):
        server = await asyncio.start_server(
            self.handle_client, host, port
        )
        sockname = server.sockets[0].getsockname()
        logger.info("Serving", sockname=sockname)

        echo_task = asyncio.create_task(self.echo_request())
        async with server:
            server_task = asyncio.create_task(server.serve_forever())
            await asyncio.wait(
                [echo_task, server_task],
                return_when=asyncio.ALL_COMPLETED
            )

    async def handle_client(self,
                            reader: asyncio.StreamReader,
                            writer: asyncio.StreamWriter):
        """
        클라이언트의 요청 처리

        """
        self.writers.append(writer)

        try:
            while writer in self.writers:
                try:
                    # TODO: stream에서 EOF 될떄까지 읽기
                    data = await reader.read(100)
                    writer.write(data)
                    await writer.drain()
                except (asyncio.CancelledError, KeyboardInterrupt):
                    raise
                except Exception as e:
                    logger.exception(exc_info=e)
        finally:
            self.writers.remove(writer)
            writer.close()
