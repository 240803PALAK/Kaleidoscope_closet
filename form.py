import pandas as pd
import random
df = pd.read_excel('coloranalysis.xlsx')
name = "divya"
age = "15 - 21"
gender = "Female"
style = "ethenic"
hairColor = "blonde"
skinColor = "white"
size = "S"
print(name, age, gender, style, hairColor, skinColor, size)


filtered_df = df[(df['Gender'] == gender) &
                 (df['Age'] == age) &
                 (df['Skin color'] == skinColor) &
                 (df['Size'] == size) &
                 (df['Style'] == style) &
                 (df['Haircolor'] == hairColor) ]

filtered_data = filtered_df[['reference', 'links', 'price', 'image']]
image_paths_list = filtered_data['image'].tolist()
random.shuffle(image_paths_list)
# for image_path in image_paths_list:
#     image_path = int(image_path)
#     img = Image.open(f"{image_path}.jpg")
#     width, height = 250, 300
#     img_resized = img.resize((width, height))
#     display(img_resized)
print(filtered_data)