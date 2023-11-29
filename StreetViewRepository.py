import google_streetview.api
#from bs4 import BeautifulSoup

# デバック用パッケージ
from icecream import ic


class StreetViewRepository:
    def __init__(self, api_key):
        self.api_key = api_key

    def _create_param(self,size: str,location: str, pitch: int, heading: int, fov: int = 90):
        params = [
            {
                "size": str(size),  # max 640x640 pixels
                "location": str(location), #座標
                "pitch": str(pitch),  # 上下の角度 -90~90 (-90: 真下, 90: 真上)
                "heading": str(heading),  # 方位 0~360 (0:北, 90:東, 180:南, 270:西)
                "fov": str(fov),  # ズーム 0~120
                "key": self.api_key,
            }
        ]
        return params

    def get_pano(self,size: str, location: str, pitch: int, heading: int, fov: int = 90):
        params = self._create_param(size,location, pitch, heading,fov)
        results = google_streetview.api.results(params)
        ic(results.preview())
        results.download_links("downloads")
    