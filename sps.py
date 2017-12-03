import threading as thr
import socket
import argparse
import termcolor

def port_scan(server, port, port_names):
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	try:
		sock.connect((server, port))
		print(termcolor.colored("[+] %d (%s) is open!" % (port, port_names[port]), "green"))
		sock.close()
	except:
		pass	

def main():
	parser = argparse.ArgumentParser()		
	parser.add_argument("-s", "--server", help="server name")
	args = parser.parse_args()

	if not args.server:
		print("hit \"-s or --server\" to scan...")
	else:
		server = args.server

		timeout = 1
		socket.setdefaulttimeout(timeout)	
		
		port_names = {21: "ftp", 22: "ssh", 23: "telent", 
						25: "smtp", 80: "http", 443: "https", 3306: "mysql"}

		ip = socket.gethostbyname(server)
		print("scanning %s (%s):" % (server, ip))

		for port in port_names.keys():
			thrd = thr.Thread(target=port_scan, args=(server, port, port_names))
			thrd.start()

if __name__ == "__main__":
	main()
