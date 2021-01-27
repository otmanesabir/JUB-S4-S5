---
attachments: [connection-sharing.png, ip-tunneling.png, private_keyring.png, public_keyring.png, ssh-agent-forwarding.png, ssh-agent.png, ssh-connection-protocol.png, ssh-transport-protocol.png, ssh-user-authentication.png, tcp-forwarding.png, x11-forwarding.png]
tags: [SADS]
title: 5 Secure Communication Protocols
created: '2020-05-25T18:04:09.272Z'
modified: '2020-08-14T08:49:31.529Z'
---

# 5 Secure Communication Protocols

[//]: # (Primary = #BB86FC)
[//]: # (Secondary = #03DAC5)
[//]: # (Secondary = #FF0266)

This part illustrates how the cryptographic primitives introduced so far are used to secure communication over the internet. It is important to recall that the Internet was not designed with security in mind.

<h2 style="color:#BB86FC">Pretty Good Privacy (PGP)</h2>

* PGP was developed by Philip Zimmerman in 1991
* PGP got famous because it demonstrated why patent laws and export laws in a globalized connected world new interpretations.
* In order to export his PGP implementation, Philip Zimmerman did publish the code as a book.
* There are nowadays several independent PGP implementations.
* The underlying PGP specification is now called OpenPGP.
* An alternative to PGP is S/MIME, which relies centralized trust via X.509 certificates, while PGP relies on decentralized web of trust.

<h3 style="color:#03DAC5">PGP Signatures</h3>

To produce a signed message of a cleartext $m$
  1. a cryptographic hash is computed over $m$;
  2. the hash is encrypted using the signer's private key;
  3. the signed hash is appended to the cleartext;
  4. the resulting message is compressed.

To verify a signed message $c$
  1. the message $c$ is uncompressed;
  2. the message is split into the signature and the cleartext;
  3. a cryptographic hash is computed over $m$;
  4. the encrypted hash is decrypted with the signer's public key;
  5. the two hash values are compard.

PGP originally used the hash-function $MD5$, the public-key algorithm RSA and zlib compression. Newer versions support crypto agility.

<h3 style="color:#03DAC5">PGP Confidentiality</h3>

To produce an encrypted message of a cleartext $m$
  1. compress the message $m$;
  2. generate a key $K_s$;
  3. the compressed message is encrypted using the key $K_s$;
  4. the key $K_s$ is encrypted using the receiver's public key;
  5. the encrypted key is appended to the encrypted message.

To receive an encrypted message $c$
  1. the message is split into the encrypted key and the encrypted message;
  2. the encrypted key is decrypted using the receiver's private key;
  3. the encrypted message is decrypted using $K_s$;
  4. the resulting compressed message is decompressed.

PGP confidentiality combines symmetric encryption algorithms, which are fast on large inputs, with asymmetric encryption algorithms, which make it easy to identify communicating parties.

<h3 style="color:#03DAC5">PGP Signatures and Confidentiality</h3>

To send an encrypted message with the signature of the sender, the two previous algorithms are combined. All three schemes require that all communicating parties have access to the public keys and that they trust these keys to belong to the correct identity. Also note that protected messages can have a long lifetime during which (i) keys may simply get lost or (ii) keys may get stolen or broken.

<h3 style="color:#03DAC5">PGP Key Management</h3>

* Keys are maintained is so called key rings:
  * one key ring for public keys
  * one key ring for private keys
* keys are identified by their fingerprints.
* Key generation utilizes various sources of random information (/dev/random if available) and symmetric encryption algorithms to generate good key material.
* So called "key signing parties" are used ot sign keys of others and establish a "web of trust" in order to avoid centralized certification authorities.

<h3 style="color:#03DAC5">PGP Private Key Ring</h3>

![Icon](@attachment/private_keyring.png)

* Private keys are encrypted using $E_{H(P_i)}()$, which is a symmetric encryption function using a key which is derived from a hash value computed over a user supplied passphrase $P_i$.
* The Key ID is taken from the last 64 bits of the key $K_i$.

<h3 style="color:#03DAC5">PGP Public Key Ring</h3>

![Icon](@attachment/public_keyring.png)

* Keys in the public key ring can be signed by multiple parties. Every signature has an associated trust level:
  1. undefined trust
  2. usually not trusted
  3. usually trusted
  4. always trusted
* Computing a trust level for new keys which are signed by others (trusting others when they sign keys).


<h2 style="color:#BB86FC">Transport Layer Security</h2>

Transport Layer Security is probably the most widely used protocol to secure communication over the internet. Originally designed to enable commerce over the internet, it is used meanwhile for many other purposes, such as creating secure virtual private networks, to securely access email message stores, or to protect domain name lookups.

* Transport Layer Security (TLS), formerly known as Secure Socket Layer (SSL), was created by Netscape to secure data transfers on the Web.
* As a user-space implementation, TLS can be shipped as part of applications (Web browsers) and does not require operating system support.
* TLS uses X.509 certificates to authenticate servers and clients.
* TLS is widely used to secure application protocols running over TCP (http, smtp, ftp, telnet, ...)
* A datagram version of TLS called DTLS can be used with protocols running over UDP (dns, ...).

<h3 style="color:#03DAC5">History TLS and SSL</h3>

All TLS versions prior to TLS 1.2 are considered outdated at the time of this writing. Web browsers are moving towards disabling support for outdated TLS versions, which forces all sites still running old versions of TLS to upgrade to at least TLS 1.2.

<h3 style="color:#03DAC5">TLS Protocols</h3>

* The _Handshake Protocol_ authenticates the communicating parties, negotiates cryptographic modes and parameters, and establishes shared keying material.

* The _Alert Protocol_ communicates alerts such as closure alerts and error alerts.

* The _Record Protocol_ uses the parameters established by the handshake protocol to protect traffic between the communicating peers.
* The Record Protocol is the lowest internal layer of TLS and it carries the handshake and alert protocol messages as well as application data.


<h3 style="color:#03DAC5">TLS Record Protocol</h3>
<h4 style="color:#FF0266">Record Protocol</h4>

The record protocol takes messages to be transmitted, fragments the data into manageable blocks, optionally compresses the data, adds a message authentication code, and encrypts and transmits the results. Received data is decrypted, verified, decompressed, reassembled, and then delivered to higher-level clients.

* The record layer is used by the handshake protocol, the change cipher spec protocol, the alert protocol and the application data protocol.

<h4 style="color:#FF0266">TLS Handshake Protocol</h4>

* Exchange messages to agree on algorithms, exchange random number, and check for session resumption.
* Exchange the necessary cryptographic parameters to allow the client and server to agree on premaster secret.
* Exchange certificates and cryptographic information to allow the client and server to authenticate themselves.
* Generate a master secret from the premaster secret and the exchanged random numbers.
* Provide security parameters to the record layer.
* Allow client and server to verify that the peer has calculated the same security parameters and that the handshake completed without tampering by an attacker.

<h4 style="color:#FF0266">TLS Change Cipher Spec Protocol</h4>

The change cipher spec protocol is used to signal transitions in ciphering strategies.

* The protocol consists of a single ChangeCipherSpec message.
* This message is sent by both the client and the server to notify the receiving party that subsequent records will be protected under the newly negotiated CipherSpec and keys.
* This protocol does not exist anymore in TLS 1.3


<h4 style="color:#FF0266">TLS Alert Protocol</h4>

The alert protocol is used to signal exceptions (warnings, errors) that occured during the processing of TLS protocol messages.

* The _alert protocol_ is used to properly close a TLS connection by exchanging _close notify_ alert messages.
* The closure exchange allows to detect truncation attacks.

It is important that both parties involved in a TLS session properly terminate the session. The alert protocol can be used to signal to the remote party that no more data follows. Note that TLS close notification allows to determine which of the two communication parties initiates the teardown of the underlying TCP connection.

<h3 style="color:#03DAC5">Secure Shell (SSH)</h3>

* SSH provides a secure connection through which user authentication and several inner protocols can be run.
* The general architecture of SSH is defined in RFC 4251.
* SSH was quickly adopted as a replacement for insecure remote login protocol such as telnet or rlogin/rsh.
* Several commercial and open source implementations are available running on almost all platforms.
* SSH is a Proposed Standard protocol of the IETF since 2006.

<h3 style="color:#03DAC5">SSH Protocol Layers</h3>

1. The **Transport Layer Protocol** provides server authentication, confidentiality, and integrity with perfect forward secrecy.
2. The **User Authentication Protocol** authenticates the client-side user to the server.
3. The **Connection Protocol** multiplexes the encrypted data stream into several logical channels.

* SSH authentication is not symmetric!
* The SSH protocol is designed for clarity, not necessarily for efficiency (shows its academic roots).

<h3 style="color:#03DAC5">SSH Keys, Passwords, and Passphrases</h3>

* **Host Key**
  * Every server must have a public/private host key pair.
  * Host keys are used for server authentication.
  * Host keys are typically identified by their fingerprint.
* **User Key**
  * Users may have their own public/private key pairs, optionally used to authenticate users.
* **User Password**
  * Remote accounts may use passwords to authenticate users.
* **Passphrase**
  * Storage of a user's private key may be protected by a passphrase.

It is important to distinguish betwen the server's key (called thehost key) and user's keys (called the user key). Note that user authentication protocol can authenticate user's by their keys but also via other means such as simple traditional passwords. SSH often relies on leap-of-faith to build trust into a host key. When a user connects to a server for the first time, the server asks the user to verify the server's host key fingerprint.


<h3 style="color:#03DAC5">SSH Features: TCP Forwarding</h3>

![Icon](@attachment/tcp-forwarding.png)

* TCP forwarding allows users to tunnel unencrypted traffic through an encrypted SSH connection. 

Port forwarding can be used to tunnel a protocol over SSH. IN the example an SSH conncetion from Joe's local machine to example.com using the remote account _joe_ is established. The SSH sever then creates a tunnel and connects as a client to port 25 on example.com and it provides a listening endpoint on the Joe's local host on port 2000. Thus, if a program on Joe's local host connects to the local port 2000, it actually talks to the server on _example.com_ using port 25.

<h3 style="color:#03DAC5">SSH Features: X11 Forwarding</h3>

![Icon](@attachment/x11-forwarding.png)

* X11 forwarding is a special application of TCP forwarding allowing X11 clients on remote machines to access the local X11 server (managing the display and the keybaord/mouse).

A typical use case for TCP port forwarding (and likely the reason for inventing it in the first place) is the traditional X window system. The X Window System consists of an X server controlling the display, the keyboard, the pointing device etc. Applications providing a graphical user interface incorporate X clients that connect to an X server in order to draw on the display and to receive events from the X server. The X11 protocol details the information flow between an X server and connected X clients.

<h3 style="color:#03DAC5">SSH Features: Connection Sharing</h3>

![Icon](@../attachment/connection-sharing.png)

* New SSH connections hook as a new channel into an existing SSH connection, reducing session startup times (speeding up shell features such as tab expansion).

Since SSH can multiplex multiple channels, it is possible t create new SSH connections on top of existing connections. The benefit of this is greatly reduced connection startup time since no new security context needs to be established. Of course, as a slight downside, the connections share fate. That said, connection sharing provides a significant performance improvement in situations where many otherwise short-lived connections would be used. 


<h3 style="color:#03DAC5">SSH Features: IP Tunneling</h3>

![Icon](@attachment/ip-tunneling.png)

* Tunnel IP packets over an SSH connection by inserting tunel interfaces into the kernels and by configuring IP forwarding.

SSH tunneling generalizes SSH port forwarding even further. Instead of forwarding transport layer connections, SSH is now tunneling network layer IP packets. This essentially provides you with a simple virtual private network (VPN) solution over which you can securely send arbitrary IP traffic. Doing this, however, requires the permissions on both systems to create tunnel network interfaces and to configure IP layer routing as desired.


<h3 style="color:#03DAC5">SSH Features: SSH Agent</h3>

![Icon](@attachment/ssh-agent.png)

* Maintains client credentials during a login session so that credentials can be reused by different SSH invocations without further user interaction.

SSH user keys are usually stored in files that are encrypted using a key derived from a passphrase. When access to a user key is needed, the user is prompted for the passphrase. In order to reduce the number of times a user has to enter the passphrase, the SSH agent may store decrypted user keys in memory for a certain period of time.

From a user's perspective, when an SSH connection is created, the SSH client tries to talk to the local SSH agent in order to obtain the user's keys. It will fallback to ask the user for a passphrase in case the local SSH agent does not hold the user key or is not accessible. A common approach is to start an ssh-agent when a user starts a login session and to load the user keys when the first SSH connection is established.

<h3 style="color:#03DAC5">SSH Features: SSH Agent Forwarding</h3>

![Icon](@attachment/ssh-agent-forwarding.png)

* An SSH server emulates an SSH Agent and forwards requests to the SSH Agent of its client, creating a chain of SSH Agent delegations.

While a local SSH agent is already very convenient, it is possible to go one step further by forwarding the port providing access t the SSH agent to a remote system. This setup enables the user to access a remote system and from there to access further systems, always accessing the local SSH agent. This way, SSH connections can go over multiple hops in a very convenient way without having to store any user keys on intermediate systems.


<h3 style="color:#03DAC5">SSH Transport Protocol</h3>

![Icon](@attachment/ssh-transport-protocol.png)

The transport protocol (RFC 4253) provides strong encryption, server authentication, integrity protection, and optionally compression. The transport protocol typically runs over TCP. The key exchange protocol does automatic key re-exchange, usually after 1 GB of data have been transferred or after 1 hour has passed, whichever is sooner. The cryptographic primitives and the key exchange mechanisms have been extended several times since the publication of RFC 4235.

The SSH host key exchange identifies a server by its hostname or IP address and possibly port number. Other key exchange mechanisms use different naming schemes for a host. There are different key exchange algorithms such as Diffie-Hellman style key exchange or GSS-API style key exchange as well as different host key algorithms. 


<h3 style="color:#03DAC5">SSH User Authentication</h3>

![Icon](@attachment/ssh-user-authentication.png)

* The user authentication protocol iterates through a list of mechanisms until either authentication was successful or all mechanisms have failed.

The user authentication protocol (RFC 4252) executes after transport protocol initialization (key exchange) to authenticate the client to the server. There are several authentication methods and set of methods can be extended:

* Password (classic password authentication)
* Intercctive (challenge response authentication)
* Host-based (uses host key for user authentication)
* Public key (usually DSA or RSA keypairs)
* GSS-API (Kerberos / NETLM authentication)
* X.509 (traditional certificates)

Note that user authentication is client driven.


<h3 style="color:#03DAC5">SSH Connection Protocol</h3>

![Icon](@attachment/ssh-connection-protocol.png)

* The connection protocol has additional messages to handle control flow, error messages (equivalent of stderr), and end-of-file indicators.


The connection protocol (RFC 4254) allows clients to open multiple independent channels. All channels are multiplexed over a single secure SSH transport.
  * Channel requests are used to relay out-of-band channel specific date.
  * Channels are widely used for TCP forwarding.


<h3 style="color:#03DAC5">OpenSSH Privilege Seperation</h3>

* Privilege seperation is a technique in which a program is divided into parts which are limited to the specific privileges they require in order to perform a specific task.

* OpenSSH is using two processes: one running with special privileges and one running under normal user priviliges.

* The process with special privileges carries out all operations requiring special permissions.

* The process with normal user privileges performs the bulk of the computation not requiring special rights.

* Bugs in the code running with normal user privileges do not give special access rights to an attacker.


The widely used OpenSSH implementation uses privilege seperation to minimize the amount of code executed with special privileges. While privilege seperation has some implementation costs, it is a very effective way to improve the security of complex server software. You can see privilege at work when you access a remote system and look at the process tree.


<h2 style="color:#BB86FC">DNS Security Extensions (DNSSEC)</h2>


The DNS essentially implements a mapping of DNS names to typed resource records. The resource records of the same type linked to the same name from a resource record set.

To sign a DNS zone, it is necessary to first create an asymmetric public/private key pair. The public key is stored in a DNSKEY resource record. Using the private key, different resource record sets of a zone are signed.

To obtain trust in the public key, a parent zone can use a DS resource record to reference a public key in a child zone.

The most common configuration for signed zones is to have two keys.
* The first key is called the Key Signing Key (KSK). This key is the secure entry point for the zone and is only used to generate a signatureover the DNSKEY RRset.

* The second key is called the ZOne Signing Key (ZSK). This key is used to generate the actual signatures over the RRsets in the zone.

Next to sign records in a zone, DNSSEC also generates cryptographically signed proofs of non-existence. These allow validators to verify that the name and record type in a query, for which they have received an NXDOMAIN response, do indeed not exist. However, different proposals have been made and work is still in progress to find a "good" solution.

