
class InputData:
    """
    入力値用のクラス
    """


    size="600x300"
    api_key="ここにAPIキー"
    location="35.694031,139.753772"
    pitch=0
    heading=0
    fov=90
    
    def __init__(self):
        self.api_key=self.api_key
        self.location=self.location
        self.pitch=self.pitch
        self.heading=self.heading
        self.fov=self.fov

    def set_size(self,size_x:int,size_y:int):
        """画像サイズを設定する関数
        Args:
            size_x (int): max640
            size_x (int): max640(ロゴ消す場合後から-20されます)
        """
        self.size=str(size_x)+"x"+str(size_y)

    def set_location(self,lat:int,lon:int):
        """座標を設定する関数
        Args:
            lat (int): 緯度
            lon (int): 経度
        """
        self.location=str(lat)+","+str(lon)

    def set_pitch(self,pitch):
        """上下の向きを設定する関数
        Args:
            pitch: -90(真下)~90(真上)
        """
        self.pitch=pitch
    
    def set_heading(self,heading):
        """水平方向の向きを設定する関数
        Args:
            heading: 方位 0~360 (0:北, 90:東, 180:南, 270:西)
        """
        self.heading=heading

    def set_fov(self,fov):
        """倍率を設定する関数
        Args:
            fov: ズーム 0~120
        """
        self.fov=fov
    
