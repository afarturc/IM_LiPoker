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

export {buyIn}