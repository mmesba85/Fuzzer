# Fuzzer

### Authors
* Mesbahi Maroua
* Li Melissa


### Usage
```
usage: Fuzzer.py [-h] [-H H] [-P P] -T {FTP,HTTP} [-f F] [-l L] [-run RUN]
                 [-u U] [-pw PW] [-msize MSIZE] [-m {random,flip}]

optional arguments:
  -h, --help        show this help message and exit
  -H H              Host to fuzz
  -P P              Port that listens
  -T {FTP,HTTP}     Protocol
  -f F              Config file
  -l L              Log file
  -run RUN          Number of runs
  -u U              FTP connection username
  -pw PW            FTP connection password
  -msize MSIZE      Maximum size of the input
  -m {random,flip}  Mutation technique
  ```
