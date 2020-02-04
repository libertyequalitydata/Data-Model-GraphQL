from models import engine, db_session, Base, Basic, Education, Occupation, Household, Foodandbeverage, Hobbiesandinterests
Base.metadata.create_all(bind=engine)

tyler = Basic(name='Tyler', age=34, gender='male')
db_session.add(tyler)
degree = Education(highestdegree='Masters', areaofstudy='Computer Science', basic=tyler)
db_session.add(degree)
job = Occupation(organization='Prifina', employeedepartment='Information Technology', employeeprimaryrole='Data Analyst', basic=tyler)
db_session.add(job)
house = Household(numberofpersonsinhome=3, maritalstatus='Married', numberofchildren=1, accomodationtype='Apartment', income='over 120,000', basic=tyler)
db_session.add(house)
foods = Foodandbeverage(fastfoodweeklyfrequency=0, alcoholweeklyfrequency=3, restaurantweeklyfrequency=3, basic=tyler)
db_session.add(foods)
hobbies = Hobbiesandinterests(cinemaweeklyfrequency = 1, exerciseweeklyfrequency = 5, favoritemusicgenre = 'rock', basic=tyler)
db_session.add(hobbies)



steve = Basic(name='Steve', age=55, gender='male')
db_session.add(steve)
degree_steve = Education(highestdegree='Masters', areaofstudy='Business Administration', basic=steve)
db_session.add(degree_steve)
job_steve = Occupation(organization='Google', employeedepartment='Marketing and Sales', employeeprimaryrole='Sales Engineer', basic=steve)
db_session.add(job_steve)
house_steve = Household(numberofpersonsinhome=4, maritalstatus='Married', numberofchildren=2, accomodationtype='House', income='50,000 to 60,000', basic=steve)
db_session.add(house_steve)
foods_steve = Foodandbeverage(fastfoodweeklyfrequency = 2, alcoholweeklyfrequency = 0, restaurantweeklyfrequency = 2, basic=steve)
db_session.add(foods_steve)
hobbies_steve = Hobbiesandinterests(cinemaweeklyfrequency = 2, exerciseweeklyfrequency = 1, favoritemusicgenre = 'classic', basic=steve)
db_session.add(hobbies_steve)

db_session.commit()
