from StreetViewRepository import StreetViewRepository
def download_photo(
    size: str,api_key: str, location: str, pitch: int = 0, heading: int = 0, fov: int = 90
):
    """住所からGoogleStreetViewの画像を保存する
    Args:
        size (str): 画像サイズ max640x640pix
        api_key (str): GoogleStreetViewから取得するAPIキー
        location (str): 検索対象の座標
        pitch (int): 上下方向の角度
        heading (int): 水平方向の角度
        fov (int): ズームの割合
    """
    # 初期化
    sr = StreetViewRepository(api_key=api_key)

    # 画像のダウンロード処理
    sr.get_pano(
        size=size,
        location=location,
        pitch=pitch,
        heading=heading,
        fov=fov,
    )
