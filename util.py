def get_senteces(path):
    f=open(path, "r")    
    content = f.read()
    content = content.split('\n\n')
    return content

def split_tokens_labeled(sentences):
    result = []
    for sent in sentences: 
        sent = sent.split('\n')
        sent = [w.split(' ') for w in sent]
        if len(sent) > 1:
            sent = [(w[0],w[1],w[2]) for w in sent]
            result.append(sent)
    return result

def split_tokens_unlabeled(sentences):
    result = []
    for sent in sentences: 
        sent = sent.split('\n')
        sent = [w.split(' ') for w in sent]
        if len(sent) >= 1:
            if len(sent[0]) >1:
                sent = [(w[0],w[1]) for w in sent]
                result.append(sent)
    return result

def get_words(sentences):
    words = []
    for s in sentences:
        for w in s:
            words.append(w[0])
    words = list(set(words))
    words.append("ENDPAD")
    return words

def get_labels(sentences):
    tags = []
    for s in sentences:
        for w in s:
            tags.append(w[2])
    tags = list(set(tags))
    return tags

def get_token_class(sentences):
    tags = []
    for s in sentences:
        for w in s:
            tags.append(w[1])
    tags = list(set(tags))
    return tags
