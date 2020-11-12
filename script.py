
# simple script to generate html like the following: 
import os

for root, dirs, files in os.walk("./img"):
    for i, filename in enumerate(files):
        if i == 14 or i == 28:
            print("------------------------------------------------------------------------")
        
        print(f"""<div class="photo">
    <img src="img/{filename}">
</div>
""")


