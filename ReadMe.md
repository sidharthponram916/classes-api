# UMD Course Catalog API
This is a project that pulls data from the University of Maryland's Schedule of Classes Website, built using FastAPI + BeautifulSoup. Currently, there is only 1 API endpoint and 2 query strings, but more will be available as development continues. 

**API Endpoint**

-  `/api`: Default Endpoint

**Query**

- `?name=`: Course Name 
- `?date=`: Course Catalog Date

**Sample API Response from** `/api?name=BMGT110`
```
[
  {
    "id": "BMGT110",
    "title": "Introduction to the Business Value Chain",
    "information": [
      "Students are provided with an introduction to the business value chain with an emphasis on inter-organizational and intra-organizational coordination of core business processes. Emphasis is on cross-functional integration and the efficient and effective management of core processes with an emphasis on marketing, operations and supply chain management."
    ],
    "credits": "3",
    "sections": [
      {
        "id": "0101",
        "instructors": [
          "Jeffrey Miller"
        ],
        "open": 41,
        "total": 225,
        "days_info": [
          {
            "days": "MW",
            "start_time": "2:00pm",
            "end_time": "3:15pm",
            "building": "VMH",
            "room": "1524"
          }
        ]
      }
    ]
  },
  {
    "id": "BMGT110S",
    "title": "Introduction to the Business Value Chain",
    "information": [],
    "credits": "3",
    "sections": [
      {
        "id": "0101",
        "instructors": [
          "Oliver Schlake"
        ],
        "open": 7,
        "total": 42,
        "days_info": [
          {
            "days": "MW",
            "start_time": "9:30am",
            "end_time": "10:45am",
            "building": "CCC",
            "room": "1111"
          }
        ]
      },
      {
        "id": "0201",
        "instructors": [
          "Oliver Schlake"
        ],
        "open": 23,
        "total": 42,
        "days_info": [
          {
            "days": "MW",
            "start_time": "11:00am",
            "end_time": "12:15pm",
            "building": "CCC",
            "room": "1111"
          }
        ]
      }
    ]
  }
]
```
