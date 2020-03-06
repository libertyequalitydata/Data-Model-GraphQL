# Local Activity Profile

Local activity profile is queried from GraphQL model.

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
