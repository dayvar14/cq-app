#!/usr/bin/env python

"""
    ts_json.py:
        The function of this script is to convert the training sets from https://cogcomp.seas.upenn.edu/Data/QA/QC/
        to a json file that is easier to utilize.
"""

__author__ = "Daniel Ayvar"

import json
import sys


def json_from_training_set(input_path, output_path):
    """
    Converts the .label training data to a json format
    :param input_path: A path to the .label training data found on https://cogcomp.seas.upenn.edu/Data/QA/QC/
    :param output_path: A path to the desired location for the .json training data
    :return: writes to the output_path
    """
    input_file = open(input_path, 'r')
    output_file = open(output_path, 'w')
    json_arr = []

    for line in input_file:
        line_arr = line.split()
        coarse_classifier, fine_classifier = line_arr[0].split(":")
        question = " ".join(line_arr[1:])

        object = {
            "coarse": coarse_classifier,
            "fine": fine_classifier,
            "question": question
        }

        json_arr.append(object)

    json.dump(json_arr, output_file)


def main():
    if (len(sys.argv) < 2):
        print("Need input path and output path...")
        sys.exit(1)
    elif (len(sys.argv) < 3):
        print("Need output path...")
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]

    json_from_training_set(input_path, output_path)
    print("Training set converted to json.")


if __name__ == "__main__":
    main()
