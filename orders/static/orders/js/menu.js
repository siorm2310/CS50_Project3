var pizzas = JSON.parse(document.getElementById("pizzasJSON").textContent);
var subs = JSON.parse(document.getElementById("subsJSON").textContent);
var dishes = JSON.parse(
  document.getElementById("other_dishesJSON").textContent
);
var toppings = JSON.parse(document.getElementById("toppingsJSON").textContent);

function openItemMenu(itemId) {
  const template = `
  <div class="form-group">
  <h4>Please select your toppings:</h4>
  <br />
  <strong>x toppings remain</strong>
  <div class="form-check">
    <input type="checkbox" class="form-check-input" id="exampleCheck1" />
    <label class="form-check-label" for="exampleCheck1">Check me out</label>
  </div>
  <button type="submit" class="btn btn-primary">Add to order</button>
</div>
`;
  document.getElementById("item_form").innerHTML = template;
}

document.addEventListener("DOMContentLoaded", () => {
  document.querySelectorAll(".pizza").forEach((btn) => {
    btn.addEventListener("click", () => {
      const dataId = btn.getAttribute("data-id");
    });
  });

  document.querySelectorAll(".sub").forEach((btn) => {
    btn.addEventListener("click", () => {
      const dataId = btn.getAttribute("data-id");
      console.log(dataId);
    });
  });

  document.querySelectorAll(".dish").forEach((btn) => {
    btn.addEventListener("click", () => {
      const dataId = btn.getAttribute("data-id");
      console.log(dataId);
    });
  });
});
