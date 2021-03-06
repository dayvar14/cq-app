#!/usr/bin/env python

"""
    model.py:
        The function of this script is utilize a training set to classify questions. It categorizes questions and creates
        and processes them to be used by classy.py.
"""

__author__ = "Daniel Ayvar"

import json
import spacy
import sys


def read_input_file(file_path):
    """
    Reads an file containing the classified question set and return a list of the questions fields
    within a dictionary.

    :param file_path: file path to the json data model created by ts_json
    :return: returns a list of question json objects
    """

    question_list = []

    with open(file_path, 'r') as file:
        for line in file:
            line_arr = line.split()
            coarse_class,fine_class = line_arr[0].split(":")
            question = " ".join(line_arr[1:])
            question_list.append({"question":question,"fine":fine_class,"coarse":coarse_class})
        file.close()

    return question_list


def write_output_file(file_path, classifiers):
    """
    Write classifiers into a output file as json array

    :param file_path: file path to the output file
    :param classifiers: a list of the processed questions
    :return: Writes a json model to the file_path given
    """
    with open(file_path, 'w+') as output_file:
        json.dump(classifiers,output_file, sort_keys=True, indent=4, separators=(',', ': '))


def clear_output_file(file_path):
    """
        Creates output file. If output file already exists, the contents are cleared.
    """
    with open(file_path, "w+") as file:
        file.truncate(0)
        file.close()


def process_question(question_obj, en_nlp):
    """
    Processes a question by saving the question term ('Who','When','What','How'), saving it's Part of Speech Tag. It also
    saves it's bigram and the neighbor's part of speech tag.

    :param question_obj: a question from the .json training data set created from ts_json.py
    :param en_nlp: a language model obtained from spacy
    :return: returns the required data from the question
    """
    en_doc = en_nlp(u'' + question_obj["question"])
    sentences = list(en_doc.sents)
    sentence = sentences[0]

    wh_bi_gram = []
    root_token = ""
    wh_pos = ""
    wh_nbor_pos = ""
    wh_word = ""
    for token in sentence:
        if token.tag_ == "WDT" or token.tag_ == "WP" or token.tag_ == "WP$" or token.tag_ == "WRB":
            wh_pos = token.tag_
            wh_word = token.text
            wh_bi_gram.append(token.text)
            wh_bi_gram.append(str(en_doc[token.i + 1]))
            wh_nbor_pos = en_doc[token.i + 1].tag_
        if token.dep_ == "ROOT":
            root_token = token.tag_

    classifier = {
        "question": question_obj["question"],
        "f_class": question_obj["fine"],
        "c_class": question_obj["coarse"],
        "wh_pos": wh_pos,
        "wh_word": wh_word,
        "wh_bi_gram": wh_bi_gram,
        "wh_nbor_pos": wh_nbor_pos,
        "root_token": root_token
    }
    return classifier


def main():
    if (len(sys.argv) < 2):
        print("Need input path and output path...")
        sys.exit(1)
    elif (len(sys.argv) < 3):
        print("Need output path...")
        sys.exit(1)

    en_nlp = spacy.load("en_core_web_md")

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    questions = read_input_file(input_path)
    classifiers = []
    for question in questions:
        classifiers.append(process_question(question, en_nlp))

    write_output_file(output_path, classifiers)

    print("Question classifier model created.")


if __name__ == "__main__":
    main()
