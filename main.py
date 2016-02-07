import pickle

stopwords = ['all', 'just', 'being', 'over', 'both', 'through', 'yourselves', 'its', 'before', 'herself', 'had', 'should', 'to', 'only', 'under', 'ours',
'has', 'do', 'them', 'his', 'they', 'during', 'now', 'him', 'nor', 'did', 'this', 'she', 'each', 'further', 'where', 'few', 'because', 'doing',
'some', 'are', 'our', 'ourselves', 'out', 'what', 'for', 'while', 'does', 'above', 'between', 't', 'be', 'we', 'who', 'were', 'here', 'hers', 'by', 'on',
'about', 'of', 'against', 's', 'or', 'own', 'into', 'yourself', 'down', 'your', 'from', 'her', 'their', 'there', 'been', 'whom', 'too', 'themselves', 'was',
'until', 'more', 'himself', 'that', 'but', 'don', 'with', 'than', 'those', 'he', 'me', 'myself', 'these', 'up', 'will', 'below', 'can', 'theirs', 'my', 'and',
'then', 'is', 'am', 'it', 'an', 'as', 'itself', 'at', 'have', 'in', 'any', 'if', 'again', 'no', 'when', 'same', 'how', 'other', 'which', 'you', 'after', 'most',
'such', 'why', 'a', 'off', 'i', 'yours', 'so', 'the', 'having', 'once', 'feel']

def get_emotion(word_list):
    clean_word_list = []
    for word in word_list:
        if word.lower() in stopwords:
            pass
        else:
            clean_word_list.append(word)
    emo_score = 0.0
    first_iter = True
    mult = 1.0
    for word in clean_word_list:
        if first_iter is True:
            word_score = score(word)
            if str(word_score).startswith('x'):
                mult = mult * float(word_score.lstrip('x'))
            else:
                emo_score = emo_score + float(word_score)
                first_iter = False
        word_score = score(word)
        if str(word_score).startswith('x'):
            mult = mult * float(word_score.lstrip('x'))
        else:
            emo_score = (emo_score + float(word_score))/2
    total_score = emo_score * mult
#    if total_score > 1:
#        total_score = 1
#    elif total_score < -1:
#        total_score = -1
    print "Score: " + str(total_score)
def score(word):
    with open('words.db', 'rb') as db_file:
        db = pickle.load(db_file)
    if word in db:
        return db[word]
    else:
        score =  raw_input("Unknown word '" + word + "': Enter emotion score: ")
        add_score(word, score)
        return score

def add_score(word, score):
    with open('words.db', 'rb') as db_file:
        db = pickle.load(db_file)
    if str(score).startswith('x'):
        db[word] = str(score)
    else:
        db[word] = float(score)
    with open('words.db', 'wb') as db_file:
        pickle.dump(db, db_file)

def fix_score():
    with open('words.db', 'rb') as db_file:
        db = pickle.load(db_file)
    for key in db.keys():
        print key + ' : ' + db[key]
        score = raw_input()
        if str(score).startswith('x'):
            db[key] = str(score)
        else:
            db[key] = float(score)
    with open('words.db', 'wb') as db_file:
        pickle.dump(db, db_file)

sentence = raw_input('Enter sentence: ')
get_emotion(sentence.split())
fix_score()
