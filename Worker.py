#!/usr/bin/python3
import socket
import select
import logging
import Generator
import http.client

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

def send_http_request(req, host, port, filename):
    d = {'action': 'SEND REQ', 'host': host, 'protocol':'HTTP'}
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
    c = s.connect(host, int(port))
    rec = s.recv(1024)

    req = command + ' ' + data + '\r\n'
    d = {'action': 'SEND REQ', 'host': host, 'protocol':'FTP'}
    logger.debug(req, extra=d)

    if command == 'USER':
        s.send(req)
        res = s.recv(1024)
        process_response('FTP', host, res)
        s.close()
        return 0
    
    s.send('USER ' + username + '\r\n')
    res = s.recv(1024)

    if command == 'PASS':
        s.send(req)
        res = s.recv(1024)
        process_response('FTP', host, res)
        s.close()
        return 0

    s.send('PASS ' + passw + '\r\n')
    res = s.recv(1024)

    s.send(req)
    res = s.recv(1024)
    process_response('FTP', host, res)

def process_response(protocol, host, res):
    d = {'action': 'RESPONSE', 'host': host, 'protocol':protocol}
    if len(res) == 0:
        logger.debug("Empty Response", extra=d)
    else:
        logger.debug(res, extra=d)
    s.close()
