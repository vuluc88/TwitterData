# Twitter API test

## Requirements

* Python 2.7.x
* PIP

## Installing requirements
```
    pip install flask-restful
```

Download source code
Navigate to code directory and run following command

```
    python setup.py develop
```


## Start the server
In the code directory, run command
```
    python main.py
```
By default, the app will run at localhost, port 5000. If you want to run on other port, go to file main.py and edit the port in this line of code
```
    app.run(debug=False, port=5000)
```
Open browser, <http://localhost:5000>


## Using the APIs
There're 2 APIs

### Get tweets by hashtag
- **Description:** This api will return the list of tweets search by given hashtag
- **Uri:** /hashtags/<string:hashtag_str>
- **Method:** GET
- **Return data type:** json
- **Parameters:**
    - **limit:** the limit number of tweets to return. It is set to 30 by default
- **Example url call:** http://127.0.0.1:5000/hashtags/bowsette?limit=1
- **Example result data:**
```
[
    {
        account: {
                fullname: "xSinCarax[INC]",
                href: "/REALxSinCarax",
                id: 104753299
            },
        text: "#Peachette #Bowsette #Toadette #bowserette #bowserpeach #bowser #peachser and now #SinCaraette ? https:// twitter.com/SINfulAngel__/ status/1044930097000730624 …",
        retweets: 0,
        replies: 0,
        date: "Wed, 26 Sep 2018 19:51:18",
        likes: 1
    }
]
```

### Get tweets by user
- **Description:** This api will return the list of tweets search by given username
- **Uri:** /users/<string:user_str>
- **Method:** GET
- **Return data type:** json
- **Parameters:**
    - **limit:** the limit number of tweets to return. It is set to 30 by default
- **Example url call:** http://127.0.0.1:5000/users/realdonaldtrump?limit=1
- **Example result data:**
```
[
    {
        account: {
                fullname: "Donald J. Trump",
                href: "/realDonaldTrump",
                id: 25073877
            },
        text: "Jobless Claims fell to their lowest level in 49 years!",
        retweets: 6788,
        replies: 4772,
        date: "Wed, 26 Sep 2018 17:57:30",
        likes: 30383
    }
]
```


### Stop server 
In running server
Ctrl+C