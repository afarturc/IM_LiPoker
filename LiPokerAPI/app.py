from flask import Flask, jsonify, request
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains 
import argparse
from flask_cors import CORS

# creating a Flask app 
app = Flask(__name__)
cors = CORS(app)

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
        value = str(request.form.get("value"))

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
        
@app.route('/raise', methods = ['POST'])
def raise_bet():
    if (request.method == 'POST'):
        value = str(request.form.get("value"))

        bet_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div[1]/div[9]/div[2]/div/div[1]/button[1]')
        action.click(on_element=bet_button)
        action.perform()
        action.pause(1)

        if value:
            bet_input = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div[1]/div[9]/div[2]/div/div/div[1]/div[2]/input')
            action.send_keys_to_element(bet_input, value)
            action.perform()

        return jsonify({'message': f"Vou fazer uma aposta"})
        
@app.route('/all_in', methods = ['POST'])
def all_in():
    if (request.method == 'POST'):
        bet_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div[1]/div[9]/div[2]/div/div[1]/button[1]')
        action.click(on_element=bet_button)
        action.perform()
        action.pause(1)

        all_in_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[9]/div[2]/div/div/div[1]/div[1]/button[5]')
        action.click(on_element=all_in_button)
        action.perform()

        return jsonify({'message': f"Apostar tudo"})
        
@app.route('/affirm_bet', methods = ['POST'])
def affirm_bet():
    if (request.method == 'POST'):
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div[1]/div[9]/div[2]/div/div/div[2]/div[1]/button[1]')
        action.click(on_element = button)
        action.perform()

        return jsonify({'message': "Confirmar aposta"})
    
@app.route('/deny_bet', methods = ['POST'])
def deny_bet():
    if (request.method == 'POST'):
        button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div[1]/div[9]/div[2]/div/div/div[2]/div[2]/button[1]')
        action.click(on_element = button)
        action.perform()

        return jsonify({'message': "Não confirmar aposta"})
        
@app.route('/call', methods = ['POST'])
def call():
    if (request.method == 'POST'):
        call_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[9]/div[2]/div/div[2]/button[1]')
        action.click(on_element = call_button)
        action.perform()

        return jsonify({'message': "Vou a jogo"})
    
@app.route('/fold', methods = ['POST'])
def fold():
    if (request.method == 'POST'):
        call_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[9]/div[2]/div/div[3]/button[1]')
        action.click(on_element = call_button)
        action.perform()

        return jsonify({'message': "Eu desisto da mão"})
    
@app.route('/check', methods = ['POST'])
def check():
    if (request.method == 'POST'):
        call_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[9]/div[2]/div/div[2]/button[1]')
        action.click(on_element = call_button)
        action.perform()

        return jsonify({'message': "Dou check"})
  
# driver function 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LiPokerAPI settings")
    parser.add_argument('key', help="Game key")
    args = parser.parse_args()
  
    driver.get(f"https://lipoker.io/game/{args.key}")
    app.run(debug=True)