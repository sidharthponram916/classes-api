from fastapi import FastAPI, HTTPException 
from bs4 import BeautifulSoup 
from fastapi.middleware.cors import CORSMiddleware
from app.scrapers import scraper 

app = FastAPI()

origins = [
        "http://localhost",
        "http://localhost:3000",
    ]
    
app.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["GET", "POST", "PUT", "DELETE", "OPTIONS"],
        allow_headers=["*"],
)

@app.get("/")
def read_root(): 
    return { "Message": "Welcome to the Testudo Schedule of Classes API"}

@app.get("/api/get-courses")
def get_course_information(name: str, date: str = "202508"):
    url = f'https://app.testudo.umd.edu/soc/search?courseId={name}&sectionId=&termId={date}&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on'
    return scraper.get_course_info(url)

@app.get("/api/get-gen-ed-courses")
def get_gen_ed_courses(name: str, date: str = "202508"): 
    url = f'https://app.testudo.umd.edu/soc/gen-ed/{date}/{name}'
    return scraper.get_gen_ed_courses(url)