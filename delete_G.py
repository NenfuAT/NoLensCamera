import cv2
def delete_G(link):
    """Googleのロゴを消し去ってしまえー
    Args:
        link: ストリートビューからとってきた画像のリンク
    """
    img=cv2.imread(link)
    height, width = img.shape[:2]
    print("width: " + str(width))
    print("height: " + str(height))
    img1 = img[0 : height-20, 0 : width]
    cv2.imwrite("images/defo_img.png", img1)