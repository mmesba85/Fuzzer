# Fuzzer

### Authors
* Mesbahi Maroua: maroua.mesbahi@epita.fr   
* Li Melissa: melissa.li@epita.fr


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

  ### Test
  Le répértoire ./tests contients deux serveurs de tests:
  * sws: serveur http
  * my_ftpd: serveur ftp

  Le répértoire racine contient de plus deux fichiers de configurations que l'utilisateur peut fournir en entrée du programme.
