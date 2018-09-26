# https://github.com/erdiaker/torrequest


# toTry:
# identity reset한 다음에 ip확인한뒤 접속 시도해보기

# torrequest는 어차피 stem을 가져다가 쓰는 모듈임


import time
import os
import random

from torrequest import TorRequest

from config import *


# Choose a proxy port, a control port, and a password.
# Defaults are 9050, 9051, and None respectively.
# If there is already a Tor process listening the specified
# ports, TorRequest will use that one.
# Otherwise, it will create a new Tor process,
# and terminate it at the end.


counter = 10

# os.system("sudo /etc/init.d/tor stop")
os.system("sudo service tor restart")
os.system("sudo service privoxy restart")

for i in range(10):
    with TorRequest(proxy_port=9050, ctrl_port=9051, password='my password') as tr:

        # for i in range(counter):

        # print(str(i)+': start')

        # Specify HTTP verb and url.
        resp = tr.get(siteURL)
        # print(resp.text)

        # Send data. Use basic authentication.
        # resp = tr.post('https://api.example.com',
        #   data={'foo': 'bar'}, auth=('user', 'pass'))'
        # print(resp.json)

        # Change your Tor circuit,
        # and likely your observed IP address.
        tr.reset_identity()

        # TorRequest object also exposes the underlying Stem controller
        # and Requests session objects for more flexibility.

        print(type(tr.ctrl))            # a stem.control.Controller object
        tr.ctrl.signal(NEWNYM) # see Stem docs for the full API

        # print(type(tr.session))         # a requests.Session object
        # c = cookielib.CookieJar()
        # tr.session.cookies.update(c)    # see Requests docs for the full API

        sleep_time = random.randint(31, 60)
        print('sleep_time: ' + str(sleep_time) + 's')

        # os.system("sudo service tor restart")
        # print('waiting 15 seconds..')
        # time.sleep(15)
        #
        print(str(i)+': done')
        print('')
