#!/usr/bin/python3
import socket
import select
import logging
import Generator
import http.client

# todo: logger toutes les informations


def http_fuzz(http_headers, host="127.0.0.1", port="8080"):
    
    req = "{} {} HTTP/{}\r\n".format(http_headers['Method'], http_headers['Path'], http_headers['Version'])
    for k, v in http_headers.items():
        if k == 'Method' or k == 'Path' or k == 'Version' or k == 'Data':
            continue
        req += k
        req += ": "
        req += v
        req += "\r\n"

    req += "\r\n"

    if http_headers['Method'] == "POST":
        req += http_headers[data]

    return req

def send_request(req, host, port, filename):
    d = {'action': 'SEND REQ', 'host': host, 'protocol':'HTTP'}
    logger.debug(req, extra=d)
    sock = socket.create_connection(("127.0.0.1", 8080))
    sock.setblocking(0)
    sock.send(req.encode())
    ready = select.select([sock], [], [], 1)
    d = {'action': 'RESPONSE', 'host': host, 'protocol':'HTTP'}
    if ready[0]:
        ans = sock.recv(1024)
        print(ans)
        logger.debug(ans, extra=d)
    else:
        logger.error('No response', extra=d)
    sock.close()

logger = logging.getLogger()
handler = logging.FileHandler('fuzz.log')
formatter = logging.Formatter(
        '%(asctime)s %(protocol)-12s %(host)-12s %(action)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)


dic = Generator.generate_http_input()
req = http_fuzz(dic)
send_request(req, '127.0.0.1', 8080, 'toto')
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

