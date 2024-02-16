import socket
import subprocess

def ping_port(ip, port):
    try:
        # Próbáljuk meg nyitni a socketet a megadott címre és portra
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        sock.settimeout(1)  # Állítsunk időtúllépési limitet

        result = sock.connect_ex((ip, port))
        if result == 0:
            print(f"{ip}:{port} elérhető")
        else:
            print(f"{ip}:{port} nem elérhető")
        sock.close()
    except KeyboardInterrupt:
        print("Megszakítva!")
        exit()
    except socket.gaierror:
        print("Érvénytelen cím")
        exit()
    except socket.error:
        print("Nem lehet kapcsolódni az adott címhez")
        exit()

def main():
    ip_prefix = "172.23.241"  # Az IP tartomány
    port = 22  # A pingelni kívánt port

    for i in range(1, 255):  # Vegyük végig az összes lehetséges IP-t az adott tartományban
        ip = f"{ip_prefix}.{i}"
        ping_port(ip, port)

if __name__ == "__main__":
    main()
