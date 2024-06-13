const card__container = document.getElementById("card__container");

fetch("http://127.0.0.1:8000/movie-api/list/")
  .then((resp) => resp.json())
  .then((data) => data.map((movie) => creat_movie_cards(movie)));

function creat_movie_cards(movie) {
  const card = `
  <div class="card">
        <img src="${movie.image_url}" alt="">
        <h3>${movie.movie_name}</h3>
        <p class="movie_content">${movie.content}</p>
        <p class="movie_detail" >${movie.release_year} | ${movie.director}</p>
 </div>
`;
  card__container.innerHTML += card;
}
