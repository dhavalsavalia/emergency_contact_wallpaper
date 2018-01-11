from PIL import Image, ImageDraw, ImageFont
import random

image1 = Image.open("wallpaper_background.png")

font_type = ImageFont.truetype("Arial.ttf", 30)
draw = ImageDraw.Draw(image1)

name = input("What is your good name?\n")
text_name = "Name: {}".format(name)

age = input("How old are you, {}?\n".format(name))
text_age = "Age: {}".format(age)

blood_group = input("Please tell me your blood group!\n")
text_blood_group = "Blood Group: {}".format(blood_group)

print("Now I'll be asking for two of your friend or family.\n")

emergency_contact_1_name = input("Please give me a name of your friends or family.\n")
emergency_contact_1_rel = input("Describe your relation with {}\n".format(emergency_contact_1_name))
print("You have to give two phone number of that person\n")
emergency_contact_1_contact_1 = input("So what's their first phone number?\n")
emergency_contact_1_contact_2 = input("So what's their second phone number?\n")

emergency_contact_1_name_render = "Name: {} ({})".format(emergency_contact_1_name, emergency_contact_1_rel)
emergency_contact_1_contact_render = "Contact: {} / {}".format(emergency_contact_1_contact_1, emergency_contact_1_contact_2)

print("Now I'll be asking about second person!\n")

emergency_contact_2_name = input("Please give me a name of your friends or family.\n")
emergency_contact_2_rel = input("Describe your relation with {}\n".format(emergency_contact_2_name))
print("You have to give two phone number of that person\n")
emergency_contact_2_contact_1 = input("So what's their first phone number?\n")
emergency_contact_2_contact_2 = input("So what's their second phone number?\n")

emergency_contact_2_name_render = "Name: {} ({})".format(emergency_contact_2_name, emergency_contact_2_rel)
emergency_contact_2_contact_render = "Contact: {} / {}".format(emergency_contact_2_contact_1, emergency_contact_2_contact_2)

(x, y) = (49, 600)

draw.text(xy=(x,y), text=text_name, fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 40), text=text_age, fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 80), text=text_blood_group, fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 120), text="", fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 160), text="Emergency/Family contact details:", fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 200), text="", fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 240), text=emergency_contact_1_name_render, fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 280), text=emergency_contact_1_contact_render, fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 320), text="", fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 360), text=emergency_contact_2_name_render, fill=(255, 255, 255), font=font_type)
draw.text(xy=(x,y + 400), text=emergency_contact_2_contact_render, fill=(255, 255, 255), font=font_type)

file_name = "{}.png".format(random.randint(1, 255))

image1.save(file_name)
