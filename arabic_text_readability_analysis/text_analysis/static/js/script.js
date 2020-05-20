
/*
  before start to search about any page or section make $ like ------ $start home_page

  list of functions implemented and you can search about using $name like below:

  - $Start initialize_calculation_classes
  - $Start add_text_readibilty_analysis
  - $Start empty_text_readibilty_analysis
  - $Start text_gerator
*/


/* --------------------
------------------------ $Start home_page
-------------------- */



/*----------------------- $Start initialize_calculation_classes -----------------------------*/


function initialize_calculation_classes(){
  /*
  Argument:
  No argument passed its just to initialize some variables
  Return:
  list of arrays
  */
  var text_composition = ["Adjectives", "Adverbs", "Conjuctions", "Determiners",
    "Interjections", "Nouns", "Proper_Nouns", "Prepositions", "Pronouns", "Verbs"],
    
    statics_calculations = ["character_count", "syllable_count", "word_count", "unique_word_count",
     "sentence_count",  "paragraph_count"]

     readability_gradeLevels = ["flesch_kincaid_grade_level", "gunning_fog_index", 
     "coleman_liau_index", "smog", "automated_readability_index", "flesch_reading_ease",
     "powers_sumner_kearl_grade"];
 return [text_composition, statics_calculations, readability_gradeLevels]
}
/*----------------------- End initialize_calculation_classes -----------------------------*/

/*----------------------- $Start empty_text_readibilty_analysis &  add_text_readibilty_analysis -----------------------------*/


function empty_text_readibilty_analysis(readibilty_analysis){

/*
Argument:
param1 as list of arrays each of them cotain some strings that we used to empty html content
Return:
No return the function add html to home page

*/ 
  for(var i=0;i<readibilty_analysis.length;++i){
    $(".home_page ." + readibilty_analysis[i] + " span").empty();
  }
}

function add_text_readibilty_analysis(data, readibilty_analysis, name_of_class){
/*
Argument:
param1 dictionary of json that returned from views.py with analysis of the three function above
param2 as list of arrays each of them cotain some strings that we used to add html
param3 which class we point to in html and views 
Return:
No return the function add html to home page
*/
  for(var i=0;i<readibilty_analysis.length;++i){
    $(".home_page ." + readibilty_analysis[i] ).append("<span>" +data[name_of_class][readibilty_analysis[i]] + "</span>");
  }
}

/*----------------------- End empty_text_readibilty_analysis &  add_text_readibilty_analysis -----------------------------*/



/*----------------------- $Start text_gerator  -----------------------------*/

function text_gerator(){
/*
    a function used to add text in html with funny css style
*/
  var text_content = 'Readability scores are a way to measure whether a written text is \
  likely to be understood by the intended reader. Text that scores a readability \
  grade level of 8 or below will be readable by around 85% of the general public. \
  And you can test your text Readability below !'
  sentence = "",
  char_index = 0,
  interval = setInterval(append_text, 90),
  color_index= 0;

  function append_text(){
/*
  The function used to append some style for generated character 
  in text_generator function - setInterval function
  Argument:
  No Argument
  Return:
  No Return
*/
    sentence += text_content[char_index];
    $('.home_page .content .text_content').text(sentence).css("color", "white");
    char_index++;
    color_index++;
    if(color_index == 2) color_index = 0;
    if (char_index == text_content.length) {
      clearInterval(interval);
    }
  }
}

/*----------------------- End text_gerator  -----------------------------*/

$(document).ready(function(){

    text_gerator();

    $('.home_page .user_input_form .submit_btns .generate_text').click(function(e){
        e.preventDefault();
        $('.home_page .user_input_form .error_input').removeClass('error_message');
        var csrfmiddlewaretoken   = $(".home_page .user_input_form").find('input[name="csrfmiddlewaretoken"]').val();
        initialize                  =   initialize_calculation_classes(),
        text_composition            = initialize[0],
        statics_calculations        = initialize[1],
        readability_gradeLevels     = initialize[2];

        $('.home_page .user_input_form .error_input').empty();
        // alert(csrfmiddlewaretoken);
        var generated_text = "";
         $.ajax({
            url: '', // ipdate at the same url
            method: 'POST',
            headers: {
                // Secure key for forms its common for django
                'X-CSRFToken': csrfmiddlewaretoken,
            },
            data: JSON.stringify({'generated_text': generated_text}),
            success: function (data) {
              $('.home_page .user_input_form textarea').val('').empty();
              $('.home_page .user_input_form textarea').val(data['generated_text']);
              
              empty_text_readibilty_analysis(text_composition);
              empty_text_readibilty_analysis(statics_calculations);
              empty_text_readibilty_analysis(readability_gradeLevels);

              add_text_readibilty_analysis(data, text_composition, "text_composition");
              add_text_readibilty_analysis(data, statics_calculations,  "statics_calculations");
              add_text_readibilty_analysis(data, readability_gradeLevels, "readability_gradeLevels");

            }
        })

    });

    $('.home_page .user_input_form .submit_btns .submit_text').click(function(e){

        e.preventDefault(); // prevent default action of form submitted
        $('.home_page .user_input_form .error_input').empty();
        // The div we append text to if there are a text then remove it
        $(".home_page .user_input_form .user_input_result").empty();
       
        if($('.home_page .user_input_form textarea').val() == ''){
          $('.home_page .user_input_form .error_input').addClass('error_message');
         $('.home_page .user_input_form .error_input').append("Please Enter Text");

            empty_text_readibilty_analysis(text_composition);
            empty_text_readibilty_analysis(statics_calculations);
            empty_text_readibilty_analysis(readability_gradeLevels);

        }else{
        $('.home_page .user_input_form .error_input').removeClass('error_message');

        user_text                   = $('.home_page .user_input_form textarea').val(),
        csrfmiddlewaretoken         = $(".home_page .user_input_form").find('input[name="csrfmiddlewaretoken"]').val(),
        initialize                  =   initialize_calculation_classes(),
        text_composition            = initialize[0],
        statics_calculations        = initialize[1],
        readability_gradeLevels     = initialize[2];

        empty_text_readibilty_analysis(text_composition);
        empty_text_readibilty_analysis(statics_calculations);
        empty_text_readibilty_analysis(readability_gradeLevels);

        $.ajax({
            url: '', 
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfmiddlewaretoken,
            },
            data: JSON.stringify({'user_text': user_text}),
            success: function (data) {
              add_text_readibilty_analysis(data, text_composition, "text_composition");
              add_text_readibilty_analysis(data, statics_calculations,  "statics_calculations");
              add_text_readibilty_analysis(data, readability_gradeLevels, "readability_gradeLevels");
            }
        })
      }
  })

}); 


/*----------------------- End home_page user_input_anaysis Section -----------------------------*/


/* --------------------
------------------------ $End home_page
-------------------- */