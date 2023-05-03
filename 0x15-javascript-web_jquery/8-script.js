$(function() {
  $.getJSON('https://swapi-api.alx-tools.com/api/films/?format=json', function(data, textStatus) {
    if (textStatus === 'success') {
      $.each(data.results, function(index, movie) {
        $('#list_movies').append($('<li></li>').text(movie.title));
      });
    }
  });
});
