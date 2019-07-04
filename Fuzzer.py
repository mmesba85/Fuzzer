#!/usr/bin/python3
import socket
import select
import logging

# todo: logger toutes les informations
FORMAT = '%(asctime)-15s %(protocol)s %(host)-8s %(message)s'
logging.basicConfig(filename='fuzz.log', format=FORMAT)

def http_fuzz(http_headers, host="127.0.0.1", port="8080"):
    
    req = "{} {} HTTP/{}\r\n".format(http_headers['Method'], http_headers['Path'], http_headers['Version'])
    for k, v in http_headers:
        if k == 'method' 
        or k == 'path' 
        or k == 'version' 
        or k == 'data':
            continue
        req += k
        req += " "
        req += v
        req += "\r\n"

    req += "\r\n"

    if http_headers['Method'] == "POST":
        req += http_headers[data]

    # loggg
    return req

def send_request(req, host, port, filename):
    sock = socket.create_connection(("127.0.0.1", 8080))
    sock.setblocking(0)
    sock.send(req)
    ready = select.select([sock], [], [], 1)
    if ready[0]:
        ans = sock.recv(1024)
        #loggggg
    else:
        print("No answer! Found something?")
        #logggg
    sock.close()

"""
a revoir
def ftp_fuzz(username, pass, method, ip="127.0.0.1", port="21", data):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	c = s.connect((ip, port))
	rec = s.recv(1024)
	print(rec)
	s.send('USER ' + username + '\r\n')
	res = s.recv(1024)
	print(res)
	s.send('PASS ' + passwd + '\r\n')
	res = s.recv(1024)
	print(res)
	for c in commands:
		print("Command = " + c + " String length = " + str(size))
		string = 'A' * size
		s.send(c + ' ' + string + '\r\n')
		res = s.recv(1024)
		if len(res) == 0:
			print("empty response")
		else:
			print("OK")
	s.close()
"""

