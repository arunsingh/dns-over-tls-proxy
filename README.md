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

### Microservices architecture usage

* This is a pretty good use-case for being a microservice. It does only one (arguably two, if you consider encryption) specific thing, and can easily be horizontally scaled out into multiple instances and load balanced, or vertically scaled if we want each proxy to have more processing power for higher throughput. It would be hosted on a small ec2 instance with only port
853 open, and only allowing connections from the local subnet or VPC for other services which require dns resolution.

### Improvements
* We could cache the requests for frequently requested hostnames.
