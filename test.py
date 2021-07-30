import sys
sys.path.append("./python/")
import nicehash
from datetime import datetime
from pprint import pprint       # 辞書型の出力
import configparser # iniファイルライブラリ

config_ini = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())  # ConfigParserオブジェクト
config_ini_path = 'nicehash.ini'  # 設定ファイルのパス
config_ini.read(config_ini_path, encoding='utf-8')      # 設定ファイル読み込み
secMyac = dict(config_ini.items("MYACCOUNT"))        # セクションの値を読み込む

dt = datetime.now()

# アカウント情報
private_api = nicehash.private_api(secMyac["host"], secMyac["organisation_id"], secMyac["key"], secMyac["secret"])

rigid = "0-XWr4VVtAK1+qzt1yjO9wCg"

# res = private_api.get_mining_miningAddress()

# algorithm = 20
# afterTimestamp = 1603023402000
# beforeTimestamp = 1603109802000
# res = private_api.get_mining_rig_stats_algo(rigid,algorithm,afterTimestamp,beforeTimestamp)

# afterTimestamp = "1624024832"
# beforeTimestamp = "1627653632"
# res = private_api.get_mining_rig_stats_unpaid(rigid,afterTimestamp,beforeTimestamp)

# res = private_api.get_mining_rig2(rigid)

# size = "100"
# page = "0"
# sortParameter = "RIG_NAME"
# sortDirection = "ASC"
# res = private_api.get_mining_rigs_activeWorkers(size, page, sortParameter, sortDirection)

# beforeTimestamp = "1627653632"
# size = "25"
# page = "0"
# res = private_api.get_mining_rigs_payouts(beforeTimestamp, size, page)

# algorithm = "20"
# afterTimestamp = "1625061632"
# beforeTimestamp = "1627653632"
# res = private_api.get_mining_rigs_stats_algo(algorithm, afterTimestamp, beforeTimestamp)

# afterTimestamp = "1625061632"
# beforeTimestamp = "1627653632"
# res = private_api.get_mining_rigs_stats_unpaid(afterTimestamp, beforeTimestamp)

size = "25"
page = "0"
path = "0"
sort =  "NAME"
system = "NHM"
status = "Mining"
res = private_api.get_mining_rigs2(size, page, path, sort, system, status)

print(dt)
pprint(res)