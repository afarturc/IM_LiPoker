const apiConfig = {
    baseUrl: 'http://127.0.0.1:5000/',
  };
  
async function buyIn(value) {
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
        throw error;
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
        return data;
    })
    .catch(error => {
        throw error;
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
        throw error;
    });
}

async function affirm_bet() {
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
        throw error;
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
        throw error;
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
        throw error;
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
        throw error;
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
        throw error;
    });
}

export {buyIn, call, fold, check, raise, affirm_bet, deny_bet, all_in}