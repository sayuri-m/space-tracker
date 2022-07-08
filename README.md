# space tracker

Simple app made in Python3 using the framework Flask.

-----

# Getting Started
To run the project you should have python3.8
install Flask (https://flask.palletsprojects.com/en/2.1.x/installation/)

set the variables

```
export FLASK_APP=flaskr
export FLASK_ENV=development
```

and run flask through python
```
python3.8 -m flask run
```

The root opens a webview with all the options already displayed.
http://127.0.0.1:5000/


# Requests
GET http://127.0.0.1:5000/latest

GET http://127.0.0.1:5000/next

GET http://127.0.0.1:5000/upcoming

GET http://127.0.0.1:5000/past

# Response
The response consists in a array with the launch infos in json format.

```
[
{"id": "62a9f0e320413d2695d88713", "model": "Starlink 3-1 (v1.5)", "date": "2022-07-11T01:00:00.000Z", "success": null, "icon": "62a9f0e320413d2695d88713.png"},

{"id": "6243ae40af52800c6e919259", "model": "CRS-25", "date": "2022-07-15T00:30:00.000Z", "success": null, "icon": "6243ae40af52800c6e919259.png"},

{"id": "62a9f0f820413d2695d88714", "model": "Starlink 4-22 (v1.5)", "date": "2022-07-01T00:00:00.000Z", "success": null, "icon": "62a9f0f820413d2695d88714.png"},

{"id": "62a9f10b20413d2695d88715", "model": "Starlink 3-2 (v1.5)", "date": "2022-07-01T00:00:00.000Z", "success": null, "icon": "62a9f10b20413d2695d88715.png"},

{"id": "62a9f12820413d2695d88716", "model": "Starlink 4-25 (v1.5)", "date": "2022-07-01T00:00:00.000Z", "success": null, "icon": "62a9f12820413d2695d88716.png"}
]
```
