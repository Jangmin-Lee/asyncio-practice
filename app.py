import asyncio
import click
from dotenv import find_dotenv, load_dotenv

from asyncio_server.app import create_app

try:
    load_dotenv(find_dotenv('.env'), override=False)
except IOError:
    load_dotenv(find_dotenv('.env.sample'), override=False)

server_app = create_app()
app = server_app

__all__ = [
    'server_app',
    'app'
]


@click.command()
@click.option('-t', '--host', 'host', default='0.0.0.0')
@click.option('-p', '--port', 'port', default=8007, type=click.INT)
def main(host, port):
    loop = asyncio.get_event_loop()
    loop.run_until_complete(server_app.run(host=host, port=port))


if __name__ == "__main__":
    main()
