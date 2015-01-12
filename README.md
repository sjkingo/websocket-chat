websocket-chat
==============

A Websockets IRC-style chat server and client. It is written purely as a demo
of Websockets functionality and probably servces no useful purpose!

The server is written in Python 3 using `asyncio` and the `websockets` library.
The client is written in HTML5 and uses Bootstrap 3.

If you are using a Python version below 3.4, you will need to manually install
the `asyncio` library as it is not included.

### To start the server:

1. Install dependencies for the server (preferably in a virtualenv):

   ```
   $ pip install -r server/requirements.txt
   ```

2. Run the server on port 8080:

   ```
   $ python3 server/run.py
   ````

By default the server listens on `0.0.0.0:8080`. If this is not desired, edit `server/run.py:LISTEN_ADDRESS` and `html5client/ws.js:server`.

### To load the client:

1. Fire up the built-in Python web server and load the client from there:

   ```
   $ cd html5client
   $ python3 -m http.server
   $ $BROWSER 'http://localhost:8000/'
   ```

