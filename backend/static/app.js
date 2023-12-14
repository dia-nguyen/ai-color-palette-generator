const form = document.querySelector("#form");

form.addEventListener("submit", function (e) {
  e.preventDefault();
  const query = form.elements.query.value;
  fetchColors(query);
});

/** Generates color box elements for each color in list
 * - colors: list of colors
 * - parentEl: parent div element
 */
function createColorBoxes(colors, parentEl) {
  parentEl.innerHTML = "";

  for (const color of colors) {
    const div = document.createElement("div");
    const p = document.createElement("p");

    div.addEventListener("click", function () {
      navigator.clipboard.writeText(color);
    });

    div.style.backgroundColor = color;
    p.innerHTML = color;

    div.appendChild(p);
    parentEl.appendChild(div);
  }
}

/**
 * Fetches colors from our color palette API
 * - query: user query from input
 */
function fetchColors(query) {
  fetch("/palette", {
    method: "POST",
    headers: {
      //data being sent as form data
      "Content-Type": "application/x-www-form-urlencoded",
    },
    body: new URLSearchParams({
      //form data
      query: query,
    }),
  })
    .then((response) => response.json())
    .then((data) => {
      const colors = data.colors;
      const container = document.querySelector(".container");
      createColorBoxes(colors, container);
    });
}
