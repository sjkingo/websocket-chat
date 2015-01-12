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

2. Run the server (note your firewall must allow port 80):

   ```
   $ python3 run.py
   ````

By default the server listens on `0.0.0.0:8080`. If this is not desired, edit `run.py`.

### To load the client:

Fire up the built-in Python web server and load the client from there:

```
$ cd html5client
$ python3 -m http.server
$ $BROWSER 'http://localhost:8000/'
```

