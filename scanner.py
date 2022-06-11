import socket
import time
import datetime

def work_time(func):
    def wrapper(*args, **kwargs):
        start = datetime.datetime.now()
        func(*args, **kwargs)
        done = datetime.datetime.now()

        print("Scanner work time: " + str((done - start)) + " sec.")
    return wrapper

@work_time    
def port_scan(host, ports):
    for port in ports:
        # Socket init
        s = socket.socket()
        # 1 s timeout
        s.settimeout(1)
        try:
            # trying connect to host:port
            s.connect((host, port))
        except socket.error:
            pass
        else:
            print(f"{host}: {port} is active.")
        s.close()
    print(f"The program scanned {len(ports)} ports.")

def main():
    ports = [int(str(p).strip()) for p in open('ports.txt', 'r')]
    host = input("Type URL to website WITHOUT http\\https or IP-address: ")
    print("Waiting...")
    port_scan(host=host, ports=ports)

if __name__ == '__main__':
    main()
