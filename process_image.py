import os
import base64
from PIL import Image

input_path = r"C:\Users\User\Downloads\ChatGPT Image Jul 24, 2026, 05_54_28 AM.png"
output_nobg = "avatar_nobg.png"
output_face = "avatar_face.png"

# 1. Remove background
img = Image.open(input_path).convert("RGBA")
datas = img.getdata()
newData = []
# Remove white background
for item in datas:
    if item[0] > 230 and item[1] > 230 and item[2] > 230:
        newData.append((255, 255, 255, 0))
    else:
        newData.append(item)
img.putdata(newData)
img.save(output_nobg, "PNG")

# 2. Crop face
# The user's image is a portrait of a girl sitting in a chair, face is in the upper middle
width, height = img.size
# Crop a square around the face (heuristically)
left = int(width * 0.35)
top = int(height * 0.05)
right = int(width * 0.65)
bottom = int(top + (right - left))

face_img = img.crop((left, top, right, bottom))
face_img.save(output_face, "PNG")

# 3. Convert to Base64
with open(output_nobg, "rb") as f:
    nobg_b64 = base64.b64encode(f.read()).decode("utf-8")
with open("nobg_b64.txt", "w") as f:
    f.write(nobg_b64)

with open(output_face, "rb") as f:
    face_b64 = base64.b64encode(f.read()).decode("utf-8")
with open("face_b64.txt", "w") as f:
    f.write(face_b64)

print(f"Processed image dimensions: {width}x{height}")
print("Saved avatar_nobg.png and avatar_face.png")
print("Saved base64 strings to nobg_b64.txt and face_b64.txt")
