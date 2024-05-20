const updateHeader = document.getElementById('update_header');
updateHeader.addEventListener('click', function() {
  document.querySelector('header').textContent = 'New Header!!!';
});
