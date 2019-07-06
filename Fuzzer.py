import argparse
import logging
import Worker
import Generator

# MAIN 

# NOT FINISHED
parser = argparse.ArgumentParser()
parser.add_argument("-H", type=str,
                    help="Host to fuzz", default='127.0.0.1')
parser.add_argument("-P", type=str,
                    help="Port that listens")
parser.add_argument("-T", type=str,
                    help="Protocol", choices=["FTP", "HTTP"], required=True)
parser.add_argument("-f", type=str,
                    help="Config file")
parser.add_argument("-l", type=str,
                    help="Log file", default='fuzz.log')
args = parser.parse_args()

if args.P is None:
    if args.T == 'FTP':
        args.P = 21
    else:
        args.P = 8080

if args.f is None:
    if args.T == 'FTP':
        data = Generator.get_random_string()
        # appel a la methode principale de fuzz
    else:
        http_headers = Generator.generate_http_input()
        Worker.http_fuzz(http_headers, args.H, args.P) #provisoire

logger = logging.getLogger()
handler = logging.FileHandler(args.l)
formatter = logging.Formatter(
        '%(asctime)s %(protocol)-12s %(host)-12s %(action)-8s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

