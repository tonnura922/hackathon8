# hackathon8
環境構築
dockerの立ち上げ
```
docker-compose build
docker-compose up
```


環境立ち上げ
```
docker exec -it backend bash
# migration
python manage.py makemigrations
python manage.py migrate

python manage.py runserver 0.0.0.0:8000
# http://localhost:8000/ でブラウザに表示される
```

frontコンテナ
```
docker-compose run front bash
npx create-react-app chickteckapp
cd /front/chickteckapp
npm start
```