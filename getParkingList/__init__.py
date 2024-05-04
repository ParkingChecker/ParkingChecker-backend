import logging
import azure.functions as func

from shared_code.DB import CosmosDB

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    現在の駐車場の情報を取得する。
    : return 駐車場の空き情報を表す行列
    """

    # 駐車場の名前の取得
    parking_name = req.params.get('parkingName')

    # 名前が何も入力されてなかったらレスポンスして終了
    if parking_name == None:
        logging.error("parking_name is None")
        return func.HttpResponse(f"parking_name is not exist", status_code=500)
    
    # データベースに接続する
    database = CosmosDB()

    # 駐車場の情報をデータベースから読み込む
    parking_list = database.getParkingInfo(parking_name)

    return func.HttpResponse(parking_list, status_code=200)
