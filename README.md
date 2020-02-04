# Data-Model-GraphQL

## Project Overview

In order to bring user held data models to the world, we need to ensure data models follow commonly accepted principles, widely used customs as well as universality to be meaningful and widely compatible.

This project tracks the building of a user held data model and API. It is based on benchmarks such as IAB Techlabs open standard content taxonomy and CINTs open standard taxonomy.

The user data model is used to build customized user data profiles that are accessed using GraphQL. The user makes these profiles available in exchange for customized services by giving permissioned API access, in the form of data profiles. 

Access to data profiles is always controlled by the individual by setting permissions by which access to the data profile is granted. The individual has the ability and right to manage those permissions, granting, modifying and revoking them. 

### Version Summary

This is the initial version of the API.

The current API does not enforce or include the access permissions. 

It includes some sample data to understand the data model and possible profile use cases. 

### Permissioned Access

![permissions](media/Harvard_Post_Redesign_V3.jpg)

### User Profiles

This project demonstrates how a data profile could be accessed using the GraphQL API and user data model. Two example data profiles are queried below: 

1. A media profile where the information made available would be useful for a media company to use to give customized recommendations to the user.
2. A local activity profile where the information made available would be useful for a discounting company like groupon to use to give local activity recommendations to the user.

### How to Use This Project

A current version of the data model and API is available for download and use. 

There are several use cases that are being trialed in segments such as consumer finance, media, travel, similar to this project. Creating different use cases based on this idea is encouraged. For more information and support, please get in touch at developers@prifina.com

### Open Source License

This project is licensed under the Mozilla Public License with terms found herein https://en.wikipedia.org/wiki/Mozilla_Public_License

### Dependencies

Use of this project requires Python 3 with the following dependencies installed:
```
pip install SQLAlchemy
pip install graphene_sqlalchemy
pip install Flask
pip install Flask-GraphQL
```

### File Descriptions

- models.py - python file containing database models of the user model
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
4. Use the GraphiQL interface to query the database

### Sample GraphQL Query and Response

