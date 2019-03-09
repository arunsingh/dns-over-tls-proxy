
import socket
import ssl
import thread

def make_request(encrypted_socket,query):
    tcp_query = build_query(query)
    encrypted_socket.send(tcp_query)
    result = encrypted_socket.recv(1024)

    return result

def build_query(query):
    pre_length = "\x00" + chr(len(query))
    prefixed_query = pre_length + query

    return prefixed_query

def encrypted_connection(cloudflare_ip):
    # Make an encrypted tcp connection
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('/etc/ssl/certs/ca-certificates.crt')

    encrypted_socket = context.wrap_socket(sock, server_hostname=cloudflare_ip)
    encrypted_socket.connect((cloudflare_ip , cloudflare_port))

    return encrypted_socket

def request_handler(data, addr, cloudflare_ip):
  encrypted_socket = encrypted_connection(cloudflare_ip)
  tcp_result = make_request(encrypted_socket, data)
  udp_result = tcp_result[2:]
  sock.sendto(udp_result,addr)

if __name__ == '__main__':
    cloudflare_ip = '1.1.1.1'
    cloudflare_port = 853
    # The first default ip assigned by docker, after the gateway
    proxy_ip = '172.17.0.2'
    proxy_port= 853

    print("Starting server...")
    try:
        # Make a udp thread
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((proxy_ip, proxy_port))

        while True:
            data,addr = sock.recvfrom(1024)
            thread.start_new_thread(request_handler,(data, addr, cloudflare_ip))

    except Exception, e:
        print("Server encountered a problem:", e)
        sock.close()












