import logging
from shared_code.parking_data import parkingArea

class CosmosDB:
    """
    Azure CosmosDB の機能をまとめたクラス
    """
    def __init__(self):
        """
        コンストラクタ
        """

    def getParkingInfo(parking_name) -> list:
        """
        駐車場の情報を取得する
        :parking_name 取得したい駐車場の名前
        :return 行列変換したリスト
        """
        try:
            parking_list = parkingArea[parking_name]
        except KeyError as e:
            logging.error(e)

        return parking_list


    def setParkingInfo(parking_name, parking_list) -> int:
        """
        駐車場の情報を更新する
        :parking_name 駐車場の名前
        :parking_list 更新した駐車場のリスト
        :return 正常に終了したかどうかを伝えるフラグ
        """
        try:
            parkingArea[parking_name] = parking_list
        except KeyError as e:
            logging.error(e)
            return 0
        
        return 1
    
    
    