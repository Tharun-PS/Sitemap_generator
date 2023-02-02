from selenium import webdriver
import os

chrome_options = webdriver.ChromeOptions()
chrome_options.binary_location = os.environ.get("GOOGLE_CHROME_BIN")
chrome_options.add_argument("--headless")
chrome_options.add_argument("--disable-dev-shm-usage")
chrome_options.add_argument("--no-sandbox")
driver = webdriver.Chrome(executable_path=os.environ.get("CHROMEDRIVER_PATH"), chrome_options=chrome_options)

from flask import Flask, request, jsonify, render_template
from flask_cors import CORS, cross_origin
# from selenium import webdriver
from selenium.webdriver.common.by import By
# app = Flask(__name__)

app = Flask(__name__)
CORS(app)


# path = "C:\\Users\\THARUN\\Desktop\\Papersdrop\\Scrapping\\chromedriver2.exe"
# driver = webdriver.Chrome(path)

# # scraped = []

# @app.route('/') #scraped
# def scraper():
#     return jsonify()

list1 = []


@app.route('/', methods=['GET'])
@cross_origin()
def add_scrap():
    
    website="https://www.papersdrop.com/"
#     scrap = request.get_json()
    driver.get(website)
    links = driver.find_elements_by_tag_name('a')
    print(links)

    for link in links:
        lnk = link.get_attribute("href")
        list1.append(lnk)
    driver.close()

    dic1 = {"output": list1}
    return jsonify(dic1)


if __name__ == "__main__":
    app.run(debug=True)
