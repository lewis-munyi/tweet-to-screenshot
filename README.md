
<p align="center">
  <a href="https://example.com/">
    <img src="https://source.unsplash.com/SyzQ5aByJnE/200x200">
  </a>
</p>
<p align="center">
  <h2 align="center">Tweet-to-screenshot</h2>
</p>

<p align="center">
    A Python/node.js app that grabs tweets from your favorite profiles, filters them according to a search string, and saves a screenshot of the tweet.
</p>
<p align="center">
    <a href="https://www.buymeacoff.ee/lewismunyi" target="_blank"><img src="https://www.buymeacoffee.com/assets/img/custom_images/orange_img.png" alt="Buy Me A Coffee" style="height: 41px !important;width: 174px !important;box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;-webkit-box-shadow: 0px 3px 2px 0px rgba(190, 190, 190, 0.5) !important;" ></a>
</p>


## Table of contents

- [Getting started](#getting-started)
- [Prerequisites](#prerequisites)
- [Installing](#installing)
- [Running the app](#running-the-app)
    - [Running the web scraper](#running-the-web-scraper)
    - [Running cloud functions](#running-cloud-functions)
- [Deployment](#deployment)
- [Built With](#built-with)
- [Versioning](#versioning)
- [Authors](#authors)
- [License](#license)
- [Acknowledgments](#acknowledgments)
# Tweet to screenshot

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

You will need these to run and set up the app
* [Python 3]("https://www.python.org/downloads/")
* [Pip]('https://pypi.org/project/pip/')
* [Node.js]('https://nodejs.org) installed on your PC

### Installing

1. Clone or download the repo from [this]("https://github.com/lewis-munyi/tweet-to-screenshot") url and extract it.

2. Open your console and change into that directory
    ```
   cd tweet-to-screenshot/
   ```
3. List the contents of the directory.
    ```
    ls
    ```
4. You should have such a directory structure
   ```
   javascript-web-scraper/
   └── config.py
   |── .gitignore
   │── .env.example
   |── tweet.py           
   |── search.js
   |── ...
   │── ...     
   |── index.js
   └── package.json
   ```
   
  5. Install the required python modules
      ```
      npm install
      ```
  6. Install the required modules for npm
       ```
       pip install -r requirements.txt
       ```
 7. Copy the `.env.example` file to `.env`
       ```
        cp .env.example .env
     ```
9. Visit the twitter [developer]("http://developer.twitter.com/") page to get your apps API keys.
8. Enter your twitter API keys in the respective fields of the `.env` file. Makes sure you add them in the `.env` file, and not the `.env.example` file.  
    ```
    CONSUMER_KEY = ""
    CONSUMER_SECRET = ""
    ACCESS_KEY = ""
    ACCESS_SECRET = ""
    ``` 

10. That's it!


## Running the app

The app is split into two parts;
* A web scraping application that scraps data and stores it in Cloud firestore
* Cloud functions that are triggered and run when updating the Telegram bot. 

### Running the app

1. Open the `config.py` file and add the usernames of the people who's tweets you want to harvest.
    Add them in the `profiles` object.
    ```
    profiles = [
        "username1",
        "username2"
    ]
   ```
2. Open your console and from the root(`/`) directory, run 
    ```
    python ./tweets.py
   ```
    It should display the progress of the harvesting activity.
3. To search and take a screenshot. open `search.js`
4. In the `search_term` object, add the string you want to query. E.g.
    ```
    search_terms = [
        "strawberry ice cream",
        "marshmallows"
    ]
    ```
5. Run 
    ```
    npm run start
    ```
6. It will open the tweets and save the screenshot to the `/images` directory.

7. If you want to get rid of the pop up windows, change the `state` flag in `search.js` to `true`
    ```
    export const state = true
    ```

Yaay! It works.

## Deployment

Work in progress ...

## Built With

* [Tweepy](https://nuxtjs.org/) - Tweet harvesting library
* [Pupeeteer](https://pptr.dev/) - Puppeteer is a Node library which provides a high-level API to control Chrome or Chromium over the DevTools Protocol

## Contributing

Currently accepting pull requests.

## Authors

* **Lewis Munyi** - *Dev* - [Website](https://lewismunyi.web.app)

See also the list of [contributors](https://github.com/lewis-munyi/javascript-web-scraper/graphs/contributors) who participated in this project.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details

## Acknowledgments

* Hat tip to anyone whose code was used

Enjoy :metal:
