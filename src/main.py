# -*- coding: utf-8 -*-
import subprocess
import socket 

class Ping(object):
    def __init__(self, hosts):
        for host in hosts:
            # pingコマンド
            ping = subprocess.Popen(["ping", "-c", "1", host],
                stdout=subprocess.PIPE,
                stderr=subprocess.PIPE
            )

            # ping試験
            out, error = ping.communicate()

            # 接続できなかったら
            if error:
                print('[NG]: ' +  host + ', Msg->\'' + error.rstrip() + '\'')

            # 接続できたら
            else:
                print('[OK]: ' +  host)
                print(ping.stdout)
                print(ping.stderr)

class Tcp(object):
    def __init__(self, hosts):
        for host in hosts:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
            result = sock.connect_ex((host, 80))
            if result == 0:
                print('[OK]: ' +  host)
            else:
                print('[NG]: ' +  host)

# ping試験するホスト
hosts = ['www.google.com', 'algorithm.joho.info',]

# ping試験
Tcp(hosts)
