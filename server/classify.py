#!/usr/bin/env python

"""
    classify.py:
        The function of this script is classify a question using a Support vector machine to find a model to
        best split the training data
"""

__author__ = "Daniel Ayvar"

from sklearn.svm import LinearSVC
import pandas
import spacy
import sys

from scipy.sparse import csr_matrix


def transform_data_matrix(train_data, predict_data):
    """
    Adds the missing columns to the train_data and predict data to prepare them for the SVM. Then returns the new
    vector models
    :param train_data: vector model of all questions
    :param predict_data: vector model of the question to be classified
    :return:
    """
    #Adds all miss
    train_columns = list(train_data.columns)
    predict_columns = list(predict_data.columns)

    trans_columns = list(set(train_columns + predict_columns))

    trans_data_train = {}

    for col in trans_columns:
        if col not in train_data:
            trans_data_train[col] = [0 for i in range(len(train_data.index))]
        else:
            trans_data_train[col] = list(train_data[col])

    t_train = pandas.DataFrame(trans_data_train)
    t_train = csr_matrix(t_train)
    trans_data_predict = {}

    for col in trans_columns:
        if col not in predict_data:
            trans_data_predict[col] = 0
        else:
            trans_data_predict[col] = list(predict_data[col])

    t_predict = pandas.DataFrame(trans_data_predict)
    t_predict = csr_matrix(t_predict)

    return t_train, t_predict


def support_vector_machine(train_data, class_col, predict_data):
    """
    Trains a Linear support vector machine to attribute the vector model for the questions to the classification
    of those questions. It then predicts the class of the question to predict using it's vector model
    :param train_data: vector model for the training question data
    :param class_col: columns that includes the classes of all the questions in the training question data vector model
    :param predict_data: vector model for the question to predict
    :return:
    """
    linsvc = LinearSVC()
    linsvc.fit(train_data, class_col)
    prediction = linsvc.predict(predict_data)
    return prediction


def process_question(question, en_nlp):
    """
    Processes question and retrieves the question word (WHO,HOW,WHEN,WHERE), it's bigram, along with their
    POS tags
    :param question: raw question text to process
    :param en_nlp: english language model from spacey
    :return: returns a processed question within a dictionary
    """
    en_doc = en_nlp(u'' + question)
    sents = list(en_doc.sents)
    sent = sents[0]

    #Bigram of word
    wh_bi_gram = []

    root_token = ""
    #Question Non-terminal
    wh_pos = ""
    #Question Neighbor Non-terminal
    wh_nbor_pos = ""
    #Question word
    wh_word = ""

    for sent in sents:
        wh_bi_gram = []
        root_token, wh_pos, wh_nbor_pos, wh_word = [""] * 4

        for token in sent:
            if token.tag_ == "WDT" or token.tag_ == "WP" or token.tag_ == "WP$" or token.tag_ == "WRB":
                wh_pos = token.tag_
                wh_word = token.text
                wh_bi_gram.append(token.text)
                wh_bi_gram.append(str(en_doc[token.i + 1]))
                wh_nbor_pos = en_doc[token.i + 1].tag_

            if token.dep_ == "ROOT":
                root_token = token.tag_

        classifier = {
            "wh_pos": wh_pos,
            "wh_word": wh_word,
            "wh_nbor_pos": wh_nbor_pos,
            "root_token": root_token
        }
    return classifier


def pre_process_model(model):
    """
    Removes unnecessary columns from the pandas question model

    :param model: pandas question model
    :return: the popped class column from the pandas question model
    """
    c_class_col = model.pop("c_class")
    f_class_col = model.pop("f_class")
    model.pop("question")
    model.pop("wh_bi_gram")
    return c_class_col,f_class_col


def classify(question, model_path, en_nlp):
    """
    Creates a vector model of the training data along with the question to predict
    :param question: raw text to process as a question
    :param model_path: path to the question json model created by model.py
    :param en_nlp: english language model from spacy
    :return: returns the predicted classification for the question provided
    """
    data_model = []
    c_class_col = []
    f_class_col = []

    with open(model_path) as input_file:
        data_model = pandas.read_json(input_file)
        c_class_col,f_class_col = pre_process_model(data_model)
        input_file.close()

    training_data = pandas.get_dummies(data_model)
    en_doc = en_nlp(u'' + question)
    classifier = process_question(question, en_nlp)

    df_data_frame = []
    df_data_frame.append(classifier)

    df_question = pandas.DataFrame(df_data_frame)

    pred_data = pandas.get_dummies(df_question)

    training_data, pred_data = transform_data_matrix(training_data, pred_data)

    c_class = support_vector_machine(training_data, c_class_col, pred_data)
    f_class = support_vector_machine(training_data, c_class_col, pred_data)

    return c_class[0],f_class[0]


def check_arguments():
    if (len(sys.argv) < 2):
        print("Enter model path:")
        sys.exit(1)
    elif (len(sys.argv) < 3):
        print("Enter a question to classify...")
        sys.exit(1)


def main():
    check_arguments()
    question = " ".join(sys.argv[2:])
    model_path = sys.argv[1]
    en_nlp = spacy.load("en_core_web_md")
    q_class = classify(question, model_path, en_nlp)[0]
    print(q_class)


if __name__ == "__main__":
    main()
