import socket

def main():

    ips = [
            "13.230.158.120",
            "18.179.245.253",
            "52.69.239.207",
            "13.209.163.61",
            "54.180.75.25",
            "13.233.76.15",
            "13.234.168.60",
            "13.250.168.23",
            "13.250.94.254",
            "54.169.195.247",
            "13.236.14.80",
            "13.238.54.232",
            "52.63.231.178",
            "18.229.199.252",
            "54.207.47.76"
           ]


    for ip in ips:
        print(ip)
        x = socket.socket()
        try:
           x.connect((ip, 443))
        except:
           print("fail ",ip)

if __name__ == "__main__":
    """ This is executed when run from the command line """
    main()
