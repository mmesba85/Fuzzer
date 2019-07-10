import argparse
import logging
import Worker
import Generator


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
parser.add_argument("-run", type=int,
                    help="Number of runs", default=10)
parser.add_argument("-u", type=str,
                    help="FTP connection username", default="")
parser.add_argument("-pw", type=str,
                    help="FTP connection password", default="")
parser.add_argument("-msize", type=int,
                    help="Maximum size of the input", default=200)
parser.add_argument("-m", type=str,
                    help="Mutation technique", default="random", choices=['random', 'flip'])

args = parser.parse_args()

logger = logging.getLogger("mainlogger")
handler = logging.FileHandler(args.l)
formatter = logging.Formatter(
        '%(asctime)s %(levelname)-5s %(protocol)-5s %(host)-5s %(action)-5s %(message)s')
handler.setFormatter(formatter)
logger.addHandler(handler)
logger.setLevel(logging.DEBUG)

if args.P is None:
    if args.T == 'FTP':
        args.P = 21
    else:
        args.P = 8080

data = {}
if args.f is None:
    if args.T == 'FTP':
        data = Generator.generate_ftp_input(args.u, args.pw)
    else:
        data = Generator.generate_http_input()

else:
    if args.T == 'FTP':
        data = Generator.build_ftp_input(args.f)
    else:
        data = Generator.build_http_input(args.f)

if args.T == 'FTP':
    Worker.fuzz('ftp', data, args.H, args.P, args.run, args.msize, args.m)
else:
    Worker.fuzz('http', data, args.H, args.P, args.run, args.msize, args.m)



