# Lab 9: Course Catalog
# Description: The program lets the user enter a course number, then it displays the course's room number, instructor, and meeting time. 
#   If the course is not in the dictionary, a message is displayed. The program continues to ask for course number until 
#   the user chooses to quit.
##########################################################################################################################################################################################
# Data Dictionary:
# Name                                          Purpose
# -----------------                             ----------------------------
# course_catalog_instructor_map                 dictionary that maps the course numbers to the instructors
# course_catalog_meeting_time_map               dictionary that maps the course numbers to the meeting times
# course_catalog_room_number_map                dictionary that maps the course numbers to the room numbers
# entered_course_number                         string of the course number entered by the user
# meeting_time                                  string of the requested course meeting time
# instructor                                    string of the requested course instructor
# room_number                                   string of the requested course room number
##########################################################################################################################################################################################

# Create the dictionaries that map the course number to the course's room number, instructor, and meeting time.
course_catalog_room_number_map = {
    'CS101': '3004', 
    'CS102': '4501', 
    'CS103': '6755', 
    'NT110': '1244', 
    'CM241': '1411'
}

course_catalog_instructor_map = {
    'CS101': 'Haynes', 
    'CS102': 'Alvarado', 
    'CS103': 'Rich', 
    'NT110': 'Burke', 
    'CM241': 'Lee'
}
course_catalog_meeting_time_map = {
    'CS101': '8:00 a.m.', 
    'CS102': '9:00 a.m', 
    'CS103': '10:00 a.m', 
    'NT110': '11:00 a.m', 
    'CM241': '1:00 p.m'
}

# Ask the user to enter a course number
entered_course_number = str(input('Enter a course number or press Enter to stop: '))

# Loop that continues to ask for course number and displays the course information or gives an error message until the user chooses to quit
while entered_course_number != '':    
    if entered_course_number in course_catalog_room_number_map:
        room_number = course_catalog_room_number_map.get(entered_course_number)
        instructor = course_catalog_instructor_map.get(entered_course_number)
        meeting_time = course_catalog_meeting_time_map.get(entered_course_number)
        print ('The details for course', entered_course_number, 'are:')
        print ('Room:', room_number)
        print ('Instructor:', instructor)
        print ('Time:', meeting_time)
    # Error handling 
    else:
        print(entered_course_number, 'is an invalid course number.')
    
    entered_course_number = str(input('Enter a course number or press Enter to stop: '))
