# Data-Model-GraphQL

## Project Overview

In order to bring user held data models to the world, we need to ensure data models follow commonly accepted principles, widely used customs as well as universality to be meaningful. This project tracks the building of a global taxonomy, using benchmarks such as IAB Techlabs open standard content taxonomy and CINTs open standard taxonomy.

The open standard will be public, developer centric and widely adoptable.

Tools are being rolled out gradually, with work ongoing on all fronts.

## 


## How to Use This Project

### Dependencies

Use of this project requires Python 3 with the following dependencies installed:
- SQLAlchemy
- graphene_sqlalchemy
- Flask
- Flask-GraphQL

### File Descriptions

- models.py - python file containing database models
- schema.py - python file which defines GraphQL graph structure for database models
- app.py - python file for running GraphQL and GraphiQL views in Flask
- database.sqlite3 - database containing dummy data for demonstration purposes
- fill_db.py - python script for putting data into database (can modify to change dummy data)

### Instructions

1. Download the files into a folder on your local computer
2. Open the command line and run: 
```
python app.py
```
3. Open http://127.0.0.1:5000/graphql in your browser
4. Query GraphQL

### Sample GraphQL Query and Response

#### Query
```
{
  allBasics {
    edges {
      node {
        id
        age
        name
        gender
        households {
          edges {
            node {
              id
              income
              numberofchildren
              numberofpersonsinhome
              maritalstatus
              accomodationtype
            }
          }
        }
        occupations {
          edges {
            node {
              id
              organization
              employeedepartment
              employeeprimaryrole
            }
          }
        }
        educations {
          edges {
            node {
              id
              highesteducation
            }
          }
        }
      }
    }
  }
}
```
#### Response
```
{
  "data": {
    "allBasics": {
      "edges": [
        {
          "node": {
            "id": "QmFzaWM6MQ==",
            "age": 34,
            "name": "Tyler",
            "gender": "male",
            "households": {
              "edges": [
                {
                  "node": {
                    "id": "SG91c2Vob2xkOjE=",
                    "income": 120000,
                    "numberofchildren": 1,
                    "numberofpersonsinhome": 3,
                    "maritalstatus": "Married",
                    "accomodationtype": "Apartment"
                  }
                }
              ]
            },
            "occupations": {
              "edges": [
                {
                  "node": {
                    "id": "T2NjdXBhdGlvbjox",
                    "organization": "Prifina",
                    "employeedepartment": "Information Technology",
                    "employeeprimaryrole": "Data Analyst"
                  }
                }
              ]
            },
            "educations": {
              "edges": [
                {
                  "node": {
                    "id": "RWR1Y2F0aW9uOjE=",
                    "highesteducation": "Masters"
                  }
                }
              ]
            }
          }
        },
        {
          "node": {
            "id": "QmFzaWM6Mg==",
            "age": 55,
            "name": "Steve",
            "gender": "male",
            "households": {
              "edges": [
                {
                  "node": {
                    "id": "SG91c2Vob2xkOjI=",
                    "income": 55000,
                    "numberofchildren": 2,
                    "numberofpersonsinhome": 4,
                    "maritalstatus": "Married",
                    "accomodationtype": "House"
                  }
                }
              ]
            },
            "occupations": {
              "edges": [
                {
                  "node": {
                    "id": "T2NjdXBhdGlvbjoy",
                    "organization": "Google",
                    "employeedepartment": "Marketing and Sales",
                    "employeeprimaryrole": "Sales Engineer"
                  }
                }
              ]
            },
            "educations": {
              "edges": [
                {
                  "node": {
                    "id": "RWR1Y2F0aW9uOjI=",
                    "highesteducation": "Masters"
                  }
                }
              ]
            }
          }
        }
      ]
    }
  }
}
```



## Acknowledgements
