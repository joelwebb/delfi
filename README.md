# Delfi_trie_and_api
Example code comparing trie performances on DNA sequences and a simple API.

The API uses a simple RESTful architecture with CRUD operations connected to a simple mysql database to store information on laboratories, freezers and containers.   

Additionally there are Swagger docs available with the API using [Swagger UI](http://swagger.io/swagger-ui/).

## Setup

Requires at least Python 3, tested with 3.6.9

Relies on [Flask](http://flask.pocoo.org/docs/0.11/) and [Flask-RESTPlus](https://flask-restplus.readthedocs.io/en/stable/index.html) for the webserver and REST API. 

To get these clone the repository, open a terminal inside the repository directory and run:

```shell
$ pip install -r requirements.txt
```

## Running

Run with `-h` for full usage options.

```shell
$ python delfi_sample_api.py -h
```

## Tests
python3 tests/test_api.py

python3 tests/test_trie.py


## Benchmark Results
Benchmarks for memory usage were running using the time package with an example below:
/usr/bin/time --verbose python3 compare_trie_performance.py

The python script contains code to compare benchmark time comparisons for creating 3 different Trie structures and performance evaluation demonstrating that the marisa static tries outperform other dictionary based methods in terms of memory efficiency. Other dictionary implementations can execute quicker, but at a tradeoff of higher memory costs. 

![image](https://user-images.githubusercontent.com/25040566/132502578-e4d89e6b-501c-4398-a83a-327c880c1cb2.png)



## Usage



**NOTE:** All API methods are behind a `/api` base URL (Swagger UI hides this away at the very bottom of the web page).

You can explore the API using Swagger UI by opening the root URL (that is printed to the terminal when you run the server) in your web browser - see an example image of this in action below.

You can integrate with a client that supports swagger/OpenAPI schemas by just reading the schema directly from `/api/schema`.


## Running in Docker

A dockerfile is included to create a containerised microservice - build and run from the repository directory with:

```
sudo docker build -t #TODO
sudo docker run -p #TODO 
```

Now you can navigate to `http://127.0.0.1:5000/` in your web browser to access the SwaggerUI of the container.

## Limitations

- For production DB purposes, swap to Mongo or RDS Athena =over mysql. Since there was no indication of purpose of deployment/application integration, a simple mysql DB was integrated.
- 

