
import socket
import ssl
import thread

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
        print("Server encounterd a problem:", e)
        sock.close()












