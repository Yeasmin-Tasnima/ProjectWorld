import json
from rakutenma import RakutenMA

rma = RakutenMA()

# "tatoeba.json" is available at https://github.com/rakuten-nlp/rakutenma
tatoeba = json.load(open("tatoeba.json"))
for i in tatoeba:
    rma.train_one(i)

print(rma.tokenize("値段からしてこんなもんでしょうかねぇ可もなく不可もなしですね who are you."))

# Initialize a RakutenMA instance with a pre-trained model
rma = RakutenMA(phi=1024, c=0.007812)  # Specify hyperparameter for SCW (for demonstration purpose)
rma.load("model_ja.json")

# Set the feature hash function (15bit)
rma.hash_func = rma.create_hash_func(15)

# Tokenize one sample sentence
print(rma.tokenize("値段からしてこんなもんでしょうかねぇ可もなく不可もなしですね who are you."))
