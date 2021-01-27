---
attachments: [cipher_blockChaining_mode.png, counter_mode.png, electronic_codebook_mode.png, merkle-damgard.png, needham_protocol.png, output_feedback_mode.png, substitution_perm_network.png]
tags: [SADS]
title: 4 Cryptography
created: '2020-05-25T18:03:56.813Z'
modified: '2020-05-28T07:10:15.047Z'
---

# 4 Cryptography

[//]: # (Primary = #BB86FC)
[//]: # (Secondary = #03DAC5)
[//]: # (Secondary = #FF0266)

This part introduces basic concepts of cryptography. The goal is to cover a minimum that is needed to understand how cryptography can be use later on to secure communication protocols or to more generally protect information.

<h2 style:color="#BB86FC">Terminology - Cryptography</h2>

* _Cryptology_ subsumes cryptography and cryptanalysis:
  * _Cryptography_ is the art of secret writing.
  * _Cryptanalysis_ is the art of breaking ciphers.

* _Encryption_ is the process of converting _plaintext_ into unreadable form, termed _ciphertext_.

* _Decryption_ is the reverse process, recovering the plaintext back from the ciphertext.

* A _cipher_ is an algorithm for encryption and decryption.

* A _key_ is some secret piece of information used as a parameter of a cipher and customizes the algorithm used to produce ciphertext.


It is important that the security of a cryptosystem rests on the secrecy of the keys and not on the secrecy of the algorithms. The algorithms of good cryptosystems should be publically known and withstand any attempts to break them.

The following rules should be followed:
  1. You should not keep your algorithm secret.
  2. You do not know how much your algorithm is secret.
  3. You cannot keep your algorithm secret. 
  4. You must keep your password secret, and you can know and control how secret it is.

<h2 style="color:#BB86FC">Cryptosystem - Cryptography Primer</h2>
<h3 style="color:#03DAC5">Definition</h3>

A _cryptosystem_ is a quintuple $(M, C, K, E_k, D_k)$, where
  * $M$ is a cleartext space,
  * $C$ is a chiffretext space,
  * $K$ is a key space,
  * $E_k : M \rightarrow C$ is an encryption transformation with $k \in K$, and
  * $D_k : C \rightarrow M$ is a decryption transformation with $k \in K$.

For a given $k$ and all $m \in M$, the following holds:

$D_k(E_k(m)) = m$

The defintiion is not yet complete. We want cryptosystems to satisfy certain requirements since we do not want simple functions that are easy to revert.

<h3 style="color:#03DAC5">Cryptosystem Requirements</h3>

* The transformations $E_k$ and $D_k$ must be efficient to compute.
* It must be easy to find a key $k \in K$ and functions $E_k$ and $D_k$.
* The security of the system rests on the secrecy of the key and not on the secrecy of the transformations $E_k$ and $D_k$ (the algorithms).
* For a given $c \in C$, it is difficult to systematically compute
  * $D_k$ even if $m \in M$ with $E_k = c$ is known
  * a cleartext $m \in M$ such that $E_k(m) = c$ 
* For a given $c \in C$, it is difficult to systematically determine
  * $E_k$ even if $m \in M$ with $E_k(m) = c$ is known
  * $c^` \in C$ with $c^` \neq C$ such that $D_k(c^`)$ is a valid cleartext $M$.


<h3 style="color:#03DAC5">Symmetric vs. Asymmetric Cryptosystems</h3>

<h4 style="color:#FF0266">Symmetric Cryptosystems</h4>

* Both (all) parties here share the same key and the key needs to be kept secret.

<h4 style="color:#FF0266">Asymmetric Cryptosystems</h4>

* Each party has a pair of keys: one key is public used for encryption while the other key is private and used for decryption.

* For asymmetric cryptosystems, a key is a key pair $(k, k^{-1})$ where $k$ denotes the public key and $k_{-1}$ and the associated private key.


<h3 style="color:#03DAC5">Cryptographic Hash Functions</h3>
<h4 style="color:#FF0266">Definition</h4>

A _cryptographic hash function_ $H$ is a hash function that meets the following requirements:

1. The hash function $H$ is efficient to compute for arbitrary input $m$.
2. Given a hash value $h$, it should be difficult to find an input $m$ such that $h = H(m)$.
3. Given an input $m$, it should be difficult to find another input $m^` \neq m$ such that $H(m) = H(m^`)$
4. It should be difficult to find two different inputs $m$ and $m^`$ such that $H(m) = H(m^`)$ (collision resistance).

<h3 style="color:#03DAC5">Digital Signatures</h3>

* Digital signatures are used to prove the authenticity of a message (or ducoment) and its integrity.
  * The receiver can verify the claimed identity of the sender (authentication).
  * The sender can not deny that he did send the message.
  * The receiver can verify that the message was not tampered with.

* Digitally signing a message (or document) means that
  * the sender puts a signature into a message (or document) that can be verified.
  * that we can be sure that the signature cannot be faked (e.g., copied from some other message).

* Digital signatures are often implemented by signing a cryptogrpahic hash of the original message (or document) since this is usualy computationally less expensive.


<h3 style="color:#03DAC5">Usage of Cryptography</h3>

* Encrypting data in communication protocols (prevent eavesdropping)
* Encrypting data elements of files (e.g., passwords stored in a database)
* Encrypting entire files (prevent data leakage if machines are stolen or attacked)
* Encrypting entire file systems (prevent data leakage if machines are stolen or attached.)
* Encrypting backups stored on 3rd party storage systems
* Encrypting digital media to obtain revenue by selling keys (for example pay TV)
* Digital signatures of files to ensure that changes of file content can be detected or that the content of a file can be proven to originate from a certain source. 
* Encrypted token needed to obtain certain services or to authorize transactions.
* Modern electronic currencies (cryptocurrency).

<h2 style="color:#BB86FC">Cryptosystem - Symmetric Encryption Algorithms & Block Ciphers</h2>

<h3 style="color:#03DAC5">Substitution Ciphers</h3>

<h4 style="color:#FF0266">Definition</h4>

A _monoalphabetic substitution cipher_ is a bijection on the set of symbols of an alphabet. A _polyalphabetic substitution cipher_ is a substitution cipher with multiple bijections, i.e., a collection of monoalphabetic substitution ciphers.

* There are $| M |!$ different bijections of a finite alphabet $M$.
* Monoalphabetic substitution ciphers are easy to attack via frequency analysis since the bijection does not change the frequency of cleartext characters in the ciphertext.
* Polyalphabetic substitution ciphers are still relatively easy to attack if the length of the message is significantly longer than the key.


Lets represent all data as a number in $\Z_n$. Then we can consider monoalphabetic cryptosystems $M = \Z_n, C = \Z_n, M = \Z, E_k, D_k$ with 

$E_k(m) = (m + c) mod n$
$D_k(c) = (c - k) mod n$

with $m \in M$, $c \in C$ and $k in K$. This kind of cryptosystem is known as Ceaser cipher. The $rot_{13}$ cipher is essentially a monoalphabetic substitution cipher with the key $k = 13$ fior the $n = 26$ latin characters (applied to lower-case and upper-case characters independently, leaving all other characters unchanged).

Lets represent all data as a number in $\Z_n$. Then we can consider monoalphabetic cryptosystems $M = \Z_n, C = \Z_n, M = \Z, E_k, D_k$ with

$E_k(i, m) = (m + k_{(i mod l)}$ mod $n$
$D_k(i, c) = (c - k_{(i mod l)}$ mod $n$

with $m \in M$, $c \in C$ and $k_i \in K$. The position $i$ of the input symbol $m$ in the cleartext determines which element of the key vector $k = (k_0, ..., k_{l-1}$ is used. The Vinigére cipher splits a message into $n$ blocks of a certain length $l$ and then each symbol of a block is encrypted using a Caeser cipher with a different key $k_i$ depending on the position of the symbol in the block.

<h3 style="color:#03DAC5">Permutation Cipher</h3>

<h4 style="color:#FF0266">Definition</h4>

A _permutation cipher_ maps a plaintext $m_0, ..., m_{\delta(l-1)}$ where $\delta$ is a bijection of the positions 0,...,l-1 in the message.

* Permutation ciphers are also called transposition ciphers.
* To make the cipher parametric in a key, we can use a function $\delta_k$ that maps a key $k$ to bijections.


<h3 style="color:#03DAC5">Prodcut Cipher</h3>

<h4 style="color:#FF0266">Definition</h4>

A _product cipher_ combines two or more ciphers in a manner that  the resulting cipher is more secure than the individual components to make it resistant to cryptanalysis.

* Combining multiple substitution ciphers results in another substitution cipher and hence is of little value.
* Combining multiple permutations ciphers result in another permutation cipher and hence is of little value.
* Combining substitution ciphers with permutation ciphers gives us ciphers that are much harder to break.


Product ciphers are very important as they are the common foundation of many symmetric cipher algorithms. A specific class of product ciphers are so Feistel ciphers, named after the physicist and cryptographer Horst Feistel. Feitel ciphers work in rounds and in every round a key $k_i$ is used. The sequence of keys $k_i$ is typically generated from a key $k$ using a key generator.

<h3 style="color:#03DAC5">Chosen-Plaintext and Chosen-Ciphertext Attack</h3>

<h4 style="color:#FF0266">Defintion - CPA</h4>
In a _chosen-plaintext attach_ the adversary can chose arbitrary cleartext messages $m$ and feed them into encryption function $E$ to obtain the corresponding ciphertext.


<h4 style="color:#FF0266">Defintion - CCA</h4>
In a _chosen-ciphertext attack_ the adversary can chose arbitrary ciphertext $c$ and feed them into the decryption function $D$ to obtain the corresponding cleartext.

<h3 style="color:#03DAC5">Polynomial and Negligible Functions</h3>

<h4 style="color:#FF0266">Defintion</h4>

A function $f : \N \rightarrow \R^+$ is called
* polynomial if $f \in O(p)$ for some polynomial $p$
* super-polynomial if $f \notin O(p)$ for every polynomial $p$
* negligible if $f \in O(1 / |p|)$ for every polynomial $p : \N \rightarrow \R^+$

In modern cryptography, a security scheme is provably secure if the probability of security failure is negligible in terms of the cryptographic key length $n$. 

<h3 style="color:#03DAC5">Polynomial Time and Probabilistic Algorithms</h3>

<h4 style="color:#FF0266">Defintion - Polynomial Time</h4>

An algorithm $A$ is called _polynomial time_ if the worst-case time complexity of $A$ for input of size $n$ is a polynomial function.

<h4 style="color:#FF0266">Defintion - Probabilistic Algorithm</h4>

A _probabilistic algorithm_ is an algorithm that may return different results when called multiple times for the same input.

<h4 style="color:#FF0266">Defintion - Probabilistic Polynomial time</h4>

A _probabilistic polynomial time_ (PPT) algorithm is a probabilistic algorithm with polynomial time.


<mark>NOTES HAVE MORE DETAIL</mark>

<h3 style="color:#03DAC5">One-way Functions</h3>

<h4 style="color:#FF0266">Defintion</h4>

A function $f : \{0, 1\}^* \rightarrow \{0, 1\}^*$ is a _one-way_ function if and only if $f$ can be computed by a polynomial time algorithm, but any polynomial time randomized algorithm $F$ that attempts to computes a pseudo-inverse for $f$ succeeds with negligible probability.

One-way functions are super-polynomial hard to invert. Any algorithm $A$ that attempts to guess an $x \in \{ 0, 1 \}^n$ such that $y$ and $A(n, y)$ behave the same way under $f$ succeeds with negligible probability.


<h3 style="color:#03DAC5">Security of Ciphers</h3>

* What does it mean for an encryption scheme to be secure? Well consider an adversary who can pick two plaintexts $m_0$ and $m_1$ and who randomly receives either $E(m_0)$ or $E(m_1)$. An encryption scheme can be considered secure if the adversary cannot distinguish between the two situations with a probability that is non-negligibly better than $1/2$.


<h3 style="color:#03DAC5">Block Cipher</h3>

<h4 style="color:#FF0266">Defintion</h4>

A _block cipher_ is a cipher that operates on fixed-length groups of bits called a block. 

* A given variable-length plaintext is split into blocks of fixed size and then each block is encrypted individually.
* The last block may need to be padded using zeros or random bits.
* Encrypting each block individually has certain shortcomings:
  * the same plaintext block yields the same ciphertext block
  * encrypted blocks can be rearranged and the receiver may not necessarily detect this.

<h4 style="color:#FF0266">Electronic Codebook Mode</h4>

![Icon](@attachment/electronic_codebook_mode.png)

Electronic codebook mode simply slices the input into a sequence of blocks that are all encrypted in isolation :

* Encryption parallelizable: Yes
* Decryption parallelizable: Yes
* Random read access: Yes
* Lack of diffusion


<h4 style="color:#FF0266">Cipher Block Chaining Mode</h4>

![Icon](@attachment/cipher_blockChaining_mode.png)

The cipher block chaining mode feeds the ciphertext of block $b_i$ into the encryption of the subsequent block $b_{i+1}$.

* Encryption parallelizable: No
* Decryption parallelizable: Yes
* Random read access: Yes

The initialization vector does not have to be secret but it needs to be random and it is ideally only used once. A random number only used once is called a nonce. The sender has to communicate the initialization vector used to the receiver alongside the encrypted message. An alternative is for the receiver to discard the first block of data.


<h4 style="color:#FF0266">Output Feedback Mode</h4>

![Icon](@attachment/output_feedback_mode.png)


The output feedback mode of operation turns a block cipher into a stream cipher. A stream cipher is a symmetric key cipher where cleatext symbols are combined with pseudorandom cipher stream. The chained block ciphers generate a keystream and the cleartext is XORed with the keys. The encryption and decryption work in exactly the same way in output feedback mode :

* Encryption parallelizable: No
* Decryption parallelizable: No
* Random read access: No


<h4 style="color:#FF0266">Counter Mode</h4>

![Icon](@attachment/counter_mode.png)

The counter mode improves the main shortcomings of output feedback mode, namely that it is sequential and does not support random access.

* Encryption parallelizable: Yes
* Decryption parallelizable: Yes
* Random read access: Yes


<h3 style="color:#03DAC5">Substitution-Permutation Networks</h3>

<h4 style="color:#FF0266">Definition</h4>

A _substitution-permutation network_ is a block cipher whose bijections arise as products of substitution and permutation ciphers.

* To process a block of $N$ bits, the block is typically devided into $b$ chunks of $n = N / b$ bits each.
* Each block is processed by a sequence of rounds:
  * Key step: A key step maps a block by xor-ing it with a round key.
  * Substitution step: A chunk of $n$ bits is substituted by a substitution box (S-box).
  * Permutation step: A permutation box (P-box) permutes the bits received from S-boxes to produce bits for the next round.

We can take the sketch of a substitution-permutation network with three rounds, encrypting a plaintext block of 16 bits into a ciphertext block of 16 bits. Each S-box processes 4 bits of input while P-box permutates all 16bits. 

![Icon](@attachment/substitution_perm_network.png)

The goal of a substitution-permutation networks is to achieve good diffusion and confusion. Diffusion means that changing a single bit of the cleartext should change (statistically) half of the bits in the ciphertext. In other words, even small changes of the cleartext lead to drastic changes of the ciphertext. Confusion means that every bit of the ciphertext should depend on several bits of the key. This obscures the connections between the two. In the last round, the permutation step is often replaced by another key step.


<h3 style="color:#03DAC5">Advanced Encryption Standard</h3>

The $Advanced Encryption Standard$ is the most widely used symmetric cipher today. Even though the term "standard" in its name only refers to US government applications, the AES block cipher is also mandatory in several industry standards and is used in many commercial systems.

<h4 style="color:#FF0266">Advanced Encryption Standard Rounds</h4>

* Round 0:
  1. key step with $k_0$.
* Round 1: (i = 1, ..., r-1)
  1. substitution step (called sub-bytes) with fixed 8-bit S-box (used 16 times)
  2. permutation step (called shift-row) with a fixed permutation of 128 bits.
  3. substitution step (called mix-columns) with a fixed 32-bit S-box (used 4 times).
  4. key step (called add-round-key) with a key $k_i$.
* Round r: (no mix-columns)
  1. substitution step (called sub-bytes) with fixed 8-bit S-box (used 16 times).
  2. permutation step (called shift-row) with a fixed permutation of 128 bits.
  3. key step (called add-round-key) with a key $k_r$.


The round keys $k_0, ..., k_r$ are generated by a key generator (also know as a key schedule) from the key $k$ provided by the user of the algorithm. The AES algorithm is so widely used that computer hardware often provides hardware support for AES.

<h2 style="color:#BB86FC">Cryptosystem - Assymetric Encryption Algorithms</h2>

* Assymetric encryption schemes work with a key pair:
  * a public key used for encryption
  * a private key used for decryption
* Everybody can send a protected message to a receiver by using the receiver's public key to encrypt the message. Only the receiver knowing the marching private key will be able to decrypt the message.
* Assymetric encryption schemes give us a very easy way to digitally sign a message: A message encrypted by a sender with the sender's private key can be verified by any receiver using the sender's public key.

One inherent challenge associated with asymmetric encryption algorithms is the association of public keys with a certain identity. If Bob wants to send Alice an encrypted message, Bob first needs to obtain Alice's public key. If Mallory can interfere in this process and provide his public key instead of Alice's key, then Mallory will be able to read the message.

Another challenge associated with asymmetric encryption algorithms is the revocation of keys. If for some reason Alice has lost her private key, then the associated public key should not be used anymore and any data signed with Alice's private key should not be trusted anymore. Hence, there need to be mechanisms to revoke keys and check whether a key has been revoked.

<h3 style="color:#03DAC5">Ravist-Shamir-Adleman (RSA)</h3>

<h4 style="color:#FF0266">General Definition</h4>


* Key generation:
  1. Generate two large prime numbers $p$ and $q$ of roughly the same length.
  2. Compute $n = pq$ and $\varphi(n) = (p-1)(q-1)$.
  3. Choose a number e satisfying $1 < e < \varphi(n)$ and $gcd(e, \varphi(n)) = 1$.
  4. Compute $d$ satisfying $1 < d < \varphi(n)$ and $ed mod \varphi(n) = 1$.
  5. The public key is $(n, e)$, the private key is $(n, d);$ $p$, $q$ and $\varphi(n)$ are discarded.
* Encryption:
  1. The cleartext $m$ is represented as a sequence of numbers $m_i$ with $m_i \in \{ 0,1, ..., n - 1 \}$ and $m_i \neq p$ and $m_i \neq q$.
  2. Using the public key $(n ,e)$ compute $c_i = m_i^e mod n$ for all $m_i$.
* Decryption:
  1. Using the private key $(n, d)$ compute $m_i = c_i^d$ mod $n$ for all $c_i$.
  2. Transform the number sequence $m_i$ back into the original cleartext $m$.

 
<h4 style="color:#FF0266">Example</h4>

* Key generation:
  1. We choose the prime numbers $p = 47$ and $q = 71$.
  2. We compute $n = p \times q = 3337$ and $\varphi(n) = (p - 1).(q - 1) = 46 * 70 = 3220$.
  3. We randomly choose $e = 79$ for which $gcd(79, 3220) = 1$.
  4. We compute $d = 1019$ satisfying $ed mod 3220 = 1$
  5. The public key is (3337, 79) and the private key is (3337, 1019).
* Encryption:
  1. The cleartext RSA is converted into the cleartext numbers $m_i = [82, 83, 65]$
  2. Using the encryption key (3337, 79), we compute
  $c_0 = 82^{79} mod 3337 = 274$
    .
    .
    .
  and we obtain the cipher text numbers $c_i = [274, 2251, 541]$.

* Decryption:
  1. Using the decryption key $(3337, 1019)$,we compute
  $m_0 = 274^{1019} mod 3337 = 82$
    .
    .
  and we obtain the cleartext numbers $m_i = [82, 83, 65]$
  2. Converting the cleartext numbers back into a string, we get back $RSA$. 

<h3 style="color:#03DAC5">RSA - Math Background</h3>
<h4 style="color:#FF0266">Definition (coprime)</h4>

Two integers $a$ and $b$ are coprime if the only positive integer that divides both is 1.

<h4 style="color:#FF0266">Definition (Euler function)</h4>

The function $\varphi(n) = |\{a \in \N | 1 \leq a \leq n \wedge gcd(a, n) = 1\}|$ is called the Euler function.


<h4 style="color:#FF0266">Theorem (Euler's theorem)</h4>

If $a$ and $n$ are coprime, then $a^{\varphi(n)} \equiv (mod n)$.

<h4 style="color:#FF0266">Theorem</h4>

Let $m$ and $n$ be coprime integers. Then $\varphi(n . m) = \varphi(n) . \varphi(m)$.
If $p$ is a prime number, then $\varphi(p) = p - 1$.


<h3 style="color:#03DAC5">RSA Properties</h3>

* Security relies on the problem of factoring very large numbers.
* Quantum computers may solve this problem in polynomial time - so RSA will become obsolete once someone manages to build quantum computers.
* The prime numbers $p$ and $q$ should be at least 1024 (better 2048) bit long and not be too close to each other (otherwise an attacker can search in the proximity of $\sqrt(n)$
* Since two identical cleartexts $m_i$ and $m_j$ would lead to two identical ciphertexts $c_i$ and $c_j$, it is advisable to pad the cleartext numbers with random digits.
* Large prime numbers can be found using probabilistic prime number tests.
* RSA encryption and decryption is compute intensive and hence usualy used only on small cleartexts.


<h3 style="color:#03DAC5">Elliptic Curve Cryptography (ECC)</h3>

<h4 style="color:#FF0266">Definition</h4>

An _elliptic curve_ is a plane curve over a finite field which consists of the points 

$E = \{ (x, y) | y^2 = x^3 + ax = b \} \cup \{ \inf \}$

* Is it possible to define $R = P + Q$ with $R, P, Q$ on an elliptic curve $E$.
* With the addition defined, it is possible to define scalar multiplication $k . p$
* Given P and $k$, it is efficient to calculate $Q = k . P$
* Given $Q$ and $P$, it is difficult to find $k$ such that $Q = k . P$


<h2 style="color:#BB86FC">Cryptographic Hash Functions</h2>

<h3 style="color:#03DAC5">Cryptographic Hash Functions</h3>

* Cryptographic hash functions serve many purposes:
  * data integrity verification
  * integrity verification and authentication
  * calculation of fingerprints for efficient digital signatures
  * adjustable proof of work mechanics
* A cryptographic hash function can be obtained from a symmetric block encryption algorithm in cipher-block-chaining mode by using the last ciphertest block as the hash value.
* It is possible to construct more efficient cryptographic hash functions.ç


<h3 style="color:#03DAC5">Merkle-Damgard Construction</h3>


![Icon](@attachment/merkle-damgard.png)

* The message is padded and postfixed with a length value.
* The function $f$ is a collision-resistant compression function, which compresses a digest-sized input from the previous step (or the initialization vector) and a block-sized input from the message into a digest-sized value.


<h3 style="color:#03DAC5">Hashesd Message Authentication Codes</h3>

* A keyed-hash message authentication code (HMAC) is a specific type of message authentication code (MAC) involving a cryptographic hash function and a secret cryptographic key.
* An HMAC can be used to verify both data integrity and authenticity.
* An HMAC does not encrypt the message.
* The message must be sent alongside the HMAC hash. Parties with the secret key will hash the message again themselves, and if it is authentic, the receivd and computed hashes will match.


<h3 style="color:#03DAC5">HMAC Computation</h3>

Given a key $k$, a hash function $H$, and a message $m$, the HMAC using $H$ ($HMAC_H$) is calculated as follows:

$HMAC_H(k, m) = H((k^` \oplus opad) || H(k^` \oplus ipad) || m))$


* They key $k^`$ is derived from the original key $k$ by padding $k$ to the right with extra zeroes to the input block size of the hash function, or by hashing $k$ if it is longer than that block size.

* The $opad$ is the outer padding (0x5c5c5c ... 5c), one-block-long hexadecimal constant). The $ipad$ is the inner padding (0x363636...36, one-block-long hexadecimal constant).
 
* The symbol $\oplus$ denotes bitwise exclusive or and the symbol $||$ denotes concatenation.


<h3 style="color:#03DAC5">Authenticated Encryption with Associated Data</h3>

* It is often necessary to combine encryption with authentication of the data.
* Encryption protects the data and a message authentication code (MAC) protects the data against attempts to insert, remove, or modify data.
* Let $E_k$ be an encryption function with key $k$ and $H_k$ a hash-based MAC with key $k$ and $||$ denotes concatenation.
* Encrypt-then-Mac (EtM): $E_k(m) || H_k(E_k(M))$
* Encrypt-and-Mac (EaM): $E_k(m) || H_k(m)$
* Mac-then-Encrypt (MtE): $E_k(m || H_k(M))$


This part basically talks about authenticated encryption. The associated data is additional plaintext data that is not encrypted but covered by the hash. This is a common situation in communication protocols where the payload carried in messages is encrypted while some additional message fields remain unencrypted in order to organize forwarding of the messages. In addition, it is often required to ensure that messages are "fresh", i.e not a replay of some old messages. Hence, the AEAD interface defined in RFC 5116 consists of two functions :

$enc : (K \times N \times P \times A) \rightarrow C$
$dec : (K \times N \times C \times A) \rightarrow P$

where $k$ is a key, $N$ is a nonce (a random distinct unused value), $P$ is some plaintext, $A$ is associated data, and $C$ is ciphertext. Newer security protocols usually use AEADs instead of basic cryptographic algorithms.

The different AEAD techniques have different properties. In general, Encrypt-then-Mac is preferred by most cryptographers since it protects against chose ciphertext attacks and avoids any confidentiality issues arising from the MAC of the cleartext message.


<h2 style="color:#BB86FC">Digital Signatures and Certificates</h2>

<h3 style="color:#03DAC5">Digital Signatures</h3>

* Digital signatures are used to prove the authenticity of a message (or document) and its integrity.
  * Receiver can verify the claimed identity of the sender (authentiation)
  * The sender can later not deny that he/she sent the message (non-repudiation)
  * The message cannot be modified with invalidating the signature (integrity)
* A digital signature means that
  * the sender puts a signature into a message (or document) that can be verified and
  * that we can be sure that the signature cannot be faked (e.g., copied from some other message)
* Do not confuse digital signatures, which use cryptographic mechanisms, with electronic signatures, which may just use a scanned signature or a name entered into a form.

<h3 style="color:#03DAC5">Digital Signatures using Asymmetric Cryptosystems</h3>

* Direct signature of a document $m$:
  * Signer: $S = E_{k^{-1}}(m)$
  * Verifier: $D_k(S) =^? m$
* Indirect signature of a hash of a document $m$:
  * Signer: $S = E_{k^{-1}}(H(m))$
  * Verifier: $D_k(S) =^? H(m)$
* The verifier needs to be able to obtain the public key $k$ of the signer from a trustworthy source.
* The signature of a hash is faster (and hence more common) but it requires to send the signature $S$ along with the document $m$.


In practice, digital signaturesmost often work with hashes of documents, i.e., they are indirect signatures. Instead of signing a potential long electronic document, a cryptographic hash is calculated and then signed with the signer's private key. The received document and the signature can verify the signature by obtaining the signer's public key, calculating the has of the document, and comparing the decrypted signature with the locally calculated hash. 

Digital signatures using asymmetric cryptosystems are in general simple but the catch is that the verifier needs to obtain and trust the signer's public key. If Mallory creates a key pair and she manages to make Bob believe that the public part of the key pair belongs to Alice, then she can send messages under the identity of Alice and Bob will believe them to be authentic. Another problem arises if private keys are leaked or broken(or expired). Such an event can effectively turn all past signatures useless. So bob not only needs to trust that Alice's key is in fact Alice's key, he also need to verify at the time he uses the key that the key is still valid and has not been revoked yet. This all turns something that is concecptually simple into something that is astonishingly complex.

<h3 style="color:#03DAC5">Public Key Certificates</h3>

<h4 style="color:#FF0266">Definition - Public key certificate</h4>

A _public key certificate_ is an electronic document used to prove the ownership of a public key. The certificate includes
  * information about the public key, 
  * information about the identity of its owner (called the subject),
  * information about the lifetime of the certificate, and
  * the digital signature of an entity that has verified the certificate's contents. (called the issuer of the certificate).

* If the signature is valid, and the software examining the certificate trusts the issuer of the certificate, then it can trust the public key contained in the certificate to belong to the subject of the certificate.

<h3 style="color:#03DAC5">Public Key Infrastructure</h3>

<h4 style="color:#FF0266">Definition</h4>

A _public key infrastructure_ (PKI) is a set of roles, policies, and procedures needed to create, manage, distribute, use, store and revoke digital certificates and manage public-key enccryption.

* A central element of a PKI is the certificate authority (CA), which is responsible for storing, issuing and signing digital certificates.
* CAs are often hierarchically organized. A root CA may delegate some of the work to trusted secondary CAs if they execute their tasks according to certain rules defined by the root CA.
* A key function of a CA is to verify the identity of the subject (the owner) of a public key certificate.

<mark>skim detailed implementations of some certificates</mark>

<h3 style="color:#03DAC5">Automatic Certificate Management Environment (ACME)</h3>

* The ACME protocol provides so called Domain Validation certificates.
* It is a challenge-response protocol that aims to verify whether the client has effective control over a domain.
* The CA might challenge a client requesting a certificate for $example.com$
  * to provision a DNS record under $example.com$ or
  * to provide an HTTP resource under $http://example.com$
* ACME runs over HTTPS and message bodies are signed JSON objects.
* The client periodically contacts the server to obtain updated certificates or Online Certificate Protocal responses (OCSP) responses.


<h2 style="color:#BB86FC">Key Exchange Schemes</h2>

<h3 style="color:#03DAC5">Cryptographic Protocol Notation</h3>

<table>
<tr>
  <th>Notation</th>
  <th>Meaning</th>
</tr>
<tr>
  <td>A,B,...</td>
  <td>principals</td>
</tr>
<tr>
  <td>$K_{AB}$, ...</td>
  <td>symmetric key shared between A and B</td>
</tr>
<tr>
  <td>$K_{A}$, ...</td>
  <td>public key of A</td>
</tr>
<tr>
  <td>$K_{A}^{-1}$, ...</td>
  <td>private key of A</td>
</tr>
<tr>
  <td>$H$</td>
  <td>cryptographic hash function</td>
</tr>
<tr>
  <td>$N_A$, $N_B$, ...</td>
  <td>nonces (fresh random messages) chosen by A, B, ..</td>
</tr>
<tr>
  <td>$P, Q, R$</td>
  <td>variables ranging over principals</td>
</tr>
<tr>
  <td>$X, Y$</td>
  <td>variables ranging over statements</td>
</tr>
<tr>
  <td>$K$</td>
  <td>variables over a key</td>
</tr>
<tr>
  <td>$\{m\}_K$</td>
  <td>message $m$ encrypted with key $K$</td>
</tr>
</table>


<h3 style="color:#03DAC5">Key Exchange and Ephemeral Keys</h3>

<h4 style="color:#FF0266">Definition - key exchange</h4>

A method by which cryptographic keys are established between two parties is called a key exchange or key establishement method.

<h4 style="color:#FF0266">Definition - ephermal key</h4>

A cryptographic key that is established for the use in a single session and discarded afterwards is called an ephemeral key.

<h4 style="color:#FF0266">Definition - forward secrecy</h4>

A key exchange protocol has _forward secrecy_ (also called perfect forward secrecy) if the ephemeral key will not be compromised even any long-term keys used during the key exchange are compromised.


Key exchange methods are widely used to establish ephemeral sessions keys even if two principals have already access to suitable long-term keys. The reason is that keys can loose their strength the more frequently they are used. Hence, to secure communication over the Internet, it is desirable to establish session keys instead of using long-term keys held by a server directly. If the key exchange mechanism provides (perfect) forward secrecy, then the session keys remain strong even if the server keys get compromised at some point in time in the future.



<h4 style="color:#FF0266">Diffie-Hellman Key Exchange</h4>

* Initialization:
  * Define a prime number $p$ and a primitive root $g$ of $\Z_p$ with $g < p$. The numbers $p$ and $g$ can be made public.
* Exchange:
  * A randomly picks $x_A \in \Z_p$ and computes $y_A = g^{x_A} mod p$. $x_A$ is kept secret while $y_A$ is sent to $B$.
  * B randomly pick $x_B \in \Z_p$ and computes $y_B = g^{x_B} mod p$. $x_B$ is kept secret while $y_B$ is sent to $A$.
* $A$ computes:
  $K_{AB} = y_{B}^{X_A} \mod p = (g^{X_B} \mod p)^{X_A} \mod p = g^{X_AX_B} \mod p$.
* $B$ computes:
  $K_{AB} = y_{A}^{X_B} \mod p = (g^{X_A} \mod p)^{X_B} \mod p = g^{X_AX_B} \mod p$.

* $A$ and $B$ now own a shared key $K_{AB}$

* A number $g$ is a primitive root of $\Z_p = \{0,..., p - 1\}$ if the sequence $g^1 \mod p, g^2 \mod p, ... g^{p-1} \mod p$ produces the numbers 0, ..., p-2 in any permutation.
* $p$ should be chosen such that $(p-1)/2$ is a prime as well.
* $p$ should have a length of at least 2048 bits.

<h4 style="color:#FF0266">Needham-Schroeder Protocol</h4>

![Icon](@attachment/needham_protocol.png)

The Needham-Shcroeder protocol assumes that the two principals $A$ and $B$ both share a key with the server $S$.
  * Principals $A$ and $B$ both share a secret ($K_{AS}, K_{BS}$) key with an authentication server $S$.
  * $A$ and $B$ need a shared key to secure communication between them.
  * Idea: The authentication server creates a key $K_{AB}$ and distributes it to the principals $A$ and $B$, protected by the keys shared with $S$.
  * Principal $B$ must believe in the freshness of $K_{AB}$ in the third message. This allows an attacker to break $K_{AB}$ without any time constraint.
  * The problem can be solved by introducing time stamps. However, timestamps require securly synchronized clocks.
  * The double encryption in the second message is redundant.

<h4 style="color:#FF0266">Kerberos Protocol</h4>

The Kerberos authentication service was developed at MIT. Version 5 of Kerberos is defined in RFC 4120 deprecate weak cryptographic algorithms in Kerberos.
* This is an improved version of the Needham-Schroeder protocol.
* Uses time stamps to address the flaw in the original Needham-Schroeder protocol.
* Uses only four messages instead of five.

<h4 style="color:#FF0266">BAN Logic</h4>

* The idea is to use a formal logic to reason about authentication protocols.
* The Burrows-Abadi-Needham (BAN) logic was a first attempt to provide a formalism for authentication protocol analysis.
* The spi calculus, an extension of the pi calculus, was introduced later to analyze cryptographic protocols.

<h4 style="color:#FF0266">BAN Logic - Usage</h4>

* Steps to use BAN logic:
  1. Idealize the protocol in the language of the formal BAN logic.
  2. Define your initial security assumptions in the language of BAN logic.
  3. Use the productions and rules of the logic to deduce new predicates.
  4. Interpret the statements you've proved in this process. Have you reach your goals? 
  5. Remove unnecessary elements of the protocol, and repeat.
* BAN logic does not prove correctness of the protocol; but it helps to find subtle errors.





DRAFT:



HELLO WORL-D AND THIS IS A SECRET MESSAGE
LD AND THIHELLO WORLS IS A SECRET MESSAGE
