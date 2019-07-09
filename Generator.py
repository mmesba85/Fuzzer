# coding: utf-8

import random
from random import randint
import string
import json

from collections import defaultdict

http_methods = ['GET', 'POST', 'HEAD', 'PUT']
ftp_commands = ["USER", "PASS", "ABOR", "ACCT", "ADAT", "ALLO", "APPE", "AUTH", "CCC", "CDUP", "CONF", "CWD", "DELE", "ENC", "EPRT", "EPSV", "FEAT", "HELP", "LANG", "LIST", "LPRT", "LPSV", "MDTM", "MIC", "MKD", "MLSD", "MLST", "MODE", "NLST", "NOOP", "OPTS", "PASV", "PBSZ", "PORT", "PROT", "PWD", "REIN", "REST", "RETR", "RMD", "RNFR", "RNTO", "SITE", "SIZE", "SMNT", "STAT", "STOR", "STOU", "STRU", "SYST", "TYPE", "XCUP", "XMKD", "XPWD", "XRCP", "XRMD", "XRSQ", "XSEM", "XSEN"]
http_headers_ = ["Method", "Path", "User-Agent", "Version", "Connection", "Accept", "Accept-Charset", "Accept-Datetime", "Origin", "Content-Language", "Content-Encoding", "Content-Length", "Data"]

# reads file (yaml? json?) and build http_headers dict (comme le 
# dict de generate http input)
# le user a une liste de deux champs a remplir
# la cle est le "header" et sa valeur
# s'il donne que la clé alors la valeur est generee automatiquement
#
# json plus facile pour la sérialisation
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
    return headers

# prend un mot et lui append des lettres de taille 5
# generalement on reprend la premiere lettre ou la derniere
# lettre et cette meme lettre on la rajoute plusieurs fois (debut/fin)
def append_random(word, size=5):
    last_char = word[len(word)-1]
    for i in range(size) :
        word += last_char
    print(word)
    return word

# Bit Flipping function
# the bits are flipped in some sequence or randomly
def bit_flipping(word):
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

# rajouter d'autres header?
# TODO:
# prendre en compte le fait que l'utilisateur puisse specifier
# vouloir fuzzer que certain champs
# il peut aussi proposer une chaine de caractere pour ces champs
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

# apres que le user est donnee un fichier de config 
# il peut specifier vouloir remplir les autres champs aleatoirement
# optionnellement!
def fill_http_input(http_headers):
    for h in http_headers_:
        if h not in http_headers:
            if h == 'Content-Length':
                http_headers[h] = get_random_int()
            elif h == 'Method':
                http_headers[h] = get_random_method()
            elif h == 'Path':
                http_headers = '1.1'
            elif h == 'Version':
                http_headers[h] = get_random_version()
            else:
                http_headers[h] = get_random_string()
    return http_headers

# reads json file and build ftp_headers dict
# le user a une liste de deux champs a remplir
# la cle est le "header" et sa valeur
# s'il donne que la clé alors la valeur est generee automatiquement
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
    print(ftp_headers)
    return ftp_headers

# Get a list of n random ftp commands
def get_random_ftp_command(n):
    rand = random.sample(range(0, len(ftp_commands)-1), n)
    ftps = []
    for i in rand:
        ftps.append(ftp_commands[i])
    return ftps

def get_random_int(size=10):
    i = 1
    s = '9'
    j = 0
    for j in range(1, size):
        i = i * 10
        s = s + '9'
    return random.randrange(i, int(s))

def get_random_string(size=10):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(size))

def get_random_method():
    return 'GET'

def get_random_path(size=3):
    letters = string.ascii_lowercase
    return '/'.join(random.choice(letters) for i in range(size))
