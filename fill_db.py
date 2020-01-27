from models import engine, db_session, Base, Basic, Education, Occupation, Household
Base.metadata.create_all(bind=engine)

tyler = Basic(name='Tyler', age=34, gender='male')
db_session.add(tyler)
degree = Education(highesteducation='Masters', basic=tyler)
db_session.add(degree)
job = Occupation(organization='Prifina', employeedepartment='Information Technology', employeeprimaryrole='Data Analyst', basic=tyler)
db_session.add(job)
house = Household(numberofpersonsinhome=3, maritalstatus='Married', numberofchildren=1, accomodationtype='Apartment', income=120000, basic=tyler)
db_session.add(house)

steve = Basic(name='Steve', age=55, gender='male')
db_session.add(steve)
degree_steve = Education(highesteducation='Masters', basic=steve)
db_session.add(degree_steve)
job_steve = Occupation(organization='Google', employeedepartment='Marketing and Sales', employeeprimaryrole='Sales Engineer', basic=steve)
db_session.add(job_steve)
house_steve = Household(numberofpersonsinhome=4, maritalstatus='Married', numberofchildren=2, accomodationtype='House', income=55000, basic=steve)
db_session.add(house_steve)

db_session.commit()
