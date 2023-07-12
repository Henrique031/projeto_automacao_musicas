const axios = require('axios')

async function shazam() {

  const options = {
      method: 'GET',
      url: 'https://shazam.p.rapidapi.com/search',
      params: {
        term: 'Dormi na praça',
        limit: '1'
      },
      headers: {
        'X-RapidAPI-Key': '0951140fd6msh5542201cc7ed94ep179e77jsn6a933da5a8c9',
        'X-RapidAPI-Host': 'shazam.p.rapidapi.com'
      }
}

  try {
    axios.request(options)
    .then(res => console.log(res))

  } catch (error) {
    console.error(error)
  }
}

shazam()