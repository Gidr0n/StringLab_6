import re
import pandas as pd
from bs4 import BeautifulSoup
import lxml

for el in ab.find_all('recipe'):
    steps=el.steps.text
    steps=steps.split('\n')
    res.append({el.find('id').next:steps[1:3]})
#1
obj = {
    "home_page": "https://github.com/pypa/sampleproject",
    "keywords": "sample setuptools development",
    "license": "MIT",
}

max_key_length = max(len(key) for key in obj.keys())

for key, value in obj.items():
    print("{:{}} = {}".format(key, max_key_length, repr(value)))
#2
obj = str(pd.Series(["Евгения гр.ПМ19-1", "Илья пм 20-4", "Анна 20-3"]).values)
r=re.compile('\d{1}\'')
res=re.findall(r,obj)
print([el[:-1] for el in res])
#3
str='Написать регулярное выражение,которое позволит найти номера групп студентов.'
str=str.split()
print(str)
#Лабораторная работа
#1
recipes = pd.read_csv("recipes_sample.csv")
random_recipes = recipes.sample(5)
print(random_recipes[["id", "minutes"]].to_string(index=False, justify="center"))
#2
def show_info(ids):
    recipe_info=pd.read_csv('recipes_sample.csv')
    with open('steps_sample.xml') as f:
        ab=BeautifulSoup(f,'xml')
    for el in ab.find_all('recipe'):
        if str(ids) in str(el):
            x=el.id.parent
            print(x)
            break

    inf = recipe_info[recipe_info['id'] == ids].iloc[0]
    recipe_name = recipe_info['name'].title()
    # recipe_steps = recipe_info['steps'].replace('\n', '\n' + ' ' * 2)
    author = recipe_info['contributor_id']
    avg_time = recipe_info['minutes']
    output = f"{recipe_name}\n\n{recipe_steps}\n{'-' * 10}\nАвтор: {author}\nСреднее время приготовления: {avg_time} минут"}
    return output
show_info(44123)
#3
with open('steps_sample.xml') as f:
    ab=BeautifulSoup(f,'xml')
for el in ab.find_all('recipe'):
    if '25082' in str(el):
        x=el.id.parent
r=re.compile(r'\d+\shour|hours|minutes|minute')
print(x)
for _ in x:
    _=str(_)
    print(re.search(r,_))
#4
p=pd.read_csv('preprocessed_descriptions.csv')
exp=re.compile(r'^this[\w\s\d]*\.\.\.,\s?but\b')
exp=re.compile(r'this\w+|\s+|\d+]')
matching_recipes = p[p['preprocessed_descriptions'].str.contains(exp,na=False)]
num_matching_recipes = len(matching_recipes)
print("Количество рецептов: ", num_matching_recipes)
#3
recipe_idx=72367
steps = p.loc[p['id'] == recipe_idx, 'steps'].values[0]
pattern = r'(\d+)\s*/\s*(\d+)'
replace_with = r'\1/\2'
steps = re.sub(pattern, replace_with, steps)
print(steps)
#5
pattern = r'(\d+)\s*/\s*(\d+)'
with open('steps_sample.xml') as f:
    ab=BeautifulSoup(f,'xml')
for el in ab.find_all('recipe'):
    if '72367' in str(el):
        x=el.id.parent
        print(x)
        break
for _ in x:
    recipe_steps = re.sub(r'\s*/\s*', '/', str(_))
    print(recipe_steps)
#6
import nltk
from nltk.corpus import stopwords
nltk.download('stopwords')
nltk.download('punkt')
stop_words = set(stopwords.words('english'))
def tokenize_recipe_steps(recipe_steps):
    tokens = nltk.word_tokenize(recipe_steps.lower())
    filtered_tokens = [token for token in tokens if token.isalpha() and token not in stop_words]
    return filtered_tokens
from collections import Counter
total_words = []
for recipe_steps in df['steps']:
    tokens = tokenize_recipe_steps(recipe_steps)
    total_words.extend(tokens)
unique_words_count = len(Counter(total_words))
print("Количество уникальных слов:", unique_words_count)
#7
def split_to_sentences(text):
    sentences = nltk.sent_tokenize(text)
    return sentences
p['sentences'] = p['description'].apply(split_to_sentences)
p['num_sentences'] = p['sentences'].apply(len)
top_5_longest_recipes = p.nlargest(5, 'num_sentences')
for idx, row in top_5_longest_recipes.iterrows():
    print("Recipe ID:", row['id'])
    print("Recipe Title:", row['title'])
    print("Recipe Description:\n", row['description'])
    print("Number of Sentences:", row['num_sentences'])
    print("\n" + "-"*80 + "\n")
#8
nltk.download('nltk.pos_tag')
def pos_tagging(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)

    pos_list = []
    for word, pos in pos_tags:
        pos_list.append(pos)

    pos_str = " ".join(pos_list)
    words_str = " ".join(tokens)

    output = ""
    for word, pos in zip(tokens, pos_list):
        space1 = " " * (len(pos) - 2)
        space2 = " " * (len(word) - 1)
        output += f"{space1}{word}{space2}"
    return f"{pos_str}\n{output}"
recipe_title = p[p['id'] == 241106]['name'].values[0]
pos_info = pos_tagging(recipe_title)
print(pos_info)

def pos_info(sentence):
    tokens = nltk.word_tokenize(sentence)
    pos_tags = nltk.pos_tag(tokens)
    for tag in pos_tags:
        print(tag[1].ljust(6), end='')
    print()
    for word in tokens:
        print(word.ljust(6), end='')

pos_info(recipe_title)
