// adds, removes and clears LI elements from a list when the user clicks on different divs
// using JQuery API
document.addEventListener('DOMContentLoaded', function () {
  $('#add_item').click(function () {
    $('UL.my_list').append('<li>Item</li>');
  });
  $('#remove_item').click(function () {
    $('li').last().remove();
  });
  $('#clear_list').click(function () {
    $('UL.my_list').empty();
  });
});
