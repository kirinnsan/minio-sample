MinIOは、Amazon S3と互換があるオブジェクトストレージ。  
ローカル上にDocker ComposeでMinIOを作成する。

### コンテナ起動
```
docker-compose up -d
```

### ログイン
```
1. localhost:9000にアクセス
2. docker-compose.ymlで定義されている  
   MINIO_ROOT_USER  
   MINIO_ROOT_PASSWORD  
   を使用してログインする。
```

### バケット、ファイル作成
```
1. sample.pyを実行すると、バケット、テストファイルが作成される。
```
