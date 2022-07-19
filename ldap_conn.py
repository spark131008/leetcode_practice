from ldap3 import Server, Connection, SAFE_SYNC

devurl = 'ldap-proxy.dev.useast1.crn'
qaurl = 'ldap-proxy.qa.useast1.crn'
produrl = 'ldap.useast1.crn:1636'
cn = 'cn=authproxymanager'
pw = ''
# Initialize the Connection
# con = ldap3.initialize('ldaps://' + url)
conn = Connection(url, user=cn, password=pw, auto_bind=True)

# Ignore SSL Security Certificate
# ldap3.set_option(ldap3.OPT_X_TLS_REQUIRE_CERT, ldap3.OPT_X_TLS_ALLOW)



# Binding to LDAP Connection
# con.simple_bind_s(cn, pw)

# LDAP Scope
# searchScope = ldap3.SCOPE_SUBTREE

baseDN='dc=chick-fil-a,dc=com'
searchFilter='(uid=CFAID-0PE3KD0PDBKCXL0Z)'
retrieveAttributes=["uid", "givenName", "sn", "street", "street2", "city", "st", "zip", "mail", "mobile", "loyaltyRegistrationDate"]

ldap_result_id = conn.search(search_base=baseDN, search_filter=searchFilter, attributes=retrieveAttributes)

# result_type, result_data = conn.result(ldap_result_id, 0)
entry = conn.entries

entry.entry_to_json()