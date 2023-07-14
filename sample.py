import boto3

REGION_NAME = 'ap-northeast-1'


def create_bucket(s3_resource, bucket_name, region=None):
    """バケットの作成"""

    if region is None:
        location = {'LocationConstraint': REGION_NAME}

    try:
        response = s3_resource.create_bucket(
            Bucket=bucket_name,
            CreateBucketConfiguration=location
        )
    except Exception as e:
        print('Error', e)
        return None

    return response


def list_all_bucket(s3):
    """バケット一覧表示"""

    for bucket in s3.buckets.all():
        print('バケット情報:', bucket)
        print('バケット名:', bucket.name)


def upload_file(s3_resource, bucket_name, file_name, object_name=None):
    """
    対象のバケットにファイルをアップロードする

    ：param s3_resource：S3のリソース
    ：param bucket_name : アップロードするバケット
    ：param file_name：アップロードするファイル
    ：param object_name：S3オブジェクト名。指定しない場合、file_nameが使用されます

    ：return：ファイルがアップロードされた場合はTrue,それ以外はFalse
    """

    if object_name is None:
        object_name = file_name

    try:
        s3_resource.meta.client.upload_file(
            file_name, bucket_name, object_name)
    except Exception as e:
        print(e)
        return False

    return True


def download_file(s3_resource, bucket_name, file_name, object_name):
    """
    対象のバケットからファイルをダウンロードする

    ：param s3_resource：S3のリソース
    ：param bucket_name : ダウンロード対象のバケット
    ：param file_name：ダウンロードする時のファイル名
    ：param object_name：S3オブジェクト名。

    ：return：ファイルがダウンロードされた場合はTrue,それ以外はFalse
    """

    try:
        s3_resource.meta.client.download_file(
            bucket_name, object_name, file_name)
    except Exception as e:
        print(e)
        return False

    return True


if __name__ == '__main__':
    # S3リソース作成
    s3_resource = boto3.resource(
        's3',
        endpoint_url='http://localhost:9000',
        aws_access_key_id='root', # ログイン名
        aws_secret_access_key='password', # ログインパスワード
    )

    bucket_name = "minio-sample"

    # バケット作成
    result = create_bucket(s3_resource, bucket_name)
    if result is not None:
        print(result)

    # # バケット一覧取得
    list_all_bucket(s3_resource)

    # ファイルのアップロード
    result = upload_file(s3_resource, bucket_name=bucket_name,
                         file_name='resource/s3test.txt')
    print('ファイルアップロード結果')
    print(result)

    # ファイルのダウンロード
    result = download_file(s3_resource, bucket_name=bucket_name,
                           file_name='download.txt',
                           object_name='resource/s3test.txt'
                           )
    print('ファイルダウンロード結果')
    print(result)
