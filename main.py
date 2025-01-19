from fastapi import FastAPI, HTTPException 
from bs4 import BeautifulSoup 
from scrapers import scraper 

app = FastAPI()

@app.get("/")
def read_root(): 
    return { "Message": "Welcome to the Testudo Schedule of Classes API"}

@app.get("/api")
def get_course_information(name: str, date: str = "202501"):
    return scraper.get_course_info(name, date)