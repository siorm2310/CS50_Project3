function openItemMenu(itemId) {
  const template = ``;
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
