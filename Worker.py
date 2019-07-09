#!/usr/bin/python3
import socket
import select
import logging
import Generator
import http.client

def fuzz(protocol, data, host, port, nloop=5, size=5):
    
    if protocol == 'http':
        i = 0   
        for i in range(0, nloop):
            req = http_fuzz(data, host, port)
            print(req)
            send_http_request(req, host, port)
            data = Generator.move_data(protocol, data)
        
        data = Generator.append_sensitive(protocol, data, size)
        req = http_fuzz(data, host, port)
        send_http_request(req, host, port)
        data = Generator.move_data(data)
    
    data = Generator.append_sensitive(protocol, data, size)
    req = http_fuzz(data, host, port)
    print(req)
    send_http_request(req, host, port)

    else:
        i = 0   
        for i in range(0, nloop):
            usr = data['Username'][0]
            pwd = data['Password'][0]
            for k, v in data.items():
                if type(k) is int:
                    ftp_fuzz(v[0], v[1], str(usr), str(pwd), host, port)
                data = Generator.move_data(protocol, data)
        data = Generator.append_sensitive(protocol, data, size)
        for k, v in data.items():
            if type(k) is int:
                ftp_fuzz(v[0], v[1], str(usr), str(pwd), host, port)

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

def send_http_request(req, host, port):
    d = {'action': 'SEND REQ', 'host': host, 'protocol':'HTTP'}
    logger = logging.getLogger("mainlogger")
    logger.debug(req, extra=d)
    sock = socket.create_connection((host, int(port)))
    sock.setblocking(0)
    sock.send(req.encode())
    ready = select.select([sock], [], [], 1)
    d = {'action': 'RESPONSE', 'host': host, 'protocol':'HTTP'}
    if ready[0]:
        ans = sock.recv(1024)
        logger.debug(ans, extra=d)
    else:
        logger.error('Empty Response', extra=d)
    sock.close()

def ftp_fuzz(command, data, username="", passw="", host="127.0.0.1", port="21"):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    c = s.connect((host, int(port)))
    rec = s.recv(1024)
    print(str(username))
    print(passw)
    req = command + ' ' + data + '\r\n'
    d = {'action': 'SEND REQ', 'host': host, 'protocol':'FTP'}
    logger = logging.getLogger("mainlogger")
    logger.debug(req, extra=d)

    if command == 'USER':
        s.send(req.encode())
        res = s.recv(1024)
        process_response('FTP', host, res)
        s.close()
        return 0
    
    auth_req = 'USER ' + username + '\r\n'
    s.send(auth_req.encode())
    res = s.recv(1024)
    print(res)
    if command == 'PASS':
        s.send(req.encode())
        res = s.recv(1024)
        process_response('FTP', host, res)
        s.close()
        return 0

    auth_req = 'PASS ' + passw + '\r\n'
    s.send(auth_req.encode())
    res = s.recv(1024)
    print(res)
    s.send(req.encode())
    res = s.recv(1024)
    process_response('FTP', host, res)
    s.close()

def process_response(protocol, host, res):
    d = {'action': 'RESPONSE', 'host': host, 'protocol':protocol}
    logger = logging.getLogger("mainlogger")
    if len(res) == 0:
        logger.error("Empty Response", extra=d)
    else:
        logger.debug(res, extra=d)
