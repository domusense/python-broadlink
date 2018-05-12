import time
import broadlink

print ('Starting...')

# discover devices
devices = broadlink.discover(timeout=2, local_ip_address=None)

# we expect a single device on the network
d = devices[0]

print("IP: %s, port: %s, mac: %s, type: %s" % (d.host[0], d.host[1], ':'.join('%02x' % (b) for b in d.mac), d.type))
# authorize
d.auth()

# start sweep frequency mode. (Long press the source remote control)
input('Press Enter to start sweeping frequency')
d.sweep_frequency()
i = 1
iterations = 5 

# wait for lock frequency
while True:
  print('cycle %s of %s' % ((i, iterations)))
  time.sleep(2)
  if bool(d.check_frequency()):
    print ("Locked RF frequency")
    break
  if i >= iterations:
    print('freq sweep time out')
    break
  i=i+1

# get the command data
input('Press Enter to learn the RF command code')

i = 1
while True:
  print('cycle %s of %s' % ((i, iterations)))
  if d.find_rf_packet():
    break
  time.sleep(2)
  if i >= iterations:
    print('find_rf_packet time out')
    break
  data = d.check_data()
  if data != bytearray(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00') and data != None:
      break
  i=i+1

print("learned data info")

print(', '.join('%d' % (d) for d in data))
print(', '.join('%x' % (d) for d in data))
print(data)
input('Press Enter key to exit')


