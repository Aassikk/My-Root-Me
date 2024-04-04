from pwn import *
import math

# server IP adress and Port adress
server_ip = "challenge01.root-me.org"
server_port = 52002

# create socket type object 
client = remote(server_ip, server_port)

try:
    # receive seerver banner
    banner = client.recv()
    print(banner)
    
    # extract numbers from banner
    numbers = [ int(i) for i in banner.split() if i.isdigit()]
    print("Extracted numbers:", numbers)
    
    # calculate result
    res = round(math.sqrt(numbers[1]) * numbers[2], 2)
    print("Result of calculation=",res)
    
    # send answer to server
    client.sendline(str(res))

    # receive answer
    response = client.recv().decode()
    print("Response du serveur :", response)

except Exception as e:
    print("Erreur lors de la connexion au serveur :", e)

finally:
    # close connection with serverx
    client.close()
    print("Connexion fermÃ©e.")
