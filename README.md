# hackathon8
環境構築
dockerの立ち上げ
```
docker-compose build
docker-compose up
```


backendコンテナ内での操作(例)
```
docker exec -it backend bash
# migration(modelの変更をDBに反映)
python manage.py makemigrations
python manage.py migrate

# django立ち上げ
python manage.py runserver 0.0.0.0:8000
# http://localhost:8000/ でブラウザに表示される

# 管理ユーザーの作成
python manage.py createsuperuser
```

mysqlの操作
```
# コンテナ内へ
docker exec -it mysql bash
% mysql へログイン(パスワードは`django`)
mysql -u django -p

# mysql ログイン後の操作

mysql> SHOW DATABASES;

mysql> USE django;

mysql> SHOW tables;
```