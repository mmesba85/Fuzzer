import random
import string

http_methods = ['GET', 'POST', 'HEAD', 'PUT']
ftp_commands = ["ABOR", "ACCT", "ADAT", "ALLO", "APPE", "AUTH", "CCC", "CDUP", "CONF", "CWD", "DELE", "ENC", "EPRT", "EPSV", "FEAT", "HELP", "LANG", "LIST", "LPRT", "LPSV", "MDTM", "MIC", "MKD", "MLSD", "MLST", "MODE", "NLST", "NOOP", "OPTS", "PASV", "PBSZ", "PORT", "PROT", "PWD", "REIN", "REST", "RETR", "RMD", "RNFR", "RNTO", "SITE", "SIZE", "SMNT", "STAT", "STOR", "STOU", "STRU", "SYST", "TYPE", "XCUP", "XMKD", "XPWD", "XRCP", "XRMD", "XRSQ", "XSEM", "XSEN"]

# reads file (yaml? json?) and build http_headers dict (comme le 
# dict de generate http input)
def build_http_input(file):
    print("TODO")

# prend un mot et lui append des lettres de taille 5
# generalement on reprend la premiere lettre ou la derniere
# lettre et cette meme lettre on la rajoute plusieurs fois (debut/fin)
def append_random(word, size=5):
    print("TODO")

# rajouter d'autres header?
# TODO:
# prendre en compte le fait que l'utilisateur puisse specifier
# vouloir fuzzer que certain champs
# il peut aussi proposer une chaine de caractere pour ces champs
def generate_http_input():
    http_headers = {}
    http_headers['Method'] = get_random_method()
    http_headers['Path'] = get_random_path()
    http_headers['Version'] = get_random_version()
    http_headers['Accept'] = get_random_string()
    http_headers['Accept_Charset'] = get_random_string()
    http_headers['Accept_Datetime'] = get_random_string()
    http_headers['Origin'] = get_random_string()
    http_headers['Content-Language'] = get_random_string()
    http_headers['Content-Encoding'] = get_random_string()
    if http_headers['Method'] == 'POST':
        http_headers['Content-Length'] = get_random_int()
        http_headers['Data'] = get_random_string(200)
    return http_headers

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
    print("TODO")

def get_random_path():
    print("TODO")

def get_random_version():
    print("TODO")

