#!/usr/bin/python3
import socket
import select

commands = ["ABOR", "ACCT", "ADAT", "ALLO", "APPE", "AUTH", "CCC", "CDUP", "CONF", "CWD", "DELE", "ENC", "EPRT", "EPSV", "FEAT", "HELP", "LANG", "LIST", "LPRT", "LPSV", "MDTM", "MIC", "MKD", "MLSD", "MLST", "MODE", "NLST", "NOOP", "OPTS", "PASV", "PBSZ", "PORT", "PROT", "PWD", "REIN", "REST", "RETR", "RMD", "RNFR", "RNTO", "SITE", "SIZE", "SMNT", "STAT", "STOR", "STOU", "STRU", "SYST", "TYPE", "XCUP", "XMKD", "XPWD", "XRCP", "XRMD", "XRSQ", "XSEM", "XSEN"]

def http_fuzz(method='GET', path="/", version="1.0", host="127.0.0.1",
            useragent="UA", accept="text/html", data="test"):
    # data pris en compte que si method == "POST"
    req = "{} {} HTTP/{}\r\n".format(method, path, version)
    req += "Host: {}\r\n".format(host)
    req += "User-Agent: #{}\r\n".format(useragent)
    req += "Accept: #{}\r\n".format(accept)
    if method == "POST":
        req += "Content-Length: #{}\r\n".format(len(data))
    req += "\r\n"

    if method == "POST":
        req += data

    return req

def ftp_fuzz(ip, port, size):
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

