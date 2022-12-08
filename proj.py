from urllib.request import urlopen
import json
import string
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

stop_words = set(stopwords.words('english'))
words = set(nltk.corpus.words.words())
lemmatizer = WordNetLemmatizer()

url = "https://raw.githubusercontent.com/AlpKaanK/Hardware-software-codesign/main/data1.json"

# store the response of URL
response = urlopen(url)

# storing the JSON response
# from url in data
data_json = json.loads(response.read())
#print(data_json)

def listToString(s):
    str1 = ""

    for ele in s:
        str1 += ele + " "

    return str1

def check():
    for _responses in data_json:
        y = len(data_json)
        print(_responses)

        with open('lastdata.json', 'a+') as f:
            f.seek(0)
            f.truncate()
            f.write("{"+ '\n' + '"intents" : [' + "\n")

            sentence1 = (_responses.lower())  # Lower case
            sentence1 = lemmatizer.lemmatize(sentence1)  # Lemmatizer ( Time consumption is really high )
            sentence1 = " ".join(w for w in nltk.wordpunct_tokenize(sentence1) if
                                 w.lower() in words or not w.isalpha())  # Non-english words check

            tokens = nltk.word_tokenize(sentence1)  # Tokenizer
            tokens = [word for word in sentence1.split() if word not in stop_words]

            tokens = list(filter(lambda token: token not in string.punctuation, tokens))  # Punctuation
            json_object = json.dumps(tokens)
            print(json_object)
            f.write(json_object + '\n')

            f.write(",")

            """
            for i in range(z):
                    print(x[i])

                    break




            res = {}
            for z in x:
                res.update(z)
                print(type(res))

            """
            f.write("]" + "}")
            f.close()




check()
