# https://www.sslshopper.com/article-most-common-openssl-commands.html
openssl req -out CSR.csr -new -newkey rsa:2048 -nodes -keyout example.key
openssl req -x509 -sha256 -nodes -days 365 -newkey rsa:2048 -keyout example.key -out example.crt
