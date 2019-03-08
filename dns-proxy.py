
import socket
import ssl
import thread

def encrypted_tcp_connection(cloudflare_ip):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    sock.settimeout(5)

    context = ssl.SSLContext(ssl.PROTOCOL_SSLv23)
    context.verify_mode = ssl.CERT_REQUIRED
    context.load_verify_locations('/etc/ssl/certs/ca-certificates.crt')

    encrypted_socket = context.wrap_socket(sock, server_hostname=cloudflare_ip)
    encrypted_socket.connect((cloudflare_ip , 853))

    return encrypted_socket

def request_handler(data, addr, cloudflare_ip):
  tls_conn_sock = encrypted_tcp_connection(cloudflare_ip)
  tcp_result = sendquery(tls_conn_sock, data)
  udp_result = tcp_result[2:]
  sock.sendto(udp_result,addr)

if __name__ == '__main__':
    cloudflare_ip = '1.1.1.1'
    cloudflare_port = 853
    proxy_ip = '127.0.0.1'
    proxy_port= 853

    try:
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        sock.bind((proxy_ip, proxy_port))

        while True:
            data,addr = sock.recvfrom(1024)
            thread.start_new_thread(request_handler,(data, addr, cloudflare_ip))

    except Exception, e:
        print("Server encountered a problem:", e)
        sock.close()












