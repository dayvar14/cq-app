## Question Classification Server

### Introduction
This project's goal is to create a server that can accept a questions and send back to the client the classification of 
the sent question.

### Get started with Anaconda
To learn more about installing anaconda, go [here](https://docs.anaconda.com/anaconda/install/)

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

Download dependencies flask-restful, and spacy
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

### Creating the training model
This application uses one of many training models pr

### Running the application
To startup server run the sh file 'start_server.sh'
```
sh start_server.sh
```

Once finished, the terminal will show the default address

Alternatively The server can be started by running the python file main.py.
You just have to include the path of your trained model file.
```
python main.py "train_5000.model"
```

### Running the test client
To test the server you can run the sh file 'start_client.sh'\
The script accepts one argument enclosed by quotations
```
sh start_client.sh "Who is Don Cornero?"
#Prints
Message sent: { 'question' : 'Who is Don Cornero'}
Message recieved: { 'class' : 'HUM'} 
```

Alternatively The client can be started by running the python file test_client.py.
```
python test_client.py "Who is Don Cornero?"
```

Classification can be decoded using the [Question Classification Taxonomy](https://cogcomp.seas.upenn.edu/Data/QA/QC/definition.html)

### Test Cases
```
    #Input
    sh start_client.sh "How much does a Macbook Air cost?"
    #Output
    Message sent: {'question':'How much does a Macbook Air cost?'}
    Message recieved: {'class':'NUM'}

    #Input
    sh start_client.sh "Where can i go for a drink around here?"
    #Output
    Message sent: {'question':'Where can i go for a drink around here?'}
    Message recieved: {'class':'LOC'}

    #Input
    sh start_client.sh "Who is Don Cornero?"
    #Output
    Message sent: {'question':'Who is Don Cornero?'}
    Message recieved: {'class':'HUM'}

    #Input
    sh start_client.sh "How are you feeling today?"
    #Output
    Message sent: {'question':'How are you feeling today?'}
    Message recieved: {'class':'DESC'}
    
    #Input
    sh start_client.sh "What does a cake recipe consist of?"
    #Output
    Message sent: {'question':'What does a cake recipe consist of?'}
    Message recieved: {'class':'ENTY'}

    #Input
    sh start_client.sh "When does the movie release in theaters?"
    #Output
    Message sent: {'question':'When does the movie release in theaters?'}
    Message recieved: {'class':'NUM'}

    #Input
    sh start_client.sh "Where is the Sears Tower?"
    #Output
    Message sent: {'question':'Where is the Sears Tower?'}
    Message recieved: {'class':'LOC'}

    #Input
    sh start_client.sh "Who is Iron Man?"
    #Output
    Message sent: {'question':'Who is Iron Man?'}
    Message recieved: {'class':'HUM'}

    #Input
    sh start_client.sh "What is the powerhouse of the cell?"
    #Output
    Message sent: {'question':'What is the powerhouse of the cell?'}
    Message recieved: {'class':'DESC'}
    
    #Input
    sh start_client.sh "What inspired Micheal Jordan?"
    #Output
    Message sent: {'question':'What inspired Micheal Jordan?'}
    Message recieved: {'class':'ENTY'}
```
