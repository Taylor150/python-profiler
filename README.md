# python-profiler
This python program uses some open-source API's, the user simply inputs their first name and the program will use these API's to guess your nationality, age and gender.  This program is made using python using 'requests' and 'json' packages.  The purpose of this project is purely for practice purposes.

## API's
The three API's that I used for this project were:
- [Nationalize](https://nationalize.io/)
- [Agify](https://agify.io/)
- [Genderize](https://genderize.io/)

Nationalize is a simple API which preditcs your nationality based on your name, I then paired this with Agify which uses your name (and also localization for more accuracy) to guess your age. I used the output from the nationalize API as input for Agify alongside the users input name. Finally the same thing is done with genderize. These guesses are then all output using the print function.

## Packages
The two packages I used for this project were:
- [JSON](https://www.w3schools.com/python/python_json.asp)
- [Requests](https://pypi.org/project/requests/) 

Python has a built-in package called json, which can be used to work with JSON data. It gives you the ability to covert JSON data (commonly used format for API's) and convert it to Python. This then allows you to define variables amd key's etc. It also gave me the ability to re-format the output as there was a lot of data that I did not want to be displayed to the user. 
Requests is a simple, yet elegant HTTP library. Requests allows you to send HTTP/1.1 requests extremely easily. There’s no need to manually add query strings to your URLs, or to form-encode your PUT & POST data. This package allowed me to take the input from the user and add it to the API url with a get request, and then requesting the output json. 

## Purpose
The purpose of this application was a self-set challenge as a way for me got improve my python skills. I am curretnly in the progress of learning programming in the hopes of becoming a software engineer in the future. 

## Plans
Although I am happy with the current state of the program, It is mainly a proof of concept and a gimmick more than a practical/useful tool. I will be happy to call it finished when: 
- [x] Guesses users nationality, age & gender
- [ ] GUI
- [ ] Provides probabilty of accuracy
