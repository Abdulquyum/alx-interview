#!/usr/bin/node
const { argv } = require('process');
const request = require('request');

const movieID = argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieID}`;


request(url, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
      const filmData = JSON.parse(body);
      const characters = filmData.characters;
	  
      characters.forEach(characterUrl => {
           request(characterUrl, (charError, charResponse, charBody) => {
             if (charError) {
                console.error(charError);
             } else {
               const characterData = JSON.parse(charBody);
               console.log(characterData.name);
             }
         });
      });
    }
});
