import sys
sys.path.append("./python/")
import nicehash
from datetime import datetime
import configparser # iniファイルライブラリ

config_ini = configparser.ConfigParser(interpolation=configparser.ExtendedInterpolation())  # ConfigParserオブジェクト
config_ini_path = 'nicehash.ini'  # 設定ファイルのパス
config_ini.read(config_ini_path, encoding='utf-8')      # 設定ファイル読み込み
secMyac = dict(config_ini.items("MYACCOUNT"))        # セクションの値を読み込む

dt = datetime.now()

# アカウント情報
private_api = nicehash.private_api(secMyac["host"], secMyac["organisation_id"], secMyac["key"], secMyac["secret"])

rigid = "0-XWr4VVtAK1+qzt1yjO9wCg"

if sys.argv[1] == "POWER_MODE":
    rigs_status2 = private_api.set_mining_rigs_status2(rigid, sys.argv[1], sys.argv[2])
else:
    rigs_status2 = private_api.set_mining_rigs_status2(rigid, sys.argv[1])

print(dt)
print(rigs_status2)