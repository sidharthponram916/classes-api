from bs4 import BeautifulSoup
import requests

def get_course_info(name, date):
    url = f'https://app.testudo.umd.edu/soc/search?courseId={name}&sectionId=&termId={date}&_openSectionsOnly=on&creditCompare=%3E%3D&credits=0.0&courseLevelFilter=ALL&instructor=&_facetoface=on&_blended=on&_online=on&courseStartCompare=&courseStartHour=&courseStartMin=&courseStartAM=&courseEndHour=&courseEndMin=&courseEndAM=&teachingCenter=ALL&_classDay1=on&_classDay2=on&_classDay3=on&_classDay4=on&_classDay5=on'

    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
    else:
        return { "message": "Failed to retrieve webpage."}
    
    soup = BeautifulSoup(html, "html.parser")

    courses = soup.find_all("div", class_="course"); 
    outputs = []
    for course in courses: 
        course_id = course.find("div", class_="course-id")
        credits = course.find("span", class_="course-min-credits")
        title = course.find("span", class_="course-title")
        information = course.find_all("div", class_="approved-course-text"); 
        course_info = []

        for i in information: 
            inf = i.text.strip() if i else "N/A"
            course_info.append(inf); 


        course_id_text = course_id.text.strip() if course_id else "N/A"
        credits_text = credits.text.strip() if credits else "N/A"
        title_text = title.text.strip() if title else "N/A"

    # Sections 
        sections_html = course.find_all("div", class_="section")
        sections = []

        for section_html in sections_html: 
        
            section_id = section_html.find("span", class_="section-id")
            section_open_seats = section_html.find("span", class_="open-seats-count")
            section_total_seats = section_html.find("span", class_="total-seats-count")

            section_instructors = section_html.find_all("span", class_="section-instructor")

            instructors = []
            for instructor in section_instructors: 
                instructors.append(instructor.text.strip() if instructor else "N/A")

            class_days = section_html.find("div", class_="class-days-container").find_all("div", class_="row")

            day_info = []
            for day in class_days: 
                section_days = day.find("span", class_="section-days")
                start_time = day.find("span", class_="class-start-time")
                end_time = day.find("span", class_="class-end-time")
                building = day.find("span", class_="building-code")
                room = day.find("span", class_="class-room")

                d = { 
                    "days": section_days.text.strip() if section_days else "N/A", 
                    "start_time": start_time.text.strip() if start_time else "N/A", 
                    "end_time": end_time.text.strip() if end_time else "N/A", 
                    "building": building.text.strip() if building else "N/A", 
                    "room": room.text.strip() if room else "N/A"
                }

                day_info.append(d); 

            section =  {
                "id": section_id.text.strip() if section_id else "N/A", 
                "instructors": instructors, 
                "open": int(section_open_seats.text.strip()) if section_open_seats else None, 
                "total":  int(section_total_seats.text.strip()) if section_total_seats else None, 
                "days_info": day_info
            }

            sections.append(section)
        
        outputs.append({
        "id": course_id_text,
        "title": title_text, 
        "information": course_info, 
        "credits": credits_text,
        "sections": sections
        })
    
    return outputs; 
