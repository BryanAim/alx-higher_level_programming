$.get('https://swapi.co/api/films/?format=json', function (data) {
  const myList = data.results;
  for (const element of myList) {
    $('UL#list_movies').append('<li>' + element.title + '</li>');
  }
});
