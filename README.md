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
This application uses one of many question training sets provided by the [University of Pennsylvania](https://cogcomp.seas.upenn.edu/Data/QA/QC/).
Download one of training sets to create a training question model for our application.
```
python model.py train_5500.label train_5500.model
```
This model is used later as an argument to start the server with main.py

### Running the application
To startup server run the sh file 'start_server.sh'
```
sh start_server.sh
```

Once finished, the terminal will show the default address

Alternatively The server can be started by running the python file main.py.
You just have to include the path of your trained model file.
```
python main.py "train_5500.model"
```

### Running the test client
To test the server you can run the sh file 'start_client.sh'\
The script accepts one argument enclosed by quotations
```
sh start_client.sh "Who is Don Cornero?"
#Prints
 
```

Alternatively The client can be started by running the python file test_client.py.
```
python test_client.py "Who is Don Cornero?"
#Output
Message sent: {'question': 'Who is Don Cornero?'}
Message recieved: {"c_class": "HUM", "f_class": "ind"}

```

Classification can be decoded using the [Question Classification Taxonomy](https://cogcomp.seas.upenn.edu/Data/QA/QC/definition.html).
The attribute "c_class" represents the broader classification of the question, while "f_class" represents the finer category within the coarse classification


### Test Case
```
Message sent: {'question': 'How much does a Macbook Air Cost?'}
Message recieved: {"c_class": "NUM", "f_class": "count"}

Message sent: {'question': 'Where can i get a drink of water?'}
Message recieved: {"c_class": "LOC", "f_class": "other"}

Message sent: {'question': 'Who is Don Cornero?'}
Message recieved: {"c_class": "HUM", "f_class": "ind"}

Message sent: {'question': 'How are you feeling today?'}
Message recieved: {"c_class": "DESC", "f_class": "manner"}

Message sent: {'question': 'What does a cake recipe consist of?'}
Message recieved: {"c_class": "ENTY", "f_class": "exp"}

Message sent: {'question': 'When does the move release in theaters?'}
Message recieved: {"c_class": "NUM", "f_class": "date"}

Message sent: {'question': 'Where is the Sears Tower?'}
Message recieved: {"c_class": "LOC", "f_class": "other"}

Message sent: {'question': 'Who is Iron Man?'}
Message recieved: {"c_class": "HUM", "f_class": "ind"}

Message sent: {'question': 'What is the powerhouse of the cell?'}
Message recieved: {"c_class": "DESC", "f_class": "def"}

Message sent: {'question': 'What inspired Micheal Jordan?'}
Message recieved: {"c_class": "ENTY", "f_class": "ind"}
```
