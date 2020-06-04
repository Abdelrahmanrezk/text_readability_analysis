
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
     "sentence_count",  "paragraph_count"],

     readability_gradeLevels = ["flesch_kincaid_grade_level", "gunning_fog_index", 
     "coleman_liau_index", "smog", "automated_readability_index", "flesch_reading_ease",
     "FORCAST_grade_level", "Rix_readability", "powers_sumner_kearl_grade", "spache_score",
     "new_dale_chall_score", "Lix_readability", "lensear_write"],

     readability_issues = [ "s_g_30s", "s_g_20s", "w_g_4s", "w_g_12l",
     "s_g_30s2", "s_g_20s2", "w_g_4s2", "w_g_12l2"],

     text_density_issues = ["passive_voice_count", "characters_per_word",
      "syllables_per_word", "words_per_sentence", "words_per_paragraph", "sentences_per_paragraph"];
 
 return [text_composition, statics_calculations, readability_gradeLevels, readability_issues,
  text_density_issues]
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
    if(name_of_class == "readability_issues"){
   
      for(var i=0;i<readibilty_analysis.length;++i){
     $(".home_page ." + readibilty_analysis[i] ).append("<span class=\"non_percentage\">" +data[name_of_class][readibilty_analysis[i]] + "</span>"
     +"<span>" +data[name_of_class][readibilty_analysis[i+4]] + "%</span>");

  }
   }else{
       for(var i=0;i<readibilty_analysis.length;++i){
      $(".home_page ." + readibilty_analysis[i] ).append("<span>" +data[name_of_class][readibilty_analysis[i]] + "</span>");
  }
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
        var csrfmiddlewaretoken     = $(".home_page .user_input_form").find('input[name="csrfmiddlewaretoken"]').val();
        initialize                  =   initialize_calculation_classes(),
        text_composition            = initialize[0],
        statics_calculations        = initialize[1],
        readability_gradeLevels     = initialize[2],
        readability_issues          = initialize[3],
        text_density_issues          = initialize[4];
        $('.home_page .user_input_form .error_input').empty();

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
              empty_text_readibilty_analysis(readability_issues);
              empty_text_readibilty_analysis(text_density_issues);

              add_text_readibilty_analysis(data, text_composition, "text_composition");
              add_text_readibilty_analysis(data, statics_calculations,  "statics_calculations");
              add_text_readibilty_analysis(data, readability_gradeLevels, "readability_gradeLevels");
              add_text_readibilty_analysis(data, readability_issues, "readability_issues");
              add_text_readibilty_analysis(data, text_density_issues, "text_density_issues");
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
          empty_text_readibilty_analysis(readability_issues);
          empty_text_readibilty_analysis(text_density_issues);
        }else{
          $('.home_page .user_input_form .error_input').removeClass('error_message');

          user_text                   = $('.home_page .user_input_form textarea').val(),
          csrfmiddlewaretoken         = $(".home_page .user_input_form").find('input[name="csrfmiddlewaretoken"]').val(),
          initialize                  =   initialize_calculation_classes(),
          text_composition            = initialize[0],
          statics_calculations        = initialize[1],
          readability_gradeLevels     = initialize[2],
          readability_issues          = initialize[3],
          text_density_issues          = initialize[4];

          empty_text_readibilty_analysis(text_composition);
          empty_text_readibilty_analysis(statics_calculations);
          empty_text_readibilty_analysis(readability_gradeLevels);
          empty_text_readibilty_analysis(readability_issues);
          empty_text_readibilty_analysis(text_density_issues);

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
              add_text_readibilty_analysis(data, readability_issues, "readability_issues");
              add_text_readibilty_analysis(data, text_density_issues, "text_density_issues");
            }
        })
      }
  })

}); 
/*----------------------- End home_page user_input_anaysis Section -----------------------------*/


/* --------------------
------------------------ $End home_page
-------------------- */

