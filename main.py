from InputData import InputData
import DL_Photo
import delete_G
from img_AI import createImage

def main():
    input = InputData()
    input.set_location(35.360625,138.727363)
    input.set_size(640,380)
    input.set_pitch(10)
    input.set_fov(60)
    input.set_heading(0)
    #DL_Photo.download_photo(input.size,input.api_key,input.location,input.pitch,input.heading,input.fov)
    delete_G.delete_G("downloads/gsv_0.jpg")
    print("画像を出力中です。")
    createImage(1,2)

if __name__ == "__main__":
    main()