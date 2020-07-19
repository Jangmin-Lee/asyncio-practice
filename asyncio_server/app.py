import structlog

from server.echo_server import Server as EchoServer

logger = structlog.get_logger(__name__)


def create_app_echo() -> EchoServer:
    # TODO : configureation 가져오는 함수 작성
    config = {}
    server = EchoServer(config)
    return server
