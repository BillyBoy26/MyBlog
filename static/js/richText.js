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
       var contentText = "<div class='mdl-cell mdl-cell--6-col mdl-card__supporting-text no-padding'><p>" + selectedText + "</p></div>"
       textarea.value = textarea.value.replace(selectedText, contentText);
   }
};
document.getElementById('rt-image').onclick = function () {
    var contentImage = "<div class='mdl-cell mdl-cell--6-col'>" +
        "<img class='article-image' src='' border='0' /> " +
        "</div>";
    textarea.value = textarea.value.substring(0, textarea.selectionStart) + contentImage + textarea.value.substring(textarea.selectionStart, textarea.value.length);
};