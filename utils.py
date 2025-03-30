from typing import List, Dict


def load_data(filepath='YOUR/CSV/FILE/PATH'):
	"""
		TO DO: 
	"""
	return data, targets


def tokenization(sents):
	"""
		TO DO: 
	"""
	return tokens


def lemmatization(tokens):
	"""
		TO DO: 
	"""
	return lemmas


def pos_tagging(words: List[str]) -> Dict[str, str]:
    """
        Use this method when lemmatizing

        Input: list of words
        Output: {word: tag}
    """
    from nltk import pos_tag
    #nltk.download('omw-1.4')
    #nltk.download('averaged_perceptron_tagger')
    
    words_only_alpha = [w for w in words if w.isalpha()]

    def format_conversion(v, pos_tags=['n', 'v', 'a', 'r', 's']):
        w, p = v
        p_lower = p[0].lower()
        p_new = 'n' if p_lower not in pos_tags else p_lower
        return w, p_new

    res_pos = pos_tag(words_only_alpha)
    word2pos = {w:p for w, p in list(map(format_conversion, res_pos))}

    for w in words:
        if w not in word2pos:
            word2pos[w] = 'n'

    return word2pos


def char_embedding(lemmas):
	"""
		TO DO: 
	"""
	return v

