import zlib
import base64
import urllib.parse
from urllib.parse import unquote
from urllib.parse import quote

def decodeURL_decode64_inflate(SAMLRequest):
    decoded_data = base64.b64decode(unquote(SAMLRequest))
    return zlib.decompress( decoded_data , -15)

def deflate_and_base64_encode(StringSAMLRequest):
    zlibbed_str = zlib.compress(StringSAMLRequest)
    compressed_string = zlibbed_str[2:-4]
    return urllib.parse.quote_plus(base64.b64encode(compressed_string))


Decision = input('For encoding choose 1, for decoding choose 2: : ')

if Decision == '2':
    final = decodeURL_decode64_inflate(input('SAMLRequest: ')).decode()
elif Decision == '1':
    final = deflate_and_base64_encode(input('StringSAMLRequest: ').encode('UTF-8'))   

print ('\n\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n\n')
print (final)
