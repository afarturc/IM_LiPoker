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
  
@app.route('/request_hand_order', methods = ['POST'])
def request_hand_order():
    hands = {
        "High Card": 0, 
        "Carta Alta": 0,
        "Pair": 1,
        "Par": 1,
        "Two Pair": 2,
        "2 Pares": 2,
        "Three of a Kind": 3,
        "Trio": 3,
        "Straight": 4,
        "Sequência": 4,
        "Flush": 5,
        "Full House": 5,
        "Four of a Kind": 6,
        "Poker": 6,
        "Straight Flush": 7,
        "Royal Flush": 8,
    }

    if (request.method == 'POST'):
        hand1 = request.form.get("hand1")
        hand2 = request.form.get("hand2")

        highest_hand = max(hand1, hand2, key=hands.get)
        other_hand = min(hand1, hand2, key=hands.get)

        return jsonify({'message': f"{highest_hand} é maior do que {other_hand}"})
    
@app.route('/request_handboard', methods = ['POST'])
def request_handboard():
    if (request.method == 'POST'):
        handboard_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[8]/div[1]/div')
        screen = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div[1]/div[8]/div[3]/div/div[2]')
        action.click(on_element=handboard_button)
        action.pause(3)
        action.click(on_element=screen)
        action.perform()

        return jsonify({'message': "Aqui estão as mãos"})

@app.route('/select_username', methods = ['POST'])
def select_username():
    if (request.method == 'POST'):
        username = request.form.get("username")

        input = driver.find_element(By.XPATH, '//*[@id="input-username"]')
        play_button = driver.find_element(By.XPATH, '//*[@id="root"]/div/div[6]/div/div[2]/div/div[2]/button[2]')
        action.send_keys_to_element(input, username)
        action.click(on_element=play_button)
        action.perform()

        return jsonify({'message': f"Bom jogo, {username}"})

# driver function 
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="LiPokerAPI settings")
    parser.add_argument('key', help="Game key")
    args = parser.parse_args()
  
    driver.get(f"https://lipoker.io/game/{args.key}")
    app.run(debug=True)