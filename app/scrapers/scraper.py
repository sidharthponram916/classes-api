from bs4 import BeautifulSoup
import requests


# async def fetch_professor_rating(session, name): 
#     async with session.get(f'https://planetterp.com/api/v1/professor?name={name}', ssl=False) as response: 
#         if response.status == 200: 
#             data = await response.json()
#             rating = data.get("average_rating", "N/A")
#             slug = data.get("slug", "N/A")

#             return { "name": name, "planet_terp_rating": rating, "slug": slug}
#         else: 
#             return { "name": name, "planet_terp_rating": "N/A", "slug": "N/A"}

# async def fetch_all_ratings(instructor_names): 
#     async with aiohttp.ClientSession() as session: 
#         tasks = [fetch_professor_rating(session, name) for name in instructor_names]
#         results = await asyncio.gather(*tasks)
#     return { inst["name"]: inst for inst in results }



def get_course_info(url):
    response = requests.get(url)

    if response.status_code == 200:
        html = response.text
    else:
        return { "message": "Failed to retrieve webpage."}
    
    soup = BeautifulSoup(html, "html.parser")

    courses = soup.find_all("div", class_="course"); 
    outputs = []
    instructor_set = set()

    for course in courses: 
        sections_html = course.find_all("div", class_="section")
        for section_html in sections_html: 
            instructors = section_html.find_all("span", class_="section-instructor")
            for instructor in instructors: 
                instructor_name = instructor.text.strip()
                if instructor_name: 
                    instructor_set.add(instructor_name)

    for course in courses: 
        course_id = course.find("div", class_="course-id")
        credits = course.find("span", class_="course-min-credits")
        title = course.find("span", class_="course-title")

        information = course.find_all("div", class_="approved-course-text"); 
        course_info = []

        gen_ed = course.find_all("span", class_="course-subcategory")
        gen_ed_flags = [g.text.strip() if g else "N/A" for g in gen_ed]


        for i in information: 
            inf = i.text.strip() if i else "N/A"
            course_info.append(inf); 


        course_id_text, credits_text, title_text = (
            course_id.text.strip() if course_id else "N/A",
            credits.text.strip() if credits else "N/A",
            title.text.strip() if title else "N/A"
        )


    # Sections 
        sections_html = course.find_all("div", class_="section")
        sections = []

        section_instructors_cache = {}
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
        "flags": gen_ed_flags,
        "title": title_text, 
        "information": course_info, 
        "credits": credits_text,
        "sections": sections
        })
    
    return outputs; 

def get_gen_ed_courses(url): 
    return get_course_info(url); 



