from PIL import Image, ImageOps

img  = Image.open("Images\Camera.png")

resized_img = ImageOps.fit(img, (64, 48), Image.Resampling.LANCZOS)

resized_img.save("Camera.png")
print("Resized to 640x480")