#!/usr/bin/env python

"""
    test_client.py:
        The function of this script is utilize a training set to classify questions
"""

__author__ = "Daniel Ayvar"

import requests
import sys


def check_arguments():
    if(len(sys.argv)<2):
        print("Enter a question to classify...")
        sys.exit(1)


def main():
    check_arguments()
    question = " ".join(sys.argv[1:])
    data = {'question': question }

    r = requests.post("http://127.0.0.1:5000", json=data)
    print(r.text)

    print(data)


if __name__ == '__main__':
    main()
