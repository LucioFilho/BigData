# using a try finally instead of a contest manager
def finally_instead_of_context_manager(host, port):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    try:
        s.connect((host, port))
        s.sendall(b'Hello, world')
    finally:
        s.close()

# do it instead
# in python most resources that need be closed have their own contest manager
def finally_instead_of_context_manager(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(b'Hello, world')
