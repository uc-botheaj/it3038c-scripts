import socket, sys 

# print(sys.argv[0])

def getHostnameByIP(h):
  try:
    hostname = str(h)
    ip = socket.gethostbyname(hostname)
    print(hostname +' has an IP of ' + ip)
  except:
    print("oops, something is wrong with that host. No response.") 

getHostnameByIP(sys.argv[1]) 