$(document).ready(function(){


/*
##########################################
-----------------------         Start navbar animation
*########################################### 
*/

  var clicked = 0; // clieck button related to navbar button
  $('.nav-bar #nav-icon').click(function(){
    // Get window sizes and some divs to make it responsive with all window

    var inner_width = $( window ).innerWidth(),
        inner_height = $( window ).innerHeight(),
        nav_content_width = $(".nav-bar .nav_content").innerWidth(),
        nav_content_height = $(".nav-bar .nav_content").innerHeight(),
        $this =  $(this);

        if(!clicked){
          clicked = 1;
      
          /*
            Check if navbar is opened then we need to close it and reset some css
          */
          if($(".nav-bar .right").hasClass("right_navigate")){

            $(".nav-bar .right.right_navigate").css({'width': 0 });
            $(".nav-bar .left.left_navigate").css({'width': 0 });
            $(".nav-bar .right").removeClass("right_navigate");
            $(".nav-bar .left").removeClass("left_navigate");
            $("body").removeClass("scrolling_behavior");
            $this.removeClass('open');
            $(".nav-bar .nav_content").removeClass("show");
            $(".nav-bar .nav_content").css({
              'top' : (inner_height/2) - (nav_content_height/2) + $(window).scrollTop(),
              'right' : '-100%',
            });

          }else{ // End if of has class
              $this.addClass('open');
              $("body").addClass("scrolling_behavior")
              $(".nav-bar .right").addClass("right_navigate");
              $(".nav-bar .left").addClass("left_navigate");
              $(".nav-bar .right.right_navigate").css({
                'width': inner_width/2+7,
                'height': inner_height,
              });
              $(".nav-bar .left.left_navigate").css({
                'width': inner_width/2+7,
                'height': inner_height,
                'right': 0
              });

            // wait for links of navbar after animated lef and right divs
            setTimeout(function(){
              $(".nav-bar .nav_content").addClass("show");   
              $(".nav-bar .nav_content.show").css({
                'right': (inner_width/2) - (nav_content_width/2),
                'top' : ((inner_height/2) - (nav_content_height/2)) + $(window).scrollTop(),
              });
            }, 600);
            
          } // End of else 

            // Wait 1400 ms for next click because of let animation take its time 
          setTimeout(function(){ 
            clicked = 0;
          },1400);

    } // End of click boolean variable

  }); // End click on navbar button
/*
##########################################
-----------------------         End navbar animation
*########################################### 
*/

/*
##########################################
-----------------------         Start submit Contact Us Form
*########################################### 
*/

  $(".contact_us_page .contact_us_form .submit_contact").click(function (e){
    // prevent form from submit as default action
    e.preventDefault();

    // Get Form Data
     var message    = $('.contact_us_page .contact_us_form').find('textarea[name="message"]').val(),
        phonenumber    = $('.contact_us_page .contact_us_form').find('input[name="phonenumber"]').val(),
        mail    = $('.contact_us_page .contact_us_form').find('input[name="mail"]').val(),
        first_name    = $('.contact_us_page .contact_us_form').find('input[name="first_name"]').val(),
        csrfmiddlewaretoken   = $(".contact_us_page .contact_us_form").find('input[name="csrfmiddlewaretoken"]').val();
        
        $(".contact_us_page .submit_contact_error").hide();

        // Validation
        if(!message || !phonenumber || !first_name){
          $(this).before("<p class=\"submit_contact_error\">Please complete form data</p>");
        }else{

            var email_regex = /^[a-zA-Z0-9._-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,4}$/i,
                phonenumber_regex = /[0-9]{11}/;

            if(!email_regex.test(mail) && mail){

              $(this).before("<p class=\"submit_contact_error\">this is not valid email</p>");

            }else if(!phonenumber_regex.test(phonenumber) && phonenumber){

              $(this).before("<p class=\"submit_contact_error\">This is not valid phone number</p>");
            
            }else{
              $.ajax({
                url: '', 
                method: 'POST',
                headers: {
                    'X-CSRFToken': csrfmiddlewaretoken,
                },
                data: JSON.stringify({
                    'message': message,
                    'phonenumber': phonenumber,
                    'mail': mail,
                    'first_name': first_name,
                    }),
                success: function (data) {
                   window.location.href = "https://text-readability.herokuapp.com";
                }
              }) // End of Ajax

            } // End nested else condition
        }// End condition
    }) // End of click submit form button

/*
##########################################
-----------------------         End submit Contact Us Form
*###########################################
*/
}); // End of document ready

