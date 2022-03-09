## Documentation

### `Client()`

- `__init__(sock, on_send, on_recv)`\
  `sock` must be a connected socket. `on_send` must return something to send. `on_recv` must take in some received data.
  
- `start()`\
  Starts a Thread that calls `loop()`. can be stopped by calling `stop()`.
  
- `stop()`\
  Stops the connection without closing it, can be started again with `start()` or `loop()`.
  
- `loop()`\
  Goes into an infinite loop running the Client, useful if you want to use your own thread or main thread.
  
- `exit()`\
  Gets called when an `ConnectionError` or `EOFError` (Likely when the socket disconnects) happens in `loop()` or can be called to abruptly end the connection.
  
- `_send(data)`\
  Takes in an object and converts it to byte data using pickle, then sends that on the socket.
  
- `_recv()`\
  Receives byte data on the socket, converts it to an object using pickle and returns it.
  
- `from_address((IP, Port), *args, **kwargs)`\
  Makes a connected Client for you, just needs a tuple of `(IP, Port)` to connect to.
  

### `Server()`
- `__init__(sock, on_send, on_recv)`\
  `sock` must be a server socket. `on_send` must return something to send. `on_recv` must take in some received data.

- `start()`\
  Starts a Thread that calls `loop()`. can be stopped by calling `stop()`.
  
- `stop()`\
  Stops waiting for clients to connect without closing the socket, can be started again with `start()` or `loop()`.
  
- `connect_socket(sock)`\
  Gets called when a client connects, it should start a `Server.ServerClient()` from a socket.
  
- `connect_address(address)`\
  Same as `connect_socket()` just with an address.
  
- `loop()`\
  Goes into an infinite loop waiting for Clients to connect.
  
- `exit()`\
  Stops wating for Clients to connect and closes the server socket.
 
 - `from_address(address,  *args,  **kwargs)`\
 Creates a Server for you, just needs a tuple of `(Host, Port)` for the address.

### `Server.ServerClient()`
  - `server_send()`\
  Call this to get something to send from the Server.
  
  - `server_recv(data)`\
  Call this to tell the Server you have something to give it.