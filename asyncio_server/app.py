import collections
import typing

import structlog

from server.config import load_config
from server.api_server import Server as ApiServer
from server.echo_server import Server as EchoServer
from tanker.utils.logging import setup_logging

logger = structlog.get_logger(__name__)
Configuration = typing.Union[collections.Mapping, str]


def create_app_api() -> ApiServer:
    config = load_config()
    setup_logging(config['ENVIRONMENT']
                  not in {'development', 'production'})

    server = ApiServer(config)
    return server


def create_app_echo() -> EchoServer:
    config = load_config()
    setup_logging(config['ENVIRONMENT']
                  not in {'development', 'production'})

    server = EchoServer(config)
    return server
