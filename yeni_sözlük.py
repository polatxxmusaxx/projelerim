meme_dict = {
            "CRINGE": "Garip ya da utandırıcı bir şey",
            "LOL": "Komik bir şeye verilen cevap",
            "NECROMANCER":"ölü çağıran",
            "SUPPORT": "desteklemek",
            }
word = input("anlamadığınız bir kelime öğrenin {büyük harflerle unutma}:  ")
if word in meme_dict.keys():
    print(meme_dict[word])
else:
    print("aradığınız kelime bulunamıyoooor!!!")
