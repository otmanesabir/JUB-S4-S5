---
tags: [SADS]
title: 6 Information Hiding & Privacy
created: '2020-05-25T18:04:19.783Z'
modified: '2020-05-28T07:10:22.982Z'
---

# 6 Information Hiding & Privacy


Cryptographic mechanism can protect information. By encrypting data, only parties with access to the appropriate keys can read or modify the data. There are, however, situations where it is in addition desirable to hide the fact that data exists. Information hiding is a research domain that covers a wide spectrum of methods that are used to make (secret) data difficult to notice.


[//]: # (Primary = #BB86FC)
[//]: # (Secondary = #03DAC5)
[//]: # (Secondary = #FF0266)

<h2 style="color:#BB86FC">Steganography and Watermarks</h2>
<h3 style="color:#03DAC5">Information Hiding</h3>

_Information hiding_ aims at concealing the very existence of some kind of information for some specific purpose.

* Information hiding itself does not aim at protecting message content.
* Encryption protects message content but by itself does not hide the existence of a message.
* Information hiding techniques are often used together with encryption in order to both hide the existence of messages and to protect messages in case their existence is uncovered.


Some applications of information hiding:
  * Improving confidentiality by hiding the very existence of messages.
  * Proving ownership of digital media by inserting hidden information into it.
  * Fingerprinting media for tracking puposes
  * Hiding communication (covert channels)
  * Identification of devices used to produce an artefact
  * Hiding malware from being easily detected.
  * Enabling forensics, for example, by embedding identification codes into software
  * Carrying data or programs through border control checks
  * Storing sensitive inforamtion in a way that can't be easily discovered.

<h3 style="color:#03DAC5">Steganography</h3>

_Stegnography_ is the embedding of some information (hidden-text) within digital media (cover-text) so that the resulting digital media (stego-text) looks unchanged (imperceptible) to a human/machine.

* Information hiding explores that fact that there are often (almost) unused or redundant bits in digital media that can be used to carry hidden digital information.
* The challenge is to identify (almost) unused or redundant bits and to encode hidden digital information in them in such a way that the existence of hidden information is difficult to observe.

A very simple approach to embed hidden information into images is to take the color values (red, green, blue) of the pixels and to modify the least significant bits to encode hidden information. This is very straight-forward to implement and for humans the changes are almost impossible to spot. On the other hand, it is relatively easy to spot that an image might contain hidden information since the statistical properties of the pixels change.

<h3 style="color:#03DAC5">Types of Cover Media</h3>

* Information can be hidden in various cover media types:
  * Image files
  * Audio files
  * Video files
  * Text files
  * Software 
  * Network traffic (e.g., covert channels)
  * Storage devices
* Media types of large size usually make it easier to hide information.
* Robust steganographic methods may survive some typical modfications of stego-texts.

Several steganographic file systems have been prototyped. The basic idea is to fill unused blocks with random data and to store hidden files in these data blocks. 

<h3 style="color:#03DAC5">Watermarking</h3>
<h4 style="color:#FF0266">Definition</h4>

_Watermarking_ is the embedding of some information (watermark) within a digital media (cover-text) so that the resulting digital media looks unchanged (imperceptible) to a human/machine.

* Watermarking:
  * The hidden information itself is not important.
  * The watermark says something about the cover-text.
* Steganography:
  * The cover-text is not important, it only conveys the hidden information.
  * The hidden text is the valuable information, and it is independent of cover-text.

Digital watermarks are widely used for copyright protection and source tracking purposes.
Some modern laster printers add tiny yellow dots to each page. The barely visible-dots contain encoded printer serial numbers and data and time stamps.

Compared to steganography algorithms, watermark algorithms usually only need to store small amounts of data. Watermarking algorithms are typically designed to produce robust watermarks (watermarks that survive transformations applied to the cover text) and to create watermarks that are difficult to detect and remove.

<h3 style="color:#03DAC5">Classification of Steganographic Algorithms</h3>

* Fragils vs. Robust
  * Fragile: Modifications of stego-text likely destroys hidden text.
  * Robust: Hidden text is likely to survive modifications of the stego-text.
* blind vs. semi-blind vs. non-blind
  * Blind requires the original cover-text for detection / extraction.
  * Semi-blind needs some information from the embedding but not the whole cover-text.
  * Non-blind does not need any information for detection/extraction.
* pure vs. symmetric (secret key) vs. asymmetric (public key)
  * Pure needs no key for detection / extraction.
  * Secret key needs a symmetric key for embedding and extraction.
  * Public key needs a secret key for embedding and a public key for extraction.

<h3 style="color:#03DAC5">Example: LSB-based Image Steganography</h3>

* Idea :
  * Some image formats encode a pixel using three 8-bit color values (red, free, blue).
  * Changes in the least-significant bits (LSB) are difficult for humans to see.

* Approach:
  * Use a key to select some least-significant bits of an image to embed hidden information.
  * Encode the information multiple times to achieve some robustness against noise.

* Problem:
  * Existence of hidden information may be revealed if the statistical properties of least-significant bits change.
  * Fragile against noise such as compression, resizing, cropping, rotating or simply additive white Gaussian nosie.

<h3 style="color:#03DAC5">Example: DCT-based Image Steganography</h3>

* Idea :
  * Some image formats (e.g, JPEG) use discrete cosine transforms (DCT) to encode image data.
  * The manipulation happens in the frequency domain instead of the spatial domain and this reducces visual attacks against the JPEG image format.

* Approach
  * Replace the least-significant bits of some of the discrete cosine transform coefficients.
  * Use a key to select some DCT coefficients of an image to embed hidden information.

* Problem:
  * Existence of hidden information may be revealed if the statistical properties of the DCT coefficients are changed.
  * This risk may be reduced by using a pseudo-random number generator to select coefficients.


<h2 style="color:#BB86FC">Covert Channels</h2>
<h3 style="color:#03DAC5">Definition</h3>

* Covert channels represent unforseen communication methods that break security policies. Network covert channels transfer information through networks in ways that hide the fact that communication takes place.

* Covert channels embed information in
  * header fields of protocol data units (protocol messages)
  * the size of protocol data units
  * the timing of protocol data units

* We are not considering here covert channels that are constructed by exchanging steganographic objects in application messages.


<h3 style="color:#03DAC5">Covert Channel Patterns</h3>

1. Size Modulation Pattern
  * The covert channels uses the siwe of a header field or of a protocol message to encode hidden information.
2. Sequence Pattern
  * The covert channel alters the sequence of header fields to encode hidden information.
3. Add Redundancy Pattern
  * The covert channel create new space within a given header field within a message to carry hidden information.
4. PDU Corruption/Loss Pattern
  * The covert channel generates corrupted protocol messages that contain hidden data or it actively utilizes packet loss to signal hidden information.
5. Random Value Pattern
  * The covert channel embeds hidden data in a header field containing a "random" value.
6. Value Modulation Pattern
  * The covert channel selects one of values a header field can contain to encode a hidden message.
7. Reserved/Unused Pattern
  * The covert channel encodes hidden data into a reserved or unused header field.
8. Inter-arrival Time Pattern
  * The covert channel alters timing intervals between protocol messages (inter-arrival times) to encode hidden data.
9. Rate Pattern
  * The covert channel sender alters the data rate of a traffic flow from itself or a third party to the covert channel receiver.
10. Protocol Message Order Pattern
  * The covert channel encodes data using a synthetic protocol message order of a given number of protocol messages flowing between covert sender and receiver.
11. Re-Transmission Pattern 
  * A covert channel re-transmits previously sent of received protocol messages.

<h2 style="color:#BB86FC">Anonymization Terminology</h2>

<h3 style="color:#03DAC5">Anonymity</h3>

_Anonymity_ of a subject from an attacker's perspective means that the attacker cannot sufficiently identify the subject within a set of subjects, the anonymity set.

* All other things being equal, annonymity is the stronger, the larger the respective anonymity set is and the more evenly distributed the sending and receiving, respectively, of the subjects within that set it.

* Robustness of anonymity characterizes how stable the quantity of anonymity is against changes in the particular setting, e.g., a stronger attacker or different probability distributions.


It is important to conisder the anonymity set when we talk about anonymity.


<h3 style="color:#03DAC5">Unlinkability and Linkability</h3>
<h4 style="color:#FF0266">Unlinkability</h4>

_Unlinkability_ of two or more items of interest (IOIs) from an attacker's perspective means that within the system, the attacker cannot sufficiently distinguish whether these IOIs are related or not.

<h4 style="color:#FF0266">Linkability</h4>

_Linkability_ of two or more items of interest (IOIs) from an attacker's perspective means that within the system, the attacker can sufficiently distinguish whether these IOIs are related or not.

Anonymity can be expressed in terms of unlinkability:
  * Sender anonymity of a subject means that this potentially sending subject, each message is unlinkable.
  * Recipient anonymity of a subject means that to this potentially receiving subject, each message is unlinkable.


<h3 style="color:#03DAC5">Undetectability and Unobservability</h3>

<h4 style="color:#FF0266">Undetectability</h4>
_Undetectability_ of an item of interest (IOI) from an attacker's perspective means that the attacker cannot sufficiently distinguish whether it exists or not.


<h4 style="color:#FF0266">Unobservability</h4>
_Unobservability_ of an item of interest (IOI) means
  * undecidability of the IOI against all subjects uninvolved in it
  * anonymity of the subject(s) involved in the IOI even against the other subject(s) involved in that IOI.


* Sender unobservability then means that it is sufficiently undetectable whether any sender within the unobservability set sends. Sender unobservability is perfect if and only if it is completely undetectable whether any sender within the unobservability set sends.

* Recipient unobservability then means that it is sufficiently undetectable whether any recipient within the unobservability set receives. Recipient unobservability is perfect if and only if it is completely undetectable whether any recipient within the unobservability set receives.

* Relationship unobservability then means that it is sufficiently undetectable whether anything is sent out of a set of could-be senders to a set of could-be recipients.

<h3 style="color:#03DAC5">Relationships</h3>

With respect to the same attacker, the following relationships hold:

* unobservability $\rightarrow$ anonymity
* sender unobservability $\rightarrow$ sender anonymity
* recipient unobservability $\rightarrow$ recipient anonymity
* relationship unobservability $\rightarrow$ relationship anonymity.
<br>
We also have:

* sender anonymity $\rightarrow$ relationship anonymity
* sender anonymity $\rightarrow$ relationship anonymity
* sender unobservability $\rightarrow$ relationship unobservability
* recipient unobservability $\rightarrow$ relationship unobservability 

<h3 style="color:#03DAC5">Pseudonymity</h3>

<h4 style="color:#FF0266">Definition - Pseudonym</h4>

A _pseudonym_ is an identifier of a subject other than one of the subject's real names. The subject, which the pseudonym refers to, is the holder of the pseudonym.

<h4 style="color:#FF0266">Definition - Pseudonymity</h4>

A subject is _pseudonymous_ if a pseudonym is used as identifier instead of one of its real names. Pseudonymity is the use of pseudonyms as identifiers.


* Sender pseudonymity is defined as the sender being pseudonymous, recipient pseudonimity is defined as the recipient being pseudonymous.

* A digital pseudonym can be realized as a public key to test digital signatures where the holder of the pseudonym can prove holdership by forming a digital signature , which is created using the corresponding private key. An example would be PGP keys.

* A public key certificate bears a digital signature of a so-called certification authority and provides some assurance of the binding of a public key to another pseudonym, usually held by the same subject. In case that pseudonym is the civil identity (the real name) of a subject, such a certificate is called an identity certificate.

* The relation between a pseudonym and the related subject can be thought of as "a subject holds a pseudonym" and in general a subject holds one more multiple pseudonyms.


<h3 style="color:#03DAC5">Identifiability & Identity</h3>
<h4 style="color:#FF0266">Identifiability</h4>


_Identifiability_ of a subject from an attacker's perspective means that the attacker can sufficiently identify the subject within a set of subjects, the identifiability set.

<h4 style="color:#FF0266">Identity</h4>

An identity is any subset of attribute values of an individual person that sufficiently identifies this individual person within any set of persons. So usually there is no such thing as "the identity", but several of them.

* Identity enables both to be identifiable as well as to link items of interest (IOIs) because of some continuity of life.

<h4 style="color:#FF0266">Identity Management</h4>

Identity management means managing various partial identities (usually denoted by pseudonyms) of an individual person, i.e, administration of identity attributes including the development and choice of the partial idenitity and pseudonym to be (re-)used in a specific context or role.

* A partial identity is a subset of attribute values of a complete identity, where a complete identity is the union of all attribute values of all identities of this person.


<h2 style="color:#BB86FC">Mixes and Onion Routing</h2>
<h3 style="color:#03DAC5">Mix Networks</h3>

* A mix network uses special proxies called mixes to send data from a source to a destination.

* The mixes filter, collect, record, and reorder messages in order to hide conversations. Basic operations of a mix:
  1. Removal of duplicate messages (an attacker may inject duplicate message to infer something about a mix).
  2. Collection of messages in order to create an ideally large anonymity set.
  3. Recoding of messages so that incoming and outgoing messages cannot be linked.
  4. Reordering of messages so that order information cannot be used to link incoming and outgoing messages.
  5. Padding of messages so that message sizes fo not reveal information to link incoming and outgoing messages. 


<h3 style="color:#03DAC5">Onion Routing</h3>

* A message $m$ it sent from the source S to the destination T via an overlay network consisting of the intermediate routers $R_1$, $R_2$, ..., $R_n$, called a circuit.
* A message is cryptographically wrapped multiple times such that every router R unwraps one layer and thereby learns to which router the message needs to be forwarded next.
* To preserve the anonymity of the sender, no node in the circuit is able to tell whther the node before it is the originator or another intermediary like itself.
* Likewise, no node in the circuit is able to tell how many other nodes are in the circuit and only the final node, the "exit node", is able to determine its own location in the chain.

