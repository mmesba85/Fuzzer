# coding: utf-8

import random
from random import randint
import string
import json

from collections import defaultdict

http_methods = ['GET', 'POST', 'HEAD', 'PUT']
ftp_commands = ["USER", "PASS", "ABOR", "ACCT", "ADAT", "ALLO", "APPE", "AUTH", "CCC", "CDUP", "CONF", "CWD", "DELE", "ENC", "EPRT", "EPSV", "FEAT", "HELP", "LANG", "LIST", "LPRT", "LPSV", "MDTM", "MIC", "MKD", "MLSD", "MLST", "MODE", "NLST", "NOOP", "OPTS", "PASV", "PBSZ", "PORT", "PROT", "PWD", "REIN", "REST", "RETR", "RMD", "RNFR", "RNTO", "SITE", "SIZE", "SMNT", "STAT", "STOR", "STOU", "STRU", "SYST", "TYPE", "XCUP", "XMKD", "XPWD", "XRCP", "XRMD", "XRSQ", "XSEM", "XSEN"]
http_headers_ = ["Method", "Path", "User-Agent", "Version", "Connection", "Accept", "Accept-Charset", "Accept-Datetime", "Origin", "Content-Language", "Content-Encoding", "Content-Length", "Data"]
str_dict = ['\n', '\r\n', '%s', '%x', '%n', '\0']

# build input dictionary from configuration file
def build_http_input(file):
    headers = {}
    with open(file) as json_file:  
        data = json.load(json_file)
        if 'Method' in data:
            headers['Method'] = data['Method']
        else:
            headers['Method'] = get_random_method()
        if 'Path' in data:
            headers['Path'] = data['Path']
        else:
            headers['Path'] = get_random_path()
        if 'User-Agent' in data:
            headers['User-Agent'] = data['User-Agent']
        if 'Version' in data:
            headers['Version'] = data['Version']
        if 'Connection' in data:
            headers['Connection'] = data['Connection']
        if 'Accept' in data:
            headers['Accept'] = data['Accept']
        if 'Accept-Charset' in data:
            headers['Accept-Charset'] = data['Accept-Charset']
        if 'Accept-Datetime' in data:
            headers['Accept-Datetime'] = data['Accept-Datetime']
        if 'Origin' in data:
            headers['Origin'] = data['Origin']
        if 'Content-Language' in data:
            headers['Content-Language'] = data['Content-Language']
        if 'Content-Encoding' in data:
            headers['Content-Encoding'] = data['Content-Encoding']
            if 'Method' in data and headers['Method'] == 'POST':
                if 'Content-Length' in data:
                    headers['Content-Length'] = data['Content-Length']
                if 'Data' in data:
                    headers['Data'] = data['Data']
    fill_http_input(headers)
    return headers

# prend un mot et lui append des lettres de taille 5
# generalement on reprend la premiere lettre ou la derniere
# lettre et cette meme lettre on la rajoute plusieurs fois (debut/fin)
def append_random(word, size=5):
    last_char = word[len(word)-1]
    for i in range(size) :
        word += last_char
    return word

# Bit Flipping function
# the bits are flipped in some sequence or randomly
def bit_flipping_str(word):
    rand = randint(0, len(word)-1)
    chars = random.sample(range(0, len(word)-1), rand)
    flip_word = ''
    for i in range(len(word)):
        if i in chars:
            extended = randint(0, 255)
            flip_word += chr(extended)
        else:
            flip_word += word[i]
    return flip_word

def bit_flipping_int(num):
    bin_a = bin(num)
    str_num = str(bin_a)
    rand = randint(0, len(str_num)-1)
    to_change = random.sample(range(0, len(str_num)-1), rand)
    flip_num_str = str_num[0]
    for i in range(1, len(str_num)):
        if i in to_change:
            if str_num[i] == '0':
                flip_num_str += '1'
            else:
                flip_num_str += '0'
        else:
            flip_num_str += str_num[i]
    res = int(flip_num_str, 2)
    return res

