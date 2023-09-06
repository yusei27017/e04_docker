# e04_docker
### 請先安裝docker and docker-compose。
### 啟動docker後，移動到專案目錄下。
```
docker-compose up -d
```
### 如果需要更改查詢條件可至env.py調整網址如果要改關鍵字直接在e04.py更改就行。
### 抓取完成後可連線至dev-mongo容器中查看資料。e04-crowl會自動exit。
### 看完後可關閉compose
```
docker-compose down
```
### 單獨開啟dev-mongo
```
docker run -d -p 27017:27017 -v $(PWD)/db/mongo:/data/db mongo:4.4
```