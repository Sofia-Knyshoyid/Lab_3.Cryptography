# Lab_3.Cryptography
The laboratory work presents the implementation of terminal program
for exchanging the messages;

1. It works on the server-client principle,
the number of clients is not limited.

2. When a new user joins the server, the message
is sent to all those already on the server.

2. Uses RSA-algorithm for exchanging the encoded messages between the users.
The message integrity is ensured by the hash SHA512 function.

3. The following steps are processed in the program:
  - defining hash of the message
  - encoding the message
  - sending it as (hash, encrypted message)
  - decoding the message
  - comparing the hash of the message

4. There are two types of the messages: the general and the private ones;
The general are available to all the users on the server.
The private messages are redirected to a person confidentially.

5. Different variations of possible encoding/decoding were tested,
the examples can be seen in the relevant directory in this repository.
The final working model that was implemented is the coding of messages
consisting of capital letters only, both English and Ukrainian
