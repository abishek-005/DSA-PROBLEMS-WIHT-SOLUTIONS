from collections import Counter

def ret(s, words):
    word_len = len(words[0])
    num_words = len(words)
    window_len = word_len * num_words  
    word_count = Counter(words)
    result = []
    for i in range(len(s) - window_len + 1):
        sub_str = s[i:i + window_len]
        sub_words = [sub_str[j:j + word_len] for j in range(0, window_len, word_len)]
        if Counter(sub_words) == word_count:
            result.append(i)
            
    return result
print(ret("barfoofoobarthefoobarman",["bar","foo","the"]))
