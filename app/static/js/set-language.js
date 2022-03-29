// A function that reads the selected language from the option menu
// and loops over the paragraphs to hide / show the matching language

function setLanguage(language) {

  let userLanguage = null

  if(language) {

    userLanguage = language

  } else {

    userLanguage = window.location.pathname.replace(/\/$/, '').split("/").pop()

  }

  let allTranslations = document.querySelectorAll('.en, .kh'); 
  
  for (var i = 0; i < allTranslations.length; i++) {
  
    let span = allTranslations[i]

    if (span.className === userLanguage) {
    
      span.style.display = 'block';
      
    } else {
     
      span.style.display = 'none';
         
    } 
      
  } 
  
}

// On page load run the setLanguage function

document.addEventListener('DOMContentLoaded', function() {

 setLanguage(null)
    
});

// And any time the select element changes

document.addEventListener('DOMContentLoaded', function() {

  $("button").click(function() {

    var language = $(this).val();

    setLanguage(language)

  });
    
});

    

