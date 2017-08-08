var textarea = document.getElementById('id_content');
var selectedText = "";


textarea.addEventListener('select', function() {
    selectedText =  window.getSelection().toString();
  }, false);


document.getElementById('rt-title').onclick = function () {
   if(selectedText.length > 0){
       var titledText = "<h3 class='mdl-cell mdl-cell--12-col mdl-typography--headline'>" + selectedText + "</h3>"
       textarea.value = textarea.value.replace(selectedText, titledText);
   }
};
document.getElementById('rt-content').onclick = function () {
   if(selectedText.length > 0){
       var contentText = "<div class='mdl-cell mdl-cell--6-col mdl-card__supporting-text no-padding'>" + selectedText + "</div>"
       textarea.value = textarea.value.replace(selectedText, contentText);
   }
};
document.getElementById('rt-image').onclick = function () {
   if(selectedText.length > 0){
       var titledText = "<h3>" + selectedText + "</h3>"
       textarea.value = textarea.value.replace(selectedText, titledText);
   }
};