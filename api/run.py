#!/usr/bin/env python3
import os
from dotenv import load_dotenv, find_dotenv
from src.app import create_app
import pandas as pd 

load_dotenv(find_dotenv())

app = create_app('development')

if __name__ == '__main__':
	

	app.run(host='0.0.0.0', port=8000)
