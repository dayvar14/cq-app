from sklearn.svm import LinearSVC
import pandas
import spacy
import sys

from scipy.sparse import csr_matrix


def transform_data_matrix(X_train, X_predict):
    X_train_columns = list(X_train.columns)
    X_predict_columns = list(X_predict.columns)

    X_trans_columns = list(set(X_train_columns + X_predict_columns))
    # print(X_trans_columns, len(X_trans_columns))

    trans_data_train = {}

    for col in X_trans_columns:
        if col not in X_train:
            trans_data_train[col] = [0 for i in range(len(X_train.index))]
        else:
            trans_data_train[col] = list(X_train[col])

    XT_train = pandas.DataFrame(trans_data_train)
    XT_train = csr_matrix(XT_train)
    trans_data_predict = {}

    for col in X_trans_columns:
        if col not in X_predict:
            trans_data_predict[col] = 0
        else:
            trans_data_predict[col] = list(X_predict[col])  # KeyError

    XT_predict = pandas.DataFrame(trans_data_predict)
    XT_predict = csr_matrix(XT_predict)

    return XT_train, XT_predict


def support_vector_machine(X_train, y, X_predict):
    linsvc = LinearSVC()
    linsvc.fit(X_train, y)
    prediction = linsvc.predict(X_predict)
    return prediction


def predict_question(question, en_nlp):
    en_doc = en_nlp(u'' + question)
    sents = list(en_doc.sents)
    sent = sents[0]

    ''' Re Write this'''
    wh_bi_gram = []
    root_token = ""
    wh_pos = ""
    wh_nbor_pos = ""
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
    class_col = model.pop("class")
    model.pop("question")
    model.pop("wh_bi_gram")
    return class_col


def classify(question, model_path, en_nlp):
    data_model = []
    class_col = []

    with open(model_path) as input_file:
        data_model = pandas.read_json(input_file)
        class_col = pre_process_model(data_model)
        input_file.close()

    training_data = pandas.get_dummies(data_model)
    en_doc = en_nlp(u'' + question)
    classifier = predict_question(question, en_nlp)

    df_data_frame = []
    df_data_frame.append(classifier)

    df_question = pandas.DataFrame(df_data_frame)

    pred_data = pandas.get_dummies(df_question)

    training_data, pred_data = transform_data_matrix(training_data, pred_data)

    svm = support_vector_machine(training_data, class_col, pred_data)

    return svm


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
