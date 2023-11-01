from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import argparse

# creating a Flask app 
app = Flask(__name__)

# init driver
driver = webdriver.Edge()
action = ActionChains(driver) 
  
# on the terminal type: curl http://127.0.0.1:5000/ 
# returns hello world when we use GET. 
# returns the data that we send when we use POST. 
@app.route('/', methods = ['GET', 'POST']) 
def home(): 
    if(request.method == 'GET'): 
  
        data = "hello world"
        return jsonify({'data': data})
    
@app.route('/buy_in', methods = ['POST'])
def buy_in():
    if (request.method == 'POST'):
        value = request.form.get("value")

        if value:
            input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[9]/div[2]/div/input')
            button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[9]/div[2]/div/div[2]/button[1]')
            action.send_keys_to_element(input, value)
            action.click(on_element=button)
            action.click(on_element=button)
            action.perform()
            return jsonify({'message': f"Vou entrar em jogo com {value}"})
        else:
            return jsonify({'message': "Entrada inválida"})
        
    
@app.route('/call', methods = ['POST'])
def call():
    if (request.method == 'POST'):
        call_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[9]/div[2]/div/div[2]/button[1]')
        action.click(on_element = call_button)
        action.perform()

        return jsonify({'message': "Vou a jogo"})
  
# driver function 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LiPokerAPI settings")
    parser.add_argument('key', help="Game key")
    args = parser.parse_args()
  
    driver.get(f"https://lipoker.io/game/{args.key}")
    app.run(debug = True)