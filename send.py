import time
import broadlink
import base64

print ('Starting...')

# discover devices
devices = broadlink.discover(timeout=2, local_ip_address=None)

# we expect a single device on the network
d = devices[0]

print("IP: %s, port: %s, mac: %s, type: %s" % (d.host[0], d.host[1], ':'.join('%02x' % (b) for b in d.mac), d.type))
# authorize
d.auth()

input('Hit Enter to send data')
cmd_b64 = "slw0AA0kDSQNJCQNJA0kDQ0kJA0NJCQNDSQNJCQNDSQkDQ0kJA0kDQ0kDSQNJA0kJA0kDQwAAW8AAAAA"
command = base64.b64decode(cmd_b64)
#command = b'\xb2\x80(\x00\x12\x04\x07\x05\x07\t\x0c\x05\x07\t\x07\x04\x07\x04\x07\x04\x07\x04\x0c\n\x07\x04\x07\x04\x07\x04\x0c\x05\x07\x05\x07\x05\x07\t\x08\x04\x07\x04\x07\x05'

d.send_data(command)

#prisnt(' '.join('%02x' % (d) for d in command))
#print(' '.join('%d' % (d) for d in command))
#print(command)
#input("press enter to send command to teach the switch")
#d.send_data(command)
#print("Test 1..")

#time.sleep(2)


#print("Test 2..")
#d.send_data(command)
#time.sleep(2)

#print("Test 3..")
#d.send_data(command)
#time.sleep(2)

#print("Test 4..")
#d.send_data(command)
#time.sleep(2)

