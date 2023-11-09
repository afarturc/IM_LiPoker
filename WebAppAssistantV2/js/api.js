const apiConfig = {
    baseUrl: 'http://127.0.0.1:5000/',
  };

const defaultMessage = "Desculpe não percebi, pode voltar a repetir a pergunta?"
  
async function buy_in(value) {
    return fetch(`${apiConfig.baseUrl}/buy_in`, {
        method: 'POST',
        body: new URLSearchParams({ value }),
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function raise(value) {
    return fetch(`${apiConfig.baseUrl}/raise`, {
        method: 'POST',
        body: new URLSearchParams({ value }),
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        let message = data.message;
        return message
    })
    .catch(error => {
        return defaultMessage
    });
}

async function all_in() {
    return fetch(`${apiConfig.baseUrl}/all_in`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function confirm_bet() {
    return fetch(`${apiConfig.baseUrl}/affirm_bet`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function deny_bet() {
    return fetch(`${apiConfig.baseUrl}/deny_bet`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function call() {
    return fetch(`${apiConfig.baseUrl}/call`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function fold() {
    return fetch(`${apiConfig.baseUrl}/fold`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function check() {
    return fetch(`${apiConfig.baseUrl}/check`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function request_hand_order(hands) {
    const possible_hands = ["High Card", "Carta Alta", "Pair", "Par", "Two Pair", "2 Pares", "Three of a Kind", "Trio", "Straight", "Sequência", "Flush", "Full House", "Four of a Kind", "Poker", "Straight Flush", "Royal Flush"]
    const matching_hands = hands.filter(hand => possible_hands.includes(hand))

    return fetch(`${apiConfig.baseUrl}/request_hand_order`, {
        method: 'POST',
        body: new URLSearchParams({ "hand1": matching_hands[0], "hand2": matching_hands[1]}),
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        let message = data.message;
        return message
    })
    .catch(error => {
        return defaultMessage
    });
}

async function request_handboard() {
    return fetch(`${apiConfig.baseUrl}/request_handboard`, {
        method: 'POST',
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        return data;
    })
    .catch(error => {
        return defaultMessage
    });
}

async function select_username(value) {
    return fetch(`${apiConfig.baseUrl}/select_username`, {
        method: 'POST',
        body: new URLSearchParams({ "username": value }),
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        let message = data.message;
        return message
    })
    .catch(error => {
        return defaultMessage
    });
}

async function request_more_chips(value) {
    return fetch(`${apiConfig.baseUrl}/request_more_chips`, {
        method: 'POST',
        body: new URLSearchParams({ "amount-of-money": value }),
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        let message = data.message;
        return message
    })
    .catch(error => {
        return defaultMessage
    });
}

async function change_value(value) {
    return fetch(`${apiConfig.baseUrl}/change_value`, {
        method: 'POST',
        body: new URLSearchParams({ "amount-of-money": value }),
        headers: {
        'Content-Type': 'application/x-www-form-urlencoded',
        },
    })
    .then(response => response.json())
    .then(data => {
        let message = data.message;
        return message
    })
    .catch(error => {
        return defaultMessage
    });
}

export {buy_in, call, fold, check, raise, confirm_bet, deny_bet, all_in, request_hand_order, request_handboard, select_username, request_more_chips, change_value}