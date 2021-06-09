from gtts import gTTS

import os
my_text = "Welcome to Our Inventory,Kindly Purchase your needs available"


language = "en"
output = gTTS(text=my_text, lang=language, slow=False)

output.save("purchase.mp3")

os.system("start purchase.mp3")
