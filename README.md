# Parking Checker Backend

フロントエンドからのリクエストを受け取って、それぞれ処理を行う
なお、機能それぞれAzure Functions を使用している
- getParkingList : 現在の駐車場の情報を取得する
- setParkingList : 駐車場の情報を更新する

## 進捗 ( 5/4 時点 )
- 基本的な処理の内容の記述完了(未検証)
- CosmosDBの代わりに一時的に`parkingArea` ファイルにて駐車場の情報の管理を行う(CosmosDBが準備でき次第移行)
- 
