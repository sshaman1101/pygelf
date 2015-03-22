from pygelf import Client

grey_host = '10.0.0.200'
grey_port = '12201'

info = Client(host=grey_host, port=grey_port, facility='INFO')
error = Client(host=grey_host, port=grey_port, facility='ERROR')

info.send('Application started')

# do some useful staff there...
error.send('Some error occupied!')
# and do some again

info.send('Exec finished.')