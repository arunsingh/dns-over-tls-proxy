# DNS -> DNS over TLS proxy

This is a python proxy server that will accept, encrypt and relay DNS queries to cloudflare's DNS server over TLS.

## Installation

```bash
./build.sh
```

## Using and testing

Point your client to `172.17.0.2` on port 853. For example

```bash
kdig -d @172.17.0.2 -p 853 example.com
```

## Notes

### Security concerns

* The connection between the client and this proxy is definitely not encrypted, and succeptible to man-in-the-middle snooping on the local network.

### Microservices concerns

