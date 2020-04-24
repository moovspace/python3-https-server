# Python3 https server
Python3 https server example.

```bash
# Generate server.pem with the following command:
mkdir .ssh
openssl req -new -x509 -keyout .ssh/key.pem -out .ssh/cert.pem -days 365 -nodes

# run as follows:
python3 simple-https-server.py

# then in your browser, visit:
#    https://localhost:4443
```
