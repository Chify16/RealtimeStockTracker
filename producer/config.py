import logging #for logging errors and information
import os
from venv import logger #for accessing environment variables
from dotenv import load_dotenv #for loading environment variables from .env file
load_dotenv()

#configure logging
logging.basicConfig(
    filename='stock_data.logs.log',
    level=logging.INFO, #set the logging level to INFO -why only INFO? because we want to log all the information, warnings, and errors. If we set it to WARNING, we will only log warnings and errors. If we set it to ERROR, we will only log errors.
    format='%(asctime)s - %(levelname)s - %(message)s' #set the time,level(different levels of logging like ERROR, WARNING, INFO), and message format for the logs
)

logger = logging.getLogger(__name__) #create a logger object for this module

BASE_URL = "alpha-vantage.p.rapidapi.com" #create a variable to store the base URL for the API
url = f"https://{BASE_URL}/query" #url for the API  

api_key = os.getenv("API_KEY") #create a variable to store the API key from the environment variable


headers = {
	"x-rapidapi-key": api_key, #get the API key from the environment variable
	"x-rapidapi-host": BASE_URL #get the base URL from the environment variable
}