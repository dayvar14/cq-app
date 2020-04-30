## Question Classification Server

### Introduction
This project's goal is to create a server that can accept a questions and send back to the client the classification of 
the sent question.

### Get started with Anaconda
To install anaconda go to https://docs.anaconda.com/anaconda/install/

After installing anaconda, we need to create a anaconda environment

```
conda create -n cq-env python=3.8.2 anaconda
conda update conda
```

### Installing Dependencies

Activate the newly created environment to install the required dependencies
```
conda activate cq-env
```

Download dependencies pandas, flask, flask-restful, scikit-learn, sparse, and spacy
```
#Flask Restful
conda install -c conda-forge flask-restful

#Spacy
conda install -c conda-forge spacy

```

In the terminal, download language model using spacy

```
python -m spacy download en_core_web_md
```

### Running the application
To startup server run the sh file 'start_server.sh'
```
sh start_server.sh
```

Once finished, the terminal will show the default address

### Running the test client
To test the server you can run the sh file 'start_client.sh'\
The script accepts one argument enclosed by quotations
```
sh start_client.sh "Who is Don Cornero?"
#Prints
Message sent: { 'question' : 'Who is Don Cornero'}
Message recieved: { 'class' : 'HUM'} 
```

Classification can be decoded using the Question Classification Taxonomy https://cogcomp.seas.upenn.edu/Data/QA/QC/definition.html
