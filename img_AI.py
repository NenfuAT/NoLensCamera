from diffusers import StableDiffusionImg2ImgPipeline
from PIL import Image
import datetime

## 画像作成
def createImage(age:int,season:int):
    """img2imgする関数
        Args:
            age (int): 0過去 1現在 2未来
            season (int): 0:春 1:夏 2:秋 3:冬
        """
    ## カスタマイズ部分
    device =  "mps" #デバイス名(macの場合はmpsを使う)
    model_name = "CompVis/stable-diffusion-v1-4" #モデル名
    file_path ="images/defo_img.png" #元画像のファイルパス
    prompt = "photo" #呪文部分
    negative_prompt = "Low quality,(Human:3),text"#呪文その２
    dt_now = datetime.datetime.now()
    pipe = StableDiffusionImg2ImgPipeline.from_pretrained(
        model_name,
        use_auth_token="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"
    ).to(device)
    image =  Image.open(file_path).convert("RGB")

    if age==0:
        prompt="A Old style background,"+prompt
        strength=0.7
    elif age==2:
        prompt="A Futuristic background,"+prompt
        strength=0.7
    elif age==1:
        strength=0.5
        
    if season==0:
        prompt=prompt+",Spring"
    elif season==1:
        prompt=prompt+",Summer"
    elif season==2:
        prompt=prompt+",Autumn"
    elif season==3:
        prompt=prompt+",Winter"

    prompt="masterpiece,best quality,"+prompt
        
    images = pipe(prompt=prompt, negative_prompt=negative_prompt, image=image, strength=strength, guidance_scale=7.5).images
    images[0].save("AI_img/"+str(dt_now)+".png")



    

