function disableSubmitButton(btn) {
  btn.disabled = true;
  btn.className = ' is-disabled';
}

document.addEventListener('DOMContentLoaded', function () {
  document.querySelectorAll('form')
    .forEach(form => form.addEventListener('submit', function (_) {
      form.querySelectorAll('button[type="submit"], input[type="submit"]')
        .forEach(disableSubmitButton);
    }));
});
