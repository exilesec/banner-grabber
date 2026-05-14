import socket, os, pyfiglet
os.system("clear")
banner = pyfiglet.figlet_format("exilesec")
print(banner)

ip = input("\nip: ")

for port in range(1,1000):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(2)
        s.connect((ip,port))
        response = s.recv(1024)
        print(str(port), "Open.", "Service: ", response.decode())
    except socket.timeout as t:
        if port == 80:
            msg = "GET /HTTP/1.0\r\n\r\n"
            s.send(msg.encode())
            gelen = s.recv(1024)
            print(f"{port} Open.", "Service: {gelen.decode()}")
        else:
            print(str(port), "use different method.")
    except Exception as e:
        # print(str(port), "Closed.")
        pass
    finally:
        s.close()
