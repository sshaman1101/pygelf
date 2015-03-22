import socket
import json
import pycurl


class Client():
    def __init__(self, host=None, port=None, facility="INFO",  hostname=None):
        if not host and not port:
            raise Exception("Client must be init with host and port params.")

        self._host = host
        self._port = port
        self._endpoint = 'http://%s:%s/gelf' % (self._host, self._port)
        self._hostname = hostname or socket.gethostname()
        self._facility = facility

    def send(self, message):
        # create json object to send to Graylog
        content = {
            "short_message": message, 
            "facility": self._facility,
            "host": self._hostname,
            "_method": "Gelf HTTP",
        }
        
        try:
            c = pycurl.Curl()
            c.setopt(pycurl.URL, self._endpoint)
            c.setopt(pycurl.HTTPHEADER, ['Accept: application/json', 'Content-Type: application/json'])
            c.setopt(pycurl.POST, 1)
            c.setopt(pycurl.POSTFIELDS, json.dumps(content))
            # force HTTP 1.0 to bypass KeepAlive (Compliments of Lennart Koopmann)
            c.setopt(pycurl.HTTP_VERSION, pycurl.CURL_HTTP_VERSION_1_0)
            c.perform()
            c.close()
            print "Message logged via Gelf HTTP: " + json.dumps(content)
        except pycurl.error as e:
            print e

