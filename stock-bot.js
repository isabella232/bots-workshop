const request = require('request');
exports.main = (event, callback) => {
  const stockApiKey = process.env['STOCK_API_KEY']
  const stockTickerToCheck = event.userMessage.message;
  
  request(`https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol=${stockTickerToCheck}&apikey=${stockApiKey}`, (error, response, data) => {
    const jsonData = JSON.parse(data);
    const stockData = jsonData["Time Series (Daily)"];
    const mostRecentDate = Object.keys(stockData)[0];
    const mostRecentData = stockData[mostRecentDate];
    const open = mostRecentData['1. open'];
    const close = mostRecentData['4. close'];
    const min = mostRecentData['3. low'];
    const max = mostRecentData['2. high'];

    callback({
      botMessage: `<b>${mostRecentDate}</b><ul><li>open: ${open}</li><li>max: ${max}</li><li>min: ${min}</li><li>close: ${close}</li></ul>`,
      responseExpected: false
    });
  });
};
