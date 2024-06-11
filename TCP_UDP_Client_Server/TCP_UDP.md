## Explanation of TCP and UDP
### TCP (Transmission Control Protocol)

TCP is a connection-oriented protocol, meaning a connection is established and maintained until the application programs at each end have finished exchanging messages. It ensures reliable and ordered delivery of a stream of bytes between applications running on hosts communicating via an IP network. Key features include:

- **Reliability**: Ensures that data is delivered without errors and in the correct order.
- **Flow Control**: Manages the pace at which data is sent to ensure that the sender does not overwhelm the receiver.
- **Error Checking**: Uses checksums to ensure data integrity.

### UDP (User Datagram Protocol)

UDP is a connectionless protocol, which means it sends messages, called datagrams, without establishing a connection. It is faster but less reliable compared to TCP. Key features include:

- **Speed**: Provides faster data transmission because it does not require connection establishment and termination.
- **Simplicity**: Lacks the overhead of TCP's reliability, making it simpler and more efficient for certain applications.
- **Use Cases**: Commonly used in applications where speed is crucial and occasional data loss is acceptable, such as video streaming, online gaming, and voice over IP (VoIP).

Both TCP and UDP are integral to network communication and are chosen based on the requirements of the specific application.


## File Structure

- `tcp_client.py`: TCP client script.
- `udp_client.py`: UDP client script.
- `udp_server.py`: UDP server script.

## Requirements

To run the scripts, you will need Python 3 installed on your system. Additionally, it is recommended to create a virtual environment to manage the project's dependencies.

## How to Use

### TCP Client (`tcp_client.py`)

The `tcp_client.py` script connects to a TCP server and sends a message. To run the script, follow these steps:

1. **Set Up the Server**: Before starting the client, you will need to have a TCP server running. It can be your own script or a publicly available server.

2. **Run the Client**:
    ```bash
    python tcp_client.py
    ```

3. **Modify the Script**: You can modify the server IP address and port in the code as needed.

### UDP Server (`udp_server.py`)

The `udp_server.py` script listens for messages from UDP clients and displays them on the console. To run the script, follow these steps:

1. **Run the Server**:
    ```bash
    python udp_server.py
    ```

2. **Send Messages**: Use the `udp_client.py` or another UDP client to send messages to the server.



### UDP Client (`udp_client.py`)

The `udp_client.py` script sends a message to a UDP server. To run the script, follow these steps:

1. **Set Up the Server**: Make sure that the UDP server is running.

2. **Run the Client**:
    ```bash
    python udp_client.py
    ```

3. **Modify the Script**: Change the server IP address and port in the code as needed.

## Exemples:
- [udp_client](./udp_client.py)
- [udp_server](./udp_server.py)
- [tcp_client](./tcp_clinet.py)
