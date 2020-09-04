const request = require('request');

exports.main = (event, callback) => {
  request('https://catfact.ninja/fact', (error, response, data) => {
    const fact = JSON.parse(data).fact;
      callback({
        botMessage:  fact,
        responseExpected: false
      });
  })
};
