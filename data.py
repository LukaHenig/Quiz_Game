#--------------------------------------------------------#
#File: day quiz_brain                                    #
#Programmed by: Luka Henig (luka.henig@gmail.com)        #
#Curse: 100 Days of Code udemy                           #
#Date: 02/03/2022                                        #
#Description:Litle quiz game to learn und understand     #
#working with an input from API                          #
#--------------------------------------------------------#

#-------------------------IMPORTS------------------------#
import requests

#parameters for the API-request
parameters = {
    "amount": 10,
    "type": "boolean",
    "category": 18,
}
respond = requests.get(url="https://opentdb.com/api.php", params=parameters)
respond.raise_for_status()
question_data = respond.json()["results"]