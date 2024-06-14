const card__container = document.getElementById("card__container");
fetch("http://127.0.0.1:8000/blog-api/list/")
  .then((resp) => resp.json())
  .then((data) => data.map((blog) => creat__cards(blog)));

function creat__cards(blog) {
  const card = `<div class="card">
        <img src="${blog.image}" alt="">
        <h3>${blog.name}</h3>
        <p class="movie_content">${blog.content}</p>
        <p class="movie_detail" >${blog.created_date.slice(0, 9)} | ${blog.user}</p>
 </div>`;
  card__container.innerHTML += card;
}
