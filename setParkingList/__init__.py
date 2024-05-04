import logging
import azure.functions as func

from shared_code.DB import CosmosDB

def main(req: func.HttpRequest) -> func.HttpResponse:
    """
    現在の駐車場の情報を取得する。
    : return 駐車場の空き情報を更新したことを表すフラグ 1: 正常終了 0: 異常終了
    """

    # 駐車場の名前の取得
    parking_list = req.params.get('parking_list')

    # 名前が何も入力されてなかったらレスポンスして終了
    if parking_list == None:
        logging.error("parking_name is None")
        return func.HttpResponse(f"parking_name is not exist", status_code=500)
    
    # データベースに接続する
    database = CosmosDB()

    # 駐車場の情報を更新する
    flag = database.setParkingInfo(parking_list)

    return func.HttpResponse(flag , status_code=200)
