import urllib.parse
import base64
from urllib.parse import unquote
from urllib.parse import quote


Decision = int(input('For decoding choose 1, for encoding choose 2: '))
if Decision == 1 :
    saml_dec = base64.b64decode(unquote(input('SAMLRespone: ')))
    print ('\n\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n\n')
    print (saml_dec.decode())
else:
    saml_enc = urllib.parse.quote(base64.b64encode(input('SAMLStringResponse: ').encode()))
    print ('\n\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n\n')
    print (saml_enc)


