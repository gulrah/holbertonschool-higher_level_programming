const addItem = document.getElementById('add_item');
addItem.addEventListener('click', function() {
  const li = document.createElement('li');
  li.textContent = 'Item';
  document.querySelector('.my_list').appendChild(li);
});
