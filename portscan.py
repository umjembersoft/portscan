import socket
import subprocess
import sys

from datetime import datetime

subprocess.call('clear', shell=True)

remoteServer = raw_input("Masukkan alamat host untuk proses scanning : ")
remoteServerIP = socket.gethostbyname(remoteServer)

print "-" * 60
print "Tunggu...... Proses Scanning Remote Host", remoteServerIP
print "-" * 60

t1 = datetime.now()

try:
    for port in range(1, 1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port {}: \t Terbuka".format(port)
        sock.close()

except KeyboardInterrupt:
    print "Anda tekan Ctrl+C"
    sys.exit()

except socket.gaierror:
    print "Hostname tidak dapat diperiksa. Program akan keluar. . . ."
    sys.exit()

except socket.error:
    print "Tidak dapat terhubung ke server"
    sys.exit()

t2 = datetime.now()
total = t2 - t1

print
print "Proses Scanning selesai.."
print
print "Waktu yang dihabiskan untuk melakukan scanning adalah :", total
