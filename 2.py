#2. Remove leading zeros from an IP address
import re                            
                                     
def remove_leading_zeros(ip_address):
    return re.sub(r'\b0+(\d)', r'\1',
                                     
ip = "192.168.001.002"               
print(remove_leading_zeros(ip))
