import json

# The provided JSON data
data_json = """
{
  "data": [
    [
      "Post Name",
      "Total Post",
      "KVS Various Post Eligibility"
    ],
    [
      "Primary Teacher",
      "6414",
      "Bachelor Degree with 50% Marks and B.Ed Exam Passed. OR 10+2 with 50% Marks and 2 Year Diploma in Elementary Education OR 10+2 with 50% Marks and B.El.Ed / 2 Year Diploma in Education (Special)\n\nCTET Paper I Exam Passed.\n\nMaximum Age : 30 Years."
    ],
    [
      "Junior Secretarial Assistant",
      "702",
      "10+2 Intermediate Exam in Any Recognized Board in India.\n\nEnglish Typing : 35 WPM OR\n\nHindi Typing : 30 WPM\n\nMaximum Age : 27 Years."
    ],
    [
      "Stenographer Grade II",
      "54",
      "10+2 Intermediate Exam in Any Recognized Board in India.\n\nDictation : 10 Mts @ 80 WPM\n\nTranscription : 50 Mts English,  65 Mts Hindi\n\nMaximum Age : 27 Years."
    ],
    [
      "Senior Secretarial Assistant",
      "322",
      "Bachelor Degree in Any Stream with 3 Year Experience.\n\nMaximum Age : 30 Years."
    ],
    [
      "Hindi Translator",
      "11",
      "Master Degree in Hindi with English as Subject in Degree Level OR Master Degree in English with Hindi as Subject in Degree Level OR Master Degree in Any Subject with Hindi Medium and English as a Subject in Degree Level OR Master Degree in Any Subject with English Medium and Hindi as a Subject in Degree Level OR Master Degree in Any Subject with Hindi and English as a Compulsory Subject in Degree Level\n\nDiploma / Certificate in Translation.\n\nMaximum Age : 35 Years.\n\nMore Eligibility Details Read Notification."
    ],
    [
      "Assistant Section Officer ASO",
      "156",
      "Bachelor Degree in Any Stream with 3 Year Experience.\n\nMaximum Age : 35 Years."
    ],
    [
      "Assistant Engineer Civil",
      "02",
      "BE / B.Tech Degree in Civil Engineering with 2 Year Experience OR Diploma in Civil Engineering with 5 Year Experience.\n\nMaximum Age : 35 Years."
    ],
    [
      "Finance Officer",
      "06",
      "Bachelor Degree in Commerce with 50% Marks and 4 Year Experience OR M.Com 50% Marks with 3 Year Experience OR CA / ICWA / MBA Finance / PGDM with Experience.\n\nMaximum Age : 35 Years."
    ],
    [
      "Primary Teacher (Music)",
      "303",
      "10+2 with 50% Marks with Degree in Music.\n\nMaximum Age : 30 Years."
    ],
    [
      "Librarian",
      "355",
      "Bachelor Degree / Diploma in Library Science\n\nMaximum Age : 35 Years."
    ],
    [
      "Post Graduate Teacher (PGT Various Subject)",
      "1409",
      "Master Degree in Related Subject with Minimum 50% Marks.\n\nB.Ed Exam Passed (Exempt for PGT Computer Science  / Bio Technology)\n\nMaximum Age : 40 Years.\n\nFor Subject Wise Eligibility Details Read the Notification."
    ],
    [
      "Trained Graduate Teacher (TGT Various Subject)",
      "3176",
      "Bachelor Degree in Related Subject with Minimum 50% Marks.\n\nCTET Paper II Exam Passed\n\nB.Ed Exam Passed\n\nMaximum Age : 35 Years.\n\nFor Subject Wise Eligibility Details Read the Notification."
    ],
    [
      "Assistant Commissioner",
      "52",
      "Master Degree with 45% Marks\n\nB.Ed Exam Passed\n\nExperience\n\nMaximum Age : 50 Years."
    ],
    [
      "Principal",
      "239",
      "Master Degree with 45% Marks\n\nB.Ed Exam Passed\n\nExperience\n\nAge : 35-50 Years."
    ],
    [
      "Vice Principal",
      "203",
      "Master Degree with 50% Marks\n\nB.Ed Exam Passed\n\nExperience\n\nAge : 35-45 Years."
    ]
  ]
}
"""

# Load the JSON data
data = json.loads(data_json)

# Extract the "data" list from the JSON
data_list = data.get("data", [])

# Check for sublists with a length not equal to 7
sublists_not_equal_to_7 = [sublist for sublist in data_list if len(sublist) != 7]

# Print the sublists with a length not equal to 7
for sublist in sublists_not_equal_to_7:
    print(sublist)
