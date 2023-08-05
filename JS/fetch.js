fetch('StarcraftCharacters.json')
  .then((response) => response.json())
  .then((data) => {
    data.forEach((character) => {
      console.log('Race:', character.race);
      console.log('Name:', character.name);
      console.log('Age:', character.age);
      console.log('Home Planet:', character.homePlanet);
      console.log('----------------------');
    });
  })
  .catch((error) => {
    console.error('Error fetching or parsing data:', error);
  });
