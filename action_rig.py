import sys
sys.path.append("./python/")
import nicehash
from datetime import datetime

dt = datetime.now()

host = 'https://api2.nicehash.com'
organisation_id = '43ada640-92df-43ae-b6d5-c8eff0ab7b99'
key = '80044392-7979-486f-b68a-b204c27607ba'
secret = 'a6ea1812-b4cb-4bf2-8bb7-db9d6cd12c12b7375a28-8853-475e-b63f-9fa5eb692a23' 

private_api = nicehash.private_api(host, organisation_id, key, secret)

my_accounts = private_api.set_mining_rigs_status2("0-XWr4VVtAK1+qzt1yjO9wCg", sys.argv[1])

print(dt)
print(my_accounts)