# generate random inputs
def generate_http_input():
    http_headers = {}
    http_headers['Method'] = get_random_method()
    http_headers['Path'] = c
    http_headers['User-Agent'] = get_random_path()
    http_headers['Version'] = '1.1'
    http_headers['Connection'] = get_random_string()
    http_headers['Accept'] = get_random_string()
    http_headers['Accept-Charset'] = get_random_string()
    http_headers['Accept-Datetime'] = get_random_string()
    http_headers['Origin'] = get_random_string()
    http_headers['Content-Language'] = get_random_string()
    http_headers['Content-Encoding'] = get_random_string()
    if http_headers['Method'] == 'POST':
        http_headers['Content-Length'] = get_random_int()
        http_headers['Data'] = get_random_string(200)
    return http_headers

# build input dictionary from configuration file
def fill_http_input(http_headers):
    for h in http_headers_:
        if h not in http_headers:
            if h == 'Content-Length':
                http_headers[h] = get_random_int()
            elif h == 'Method':
                http_headers[h] = get_random_method()
            elif h == 'Path':
                http_headers = get_random_path()
            elif h == 'Version':
                http_headers[h] = get_random_version()
            else:
                http_headers[h] = get_random_string()
    return http_headers

# generate random inputs
def build_ftp_input(file):
    headers = defaultdict(list)
    with open(file) as json_file:  
        data = json.load(json_file)
        if 'Username' in data:
            headers['Username'].append(data['Username'])
        else:
            headers['Username'].append('')
        if 'Password' in data:
            headers['Password'].append(data['Password'])
        else:
            headers['Password'].append('')
        i = 1
        for p in data['Commands']:
            if 'Command' in p:
                headers[i].append(p['Command'])
            if 'Data' in p:
                headers[i].append(p['Data'])
            else:
                headers[i].append(get_random_string())
            i += 1
    return headers

# Build a ftp_headers dictionnary containing random commands 
def generate_ftp_input(username='', password=''):
    ftp_headers = defaultdict(list)
    ftp_headers['Username'].append(username)
    ftp_headers['Password'].append(password)
    nbr = randint(0, len(ftp_commands)-1)
    cmd = get_random_ftp_command(nbr)
    j = 1
    for i in cmd : 
        ftp_headers[j].append(i)
        ftp_headers[j].append(get_random_string())
        j += 1
    return ftp_headers

# Get a list of n random ftp commands
def get_random_ftp_command(n):
    rand = random.sample(range(0, len(ftp_commands)-1), n)
    ftps = []
    for i in rand:
        ftps.append(ftp_commands[i])
    return ftps

# generate random int from 0 to size
def get_random_int(size=10):
    i = 1
    s = '9'
    j = 0
    for j in range(1, size):
        i = i * 10
        s = s + '9'
    return random.randrange(i, int(s))

# generate random string with size length
def get_random_string(size=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))

# generate random http method
def get_random_method():
    r = random.randrange(0, len(http_methods)-1)
    return http_methods[r]

# generate random path for http protocol
def get_random_path(size=3):
    letters = string.ascii_lowercase
    return '/'.join(random.choice(letters) for i in range(size))

# apply random mutation or bit flipping
def move_data(protocol, data, method):
    if protocol == 'http':
        for k, v in data.items():
            if type(v) is int:
                if method == 'random':
                    data[k] = int(append_random(str(v)))
                else:
                    data[k] = bit_flipping_int(v)
                    print(data[k])
            else:
                if method == 'random':
                    data[k] = append_random(v)
                else:
                   data[k] = bit_flipping_str(v)       
    else:
        for k,v in data.items():
            if type(k) is int:
                if method == 'random':
                    data[k][1] = append_random(data[k][1])
                else:
                    data[k][1] = bit_flipping_str(data[k][1])          
    return data

# generate sensitive input
def get_sensitive_input(size=5):
    s = ""
    r = random.randrange(0, len(str_dict)-1)
    for i in range(0, size):
        s = s + str_dict[r]
    return s;

# build sensitive input
def append_sensitive(protocol, data, size):
    for k, v in data.items():
        if protocol == 'ftp':
            if type(k) is int:
                data[k][1] = get_sensitive_input(size)
        else:
            if k == 'Content-Length':
                data[k] = -1
            else:
                data[k] = get_sensitive_input(size)
    return data
