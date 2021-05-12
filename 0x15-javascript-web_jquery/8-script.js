// fetches and lists the title for all movies by using this URL: https://swapi-api.hbtn.io/api/films/?format=json
// using JQuery API
$.get('https://swapi-api.hbtn.io/api/films/?format=json', function (data) {
  $.each(data.results, function (index, value) {
    $('#list_movies').append(value.title);
  });
});