#### Full Query
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
        foodandbeverages {
          edges {
            node {
              id
              fastfoodweeklyfrequency
              alcoholweeklyfrequency
              restaurantweeklyfrequency
            }
          }
        }
        hobbiesandinterests {
          edges {
            node {
              id
              exerciseweeklyfrequency
              cinemaweeklyfrequency
              favoritemusicgenre
            }
          }
        }
        educations {
          edges {
            node {
              id
              highestdegree
              areaofstudy
            }
          }
        }
      }
    }
  }
}
```
#### Full Response
```
{
  "data": {
    "allBasics": {
      "edges": [
        {
          "node": {
            "id": "QmFzaWM6MQ==",
            "age": 34,
            "name": "Melanie",
            "gender": "female",
            "households": {
              "edges": [
                {
                  "node": {
                    "id": "SG91c2Vob2xkOjE=",
                    "income": "over 120,000",
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
                    "organization": "ExxonMobil",
                    "employeedepartment": "Petrophysics",
                    "employeeprimaryrole": "Data Analyst"
                  }
                }
              ]
            },
            "foodandbeverages": {
              "edges": [
                {
                  "node": {
                    "id": "Rm9vZGFuZGJldmVyYWdlOjE=",
                    "fastfoodweeklyfrequency": 0,
                    "alcoholweeklyfrequency": 3,
                    "restaurantweeklyfrequency": 3
                  }
                }
              ]
            },
            "hobbiesandinterests": {
              "edges": [
                {
                  "node": {
                    "id": "SG9iYmllc2FuZGludGVyZXN0czox",
                    "exerciseweeklyfrequency": 5,
                    "cinemaweeklyfrequency": 1,
                    "favoritemusicgenre": "rock"
                  }
                }
              ]
            },
            "educations": {
              "edges": [
                {
                  "node": {
                    "id": "RWR1Y2F0aW9uOjE=",
                    "highestdegree": "Masters",
                    "areaofstudy": "Petroleum Engineering"
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
                    "income": "50,000 to 60,000",
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
            "foodandbeverages": {
              "edges": [
                {
                  "node": {
                    "id": "Rm9vZGFuZGJldmVyYWdlOjI=",
                    "fastfoodweeklyfrequency": 2,
                    "alcoholweeklyfrequency": 0,
                    "restaurantweeklyfrequency": 2
                  }
                }
              ]
            },
            "hobbiesandinterests": {
              "edges": [
                {
                  "node": {
                    "id": "SG9iYmllc2FuZGludGVyZXN0czoy",
                    "exerciseweeklyfrequency": 1,
                    "cinemaweeklyfrequency": 2,
                    "favoritemusicgenre": "classic"
                  }
                }
              ]
            },
            "educations": {
              "edges": [
                {
                  "node": {
                    "id": "RWR1Y2F0aW9uOjI=",
                    "highestdegree": "Masters",
                    "areaofstudy": "Business Administration"
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
#### Media Profile Query
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
              highestdegree
              areaofstudy
            }
          }
        }
      }
    }
  }
}
```
#### Media Profile Response
```
{
  "data": {
    "allBasics": {
      "edges": [
        {
          "node": {
            "id": "QmFzaWM6MQ==",
            "age": 34,
            "name": "Melanie",
            "gender": "female",
            "households": {
              "edges": [
                {
                  "node": {
                    "id": "SG91c2Vob2xkOjE=",
                    "income": "over 120,000",
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
                    "organization": "ExxonMobil",
                    "employeedepartment": "Petrophysics",
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
                    "highestdegree": "Masters",
                    "areaofstudy": "Petroleum Engineering"
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
                    "income": "50,000 to 60,000",
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
                    "highestdegree": "Masters",
                    "areaofstudy": "Business Administration"
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
#### Local Activity Profile Query
```
{
  allBasics {
    edges {
      node {
        id
        age
        name
        gender
        foodandbeverages {
          edges {
            node {
              id
              fastfoodweeklyfrequency
              alcoholweeklyfrequency
              restaurantweeklyfrequency
            }
          }
        }
        hobbiesandinterests {
          edges {
            node {
              id
              exerciseweeklyfrequency
              cinemaweeklyfrequency
              favoritemusicgenre
            }
          }
        }
      }
    }
  }
}
```
#### Local Activity Profile Response
```
{
  "data": {
    "allBasics": {
      "edges": [
        {
          "node": {
            "id": "QmFzaWM6MQ==",
            "age": 34,
            "name": "Melanie",
            "gender": "female",
            "foodandbeverages": {
              "edges": [
                {
                  "node": {
                    "id": "Rm9vZGFuZGJldmVyYWdlOjE=",
                    "fastfoodweeklyfrequency": 0,
                    "alcoholweeklyfrequency": 3,
                    "restaurantweeklyfrequency": 3
                  }
                }
              ]
            },
            "hobbiesandinterests": {
              "edges": [
                {
                  "node": {
                    "id": "SG9iYmllc2FuZGludGVyZXN0czox",
                    "exerciseweeklyfrequency": 5,
                    "cinemaweeklyfrequency": 1,
                    "favoritemusicgenre": "rock"
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
            "foodandbeverages": {
              "edges": [
                {
                  "node": {
                    "id": "Rm9vZGFuZGJldmVyYWdlOjI=",
                    "fastfoodweeklyfrequency": 2,
                    "alcoholweeklyfrequency": 0,
                    "restaurantweeklyfrequency": 2
                  }
                }
              ]
            },
            "hobbiesandinterests": {
              "edges": [
                {
                  "node": {
                    "id": "SG9iYmllc2FuZGludGVyZXN0czoy",
                    "exerciseweeklyfrequency": 1,
                    "cinemaweeklyfrequency": 2,
                    "favoritemusicgenre": "classic"
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
