[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/oWm-EAsM)
# Museum-Project
## Overlook:
  Group Members:
    Jerome Barcelona #UCID 30185184,
    Alyan Qureshi #UCID 30169810

  Project Distribution:
    Almost everything was worked on together over call or in person, but we had certain specilaizations and focus
    on different areas for both members. 
    
    Jerome mainly focused around the python development, but created the relational
    diagram model as well as helped in MySQL script database creation.

    Alyan mainly worked with the MySQL script and queries, but also lent a hand in creating guest display for
    python and created the EERD Diagaram.

  Program Notes:
    As stated in d2l, we were given the option to either choose employee or admin interface. After
    logging into database through personal SQL password, you may view the program as either
    a guest or employee.

   If Guest is Chosen (intended for the average user):
      -You are allowed to view information regarding artworks, exhibitions, participating (known artists)
      and participating collections.
      -artworks, collections and artists all have a feature to type the respective primary key, showing
      the rest of the hidden information for the user's convinience.
      -All of the data is front end and display only, 
      you cannot make any changes to the info.

  **Assuming that you went through proper procedures (no login needed)**
   If Employee is chosen (assumed employee has experience with program and knows what they are looking for):
    -You are greeted by a main employee menu. You may add information, remove information, and edit information 
    within the database.
    -Adding will work with the tables, employees are prompted to enter in the information as needed.
    
    Unless prompted, you should not leave any inputs blank.
    -error handling was coded to counter such failures in the off chance in happens, but it is assumed that employees are not
    trying to break the program and only use it as intended.
    - There are proper insturctions that the employee can follow, but other than that it is assumed that they know what they are
    putting in other than than having to memorize id's etc.
    -The program will display those respective ID's when working with operations that the employee may forget an id or require to look
    for one.
    -employees can then go back to guest menu to verify their changes, or as well as checkin gthrough display functions
    triggerede by edit functions.
    
Features
  -Login authentication to connect to database (after building on local MySql, will take user's personal password)
  -All minimum features have been included as followed on term project 300 guideline on d2l.
  -Guests can view all the information they need regarding all tables in the museum database.
  -Employees can ADD, EDIT, and REMOVE information through commands in respective menu's/options.
  -Admin was not implemented due to optional bonus choice.
  -Mulltiple Try Except statements implemented to counter incorrect syntax, runtime errors or unusable values.

**--END of NOTES**

## Organization:
- code folder: contains your main python application code
- sql scripts folder: contains all sql scripts required (database creation and initialization, sql script with query tasks in the handout, etc...)
- database design folder: EERD and relational schema
- optional data folder: has data files that you can sue to load data to your application if you use this optional implementation requirement
