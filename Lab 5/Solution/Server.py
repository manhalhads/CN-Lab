#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import socket

def main():
    # Create a UDP socket
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Bind the socket to the server address and port
    server_address = ('127.0.0.1', 2000)
    sock.bind(server_address)

    print("Socket created and bound")
    print("Listening for messages...\n")
    checkedin = ['22L_7805_CI', '22L_8907_CI']

    while True:
        try:
            # Receive the message from the client
            client_message, client_address = sock.recvfrom(2000)
            msg = client_message.decode()
            checkout_msg = f"Welcome Student: {client_message.decode()}"
            #print(f"Received message from IP: {client_address[0]} and Port No: {client_address[1]}")
            
            size = len(msg)
            #check in mode
            if (msg[size-1] == 'I' and msg[size-2] == 'C'):

            #check if student already checked in
                for i in range(len(checkedin)):
                    if (checkedin[i] == msg):
                        checkout_msg = 'You are already here\n'   

                #mark attendance (check in)
                checkedin.append(msg);
                print("Marked attendance:" + msg)
                sock.sendto(str.encode(checkout_msg), client_address)

            elif (msg[size-1] == 'O' and msg[size-2] == 'C'):

                ci = 0
                remove_string = ''
                checkout_msg = 'You didn’t check in today. Contact System Administrator.\n'
                #check if student checked in before checking out
                for i in range(len(checkedin)):
                    string = checkedin[i]
                    if (string[:8] == msg[:8]):
                        ci = 1
                        remove_string = string
                        checkout_msg = 'GoodBye Student ' + msg +  '. Have a nice day.\n'
                        sock.sendto(str.encode(checkout_msg), client_address)
                        break

                if (ci == 1):
                     checkedin.remove(remove_string)
                     print('Checked out Student:' + msg + '\n')
            else:
                checkout_msg = 'Invalid input\n'
                sock.sendto(str.encode(checkout_msg), client_address)


        except Exception as e:
            print(f"An error occurred: {e}")
            break

    # Closing the socket
    sock.close()

if __name__ == "__main__":
    main()


# In[ ]:




