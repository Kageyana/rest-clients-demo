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
print(dt)
# アカウント情報
private_api = nicehash.private_api(secMyac["host"], secMyac["organisation_id"], secMyac["apikey"], secMyac["apisecret"])

rigid = "0-9k0l6RHDUkaD--ifeoEvsA"
# Quick MinerではHIGHがMEDIUM、MEDIUMがLITE、LOWが最適化OFF

if sys.argv[1] == "POWER_MODE":
    rigs_status2 = private_api.set_mining_rigs_status2(rigid, sys.argv[1], sys.argv[2])
    print(sys.argv[2])
else:
    rigs_status2 = private_api.set_mining_rigs_status2(rigid, sys.argv[1], "")

print(rigs_status2)