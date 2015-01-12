import asyncio

# The set of clients connected to this server. It is used to distribute
# messages.
clients = {} #: {websocket: name}

@asyncio.coroutine
def client_handler(websocket, path):
    print('New client', websocket)
    print(' ({} existing clients)'.format(len(clients)))

    # The first line from the client is the name
    name = yield from websocket.recv()
    yield from websocket.send('Welcome to websocket-chat, {}'.format(name))
    yield from websocket.send('There are {} other users connected: {}'.format(len(clients), list(clients.values())))
    clients[websocket] = name
    for client, _ in clients.items():
        yield from client.send(name + ' has joined the chat')

    # Handle messages from this client
    while True:
        message = yield from websocket.recv()
        if message is None:
            their_name = clients[websocket]
            del clients[websocket]
            print('Client closed connection', websocket)
            for client, _ in clients.items():
                yield from client.send(their_name + ' has left the chat')
            break

        # Send message to all clients
        for client, _ in clients.items():
            yield from client.send('{}: {}'.format(name, message))
