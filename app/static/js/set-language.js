// A function that reads the selected language from the option menu
// and loops over the paragraphs to hide / show the matching language

function setLanguage(userLanguage) {

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

 let language = window.location.pathname.replace(/\/$/, '').split("/").pop()

 setLanguage(language)
    
});

// And any time the select element changes

document.addEventListener('DOMContentLoaded', function() {

  $("button").click(function() {

    let language = $(this).val();

    setLanguage(language)

  });
    
});

    

