# Ecommerce Profile

The ecommerce profile is part of a permissions based user held data model. The user enables ecommerce companies access to his profile in order to get customized services from the ecommerce company.

The ecommerce profile has a generic version as well as several enhanced versions for specific retail segments.

#### Ecommerce Segments

The list of segments is based on amazon.com categories.

1. Arts & Crafts
2. Automotive
3. Baby
4. Beauty & Personal Care
5. Books
6. Computers
7. Digital Music
8. Electronics
9. Women's Fashion
10. Men's Fashion
11. Boys' Fashion
12. Girls' Fashion
13. Generic
14. Health & Household
15. Home & Kitchen
16. Industrial & Scientific
17. Luggage
18. Movies & TV
19. Music, CDs & Vinyl
20. Pet Supplies
21. Software
22. Sports & Outdoors
23. Tools & Home Improvement
24. Toys & Games
25. Video Games

#### Ecommerce Profile Queries and Responses

The ecommerce profiles are: generic profile + segment

Here, the generic ecommerce profile is queried from the GraphQL model.

#### Ecommerce Generic Profile Query
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
#### Ecommerce Generic Profile Response
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
#### Ecommerce Additional Segments Responses
´´´
´´´

