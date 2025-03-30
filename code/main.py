import utils

#####################
# YOU MUST WRITE YOUR STUDENT ID IN THE VARIABLE STUDENT_ID
# EXAMPLE: STUDENT_ID = "12345678"
#####################
STUDENT_ID = "12345678"

# 0. load data
tr_sents, tr_labels = utils.load_data(filepath='seq_class.train.csv')
ts_sents, ts_labels = utils.load_data(filepath='seq_class.test.csv')

# 1. tokenization
tr_tokens = utils.tokenization(tr_sents)
ts_tokens = utils.tokenization(ts_sents)

# 2. lemmatization
tr_lemmas = utils.lemmatization(tr_tokens)
ts_lemmas = utils.lemmatization(ts_tokens)

# 3. character embedding
tr_char_embed = utils.char_embedding(tr_lemmas)
ts_char_embed = utils.char_embedding(ts_lemmas)

# 4. sequence classification

def save_data(df):
    # EXAMPLE
    # Save the data to a csv file
    # You can change function
    # BUT you should keep the file name as "{STUDENT_ID}_seq_class.answer.csv"
    df.to_csv(f'{STUDENT_ID}_seq_class.answer.csv')

def main():
    # WRITE YOUR CODE HERE
    save_data(df)

if __name__ == "__main__":
    main()