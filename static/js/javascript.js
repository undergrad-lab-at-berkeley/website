$(document).ready(function () {

  /*
  When a duration is provided, .hide() becomes an animation method.
The .hide() method animates the width, height, and opacity of the
matched elements simultaneously. When these properties reach 0,
the display style property is set to none to ensure that the element
no longer affects the layout of the page.
*/

    $('.tree li:has(ul)').addClass('parent_li').find(' > a').attr('title', 'Collapse this branch');
    $('.tree li.parent_li > a').on('click', function (e) {

      var children = $(this).parent('li.parent_li').find(' > ul > li');
      if (children.is(":visible")) {
        children.hide('fast');
        $(this).parent().find('.down-connector').hide('fast');

        console.log('down connector: ' + test.length);
        $(this).attr('title', 'Expand this branch').find(' > i').addClass('icon-plus-sign').removeClass('icon-minus-sign');
      }
      else {
            $(this).parent().find('.down-connector').show('fast');
            children.show('fast');
            $(this).attr('title', 'Collapse this branch').find(' > i').addClass('icon-minus-sign').removeClass('icon-plus-sign');
        }
        e.stopPropagation();
    });
})
var area = document.getElementByClass('tree');
panzoom(area)
