import asyncio


async def tcp_echo_client(loop):
    reader, writer = await asyncio.open_connection('127.0.0.1', 5000,
                                                   loop=loop)
    try:
        while True:
            message = input('> Message: ')
            writer.write(message.encode())

            data = await reader.read(100)
            print(f'> Response: {data.decode()}')
    except KeyboardInterrupt:
        print('\nClose the socket')
    writer.close()


loop = asyncio.get_event_loop()
loop.run_until_complete(tcp_echo_client(loop))
loop.close()
