## Question Classification Server

### Introduction
This project's goal is to create a server that can accept a questions and send back to the client the classification of 
the sent question.

### Get started with Anaconda
To install anaconda go to https://docs.anaconda.com/anaconda/install/

After installing anaconda, we need to create a anaconda environment

```
conda create -n cq-env python=3.8.2 anaconda
```

### Installing Dependencies

Activate the newly created environment to install the required dependencies
```
conda activate cq-env
```

Download dependencies pandas, flask, flask-restful, scikit-learn, sparse, and spacy
```
#Pandas
conda install pandas

#Flask
conda install -c anaconda flask 

#Flask Restful
conda install -c conda-forge flask-restful

#Scikit Learn
conda install -c anaconda scikit-learn

#Sparse
conda install -c conda-forge sparse

#Spacy
conda install -c conda-forge spacy

```

In the terminal, download language model using spacy

```
python -m spacy download en_core_web_sm
```

### Running the application
To runn