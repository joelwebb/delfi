# Delfi_trie_and_api
Example code comparing trie performances on DNA sequences and a simple API.

The API uses a simple RESTful architecture connected to a simple database to store information on laboratory sites, freezers and containers.   

Additionally there are Swagger docs available with the API using [Swagger UI](http://swagger.io/swagger-ui/) which can be viewed at the /docs path in your browser.

## Setup

Requires at least Python 3, tested with 3.6.9

Relies on [Flask](http://flask.pocoo.org/docs/0.11/) and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/index.html) for the webserver and REST API. 

After cloing the repository, open a terminal inside the repository directory.

Create a virtual environment if necessary with venv:

```shell
python3 -m pip install virtualenv
python3 -m venv env
source env/bin/activate
```

Then to install the necessary packages install the requirements.txt file:

```shell
$ pip install -r requirements.txt
```

## Running the API

To start the API move into the API folder. 

```shell
$ python3 api/run.py  
```

## Testing the API
All API methods are behind a `/` base URL 

You can explore the API using Swagger UI by opening the root URL (that is printed to the terminal when you run the server) in your web browser - see an example image of this in action below.

While running venv, your host address might be different than localhost, so check http://192.168.1.9:8000/docs/ or http://localhost:8000/docs/ for the swagger UI. 
Swaggeer will provide example curl commands to test the API. 

You can integrate with a client that supports swagger/OpenAPI schemas by using the swagger docs in `/static/swagger.json`.

## Seeding the db
To seed the DB, visit http://localhost:8000/seed --- this will load some sample static files from csv to pre-populate the database with dummy data. Then your api calls should work.


# Trie comparison
After looking through github, there are about 15 python packages by google and other research teams for generating tries with different optimization techniques.
For the sake of the coding challenge, I made a simple dictionary implementation that performs prefix lookup and can act similarly to a trie under the hood.
To compare how well this performed, I also created tries using two other open source implementations in python - marisa & pytrie. 

## Benchmarking
Importantly for memory optimization - marisa-trie that uses a static implementation is the most memory optimized, while my dictionary implementation runs the quickest on a dataset of 10,000 samples.

Benchmarks for memory usage were running using the time package with an example below:
/usr/bin/time --verbose python3 compare_trie_performance.py

The python script contains code to compare benchmark time comparisons for creating 3 different Trie structures and performance evaluation demonstrating that the marisa static tries outperform other dictionary based methods in terms of memory efficiency. Other dictionary implementations can execute quicker, but at a tradeoff of higher memory costs. 

During intermediate testing I also used a snippit for comparison purposes saved a profile.py from https://stackoverflow.com/questions/552744/how-do-i-profile-memory-usage-in-python

## Results
![image](https://user-images.githubusercontent.com/25040566/132502578-e4d89e6b-501c-4398-a83a-327c880c1cb2.png)

## Using Individual Tries

To check an individual tree, there are assert statements and print statements in the __main__ section. 
To run one, try:
```shell
$ python3 trie/simple_trie.py 
$ python3 trie/pytrie_testing.py
$ python3 trie/marissa_testing.py
```

## Running in Docker

A dockerfile is included to create a containerised microservice - build and run from the repository directory with:

```
$ git clone https://github.com/joelwebb/delfi.git
$ cd delfi
$ sudo docker build -t delfi:latest .
$ sudo docker run -d -p 8000:8000 defli 
```

**Note** 
On my windows machine building the image put the image in a different location: docker.io/library/delfi:latest

So make sure you call the run command on the right image location or it wont work.

Then when the image is running, visit: http://localhost:8000/docs/ to view the swagger UI.



## Limitations

- For production DB purposes, swap to Mongo or AWS RDS over the local db. Since there was no indication of purpose of deployment/application integration, a simple local DB was integrated that can also be run in memory.
- For the trie testing, since no other requirements were provided marisa-trie is the most memory efficient. However since this is a static implementation, you are limited to creating the trie whenever new data is added - whereas pytrie supports additions to the trie structure out of the box. 


