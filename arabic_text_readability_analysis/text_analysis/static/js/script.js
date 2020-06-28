
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

/*
  $Start Tippy
*/

tippy('.character_count', {
   content: "Letters (just A-Z, not including numbers and punctuation).",
   placement: 'bottom',
});

tippy('.sentence_count', {
  content: "Sentences are assumed to end with periods, question marks, exclamation marks or line breaks.",
  placement: 'bottom',
});

tippy('.paragraph_count', {
   content: "Paragraphs are defined as ending with a line break.",
   placement: 'bottom',
});


tippy('.reading_time', {
  content: "The time it would take for the average person to read this text, at a rate of 225 words per minute.",
  placement: 'bottom',
});



tippy('.speaking_time', {
   content: "The time it would take for the average person to say this text aloud, at a rate of 125 words per minute.",
   placement: 'bottom',
});

tippy('.flesch_kincaid_grade_level', {
  content: "Originally created to analyze the readabiliity of technical material. Now used widely and \
  highly regarded for its reliability. Suitable for the grading of a wide range of writing and for all ages.",
  placement: 'bottom',
});

tippy('.gunning_fog_index', {
  content: "Suitable for a wide range of material and especially for business writing and publishing. Grading suitable for all ages.",
  placement: 'bottom',
});

tippy('.coleman_liau_index', {
  content: "A character-calculated formula suitable for a wide range of texts and for all ages, and especially useful within education.",
  placement: 'bottom',
});

tippy('.smog', {
  content: "Applicable to a range of texts and ages but has been proven particularly useful in healthcare literature.",
  placement: 'bottom',
});

tippy('.automated_readability_index', {
  content: "A character-calculated formula suitable for a wide range of texts and ages but proven especially useful in technical writing.",
  placement: 'bottom',
});

tippy('.FORCAST_grade_level', {
  content: "A vocabulary-calculated formula, especially useful for technical writing.",
  placement: 'bottom',
});

tippy('.powers_sumner_kearl_grade', {
  content: "Calculated with sentence length and syllables as variables, this formula is best used to calculate readability in elementary grade texts.",
  placement: 'bottom',
});

tippy('.Rix_readability', {
  content: "Rix is calculated with word length and sentence length as variables. It is an evolution from the Lix formula, and produces a grade level.",
  placement: 'bottom',
});

tippy('.flesch_reading_ease', {
  content: "This was originally created in education research but is now used for a variety of purposes, including by government bodies and policy writers. ",
  placement: 'bottom',
});

tippy('.spache_score', {
  content: "Spache is a readability test for English best for texts up to fourth-grade level. For grading texts aimed at older children for readability, the Dale-Chall test is more suitable.",
  placement: 'bottom',
});

tippy('.new_dale_chall_score', {
  content: "Based on a familiar word list, this analyzes how readable a text is for fourth grade and up. As well as being useful in elementary education, it also has important use in the accessibility of content.",
  placement: 'bottom',
});

tippy('.Lix_readability', {
  content: "Lix is calculated with word length and sentence length as variables. It was formulated to take into account the readability of non-English reading materials. ",
  placement: 'bottom',
});

tippy('.lensear_write', {
  content: "Useful for a range of texts but particularly for technical material. Sometimes incorrectly called \"Linsear Write\".",
  placement: 'bottom',
});

tippy('.s_g_30s', {
  content: "Long sentences can be difficult to keep track of and too many can be fatiguing for the user. Try to use mostly short sentences in your writing.",
  placement: 'bottom',
});

tippy('.s_g_20s', {
  content: "Long sentences can be difficult to keep track of and too many can be fatiguing for the user. Try to use mostly short sentences in your writing. ",
  placement: 'bottom',
});

tippy('.w_g_4s', {
  content: "Long words which contain a lot of syllables are hard to read and to say. Try to use short words where possible.",
  placement: 'bottom',
});

tippy('.w_g_12l', {
  content: "Long words which contain a lot of letters are hard to read and to say. Try to use short words where possible.",
  placement: 'bottom',
});

tippy('.passive_voice_count', {
  content: "Passive voice can make what you are writing less engaging to the reader, compared to the active voice. For example, instead of \"the door was closed by the man\", it might be better to say \"the man closed the door\".",
  placement: 'bottom',
});


/*
  End Tippy
*/
/*----------------------- $Start initialize_calculation_classes -----------------------------*/

function add_happy_emojis(i, readibilty_analysis){

     $(".home_page ." + readibilty_analysis[i] + " i").removeClass("fas fa-smile-wink");
    $(".home_page ." + readibilty_analysis[i] + " i").addClass("fas fa-smile-wink");
    $(".home_page ." + readibilty_analysis[i] + " svg").removeClass("fas fa-smile-wink");
    $(".home_page ." + readibilty_analysis[i] + " svg").addClass("fas fa-smile-wink");
}
function add_sad_emojis(i, readibilty_analysis){
    $(".home_page ." + readibilty_analysis[i] + " i").removeClass("far fa-frown");
    $(".home_page ." + readibilty_analysis[i] + " i").addClass("far fa-frown");
    $(".home_page ." + readibilty_analysis[i] + " svg").removeClass("far fa-frown");
    $(".home_page ." + readibilty_analysis[i] + " svg").addClass("far fa-frown");
}
function table_of_score(score, class_name){
  var result = "";
  if(class_name == "gunning_fog_index"){
      var gunning_score_table = {
      16:     "College senior",
      15:     "College junior",
      14:     "College sophomore",
      13:     "College freshman",
      12:     "High school senior",
      11:     "High school junior",
      10:     "High school sophomore",
      9:     "High school freshman",
      8:     "Eighth grade",
      7:     "Seventh grade",
    };
    result = gunning_score_table[score]
  }else if(class_name == "coleman_liau_index"){
        if(score > 1 && score <= 5) result = "Very easy to read. [1st grade - 5th grade]";
        else if (score > 5 && score <= 8)  result = "Ideal for average readers. [5th grade - 8th grade]";
        else  result = "Fairly difficult to read. [8th grade - 11th grade]";
  }else if(class_name == "automated_readability_index"){
    var automated_readability_table = {
      13:     "College student [18-24]",
      12:     "Twelfth Grade [17-18]",
      11:     "Eleventh Grade [16-17]",
      10:     "Tenth Grade Age [15-16]",
      9:     "Ninth Grade Age [14-15]",
      8:     "Eighth Grade Age [13-14]",
      7:     "Seventh Grade. Age [12-13]",
      6:     "Sixth Grade. Age 11-12",
      5:     "Fifth Grade. Age [10-11]",
      4:     "Fourth Grade. Age [9-10]",
      3:     "Third Grade Age [7-9]",
      2:     "First & Second Grade. Age [6-7]",
    };

    result = automated_readability_table[score];

  }else if(class_name == "flesch_reading_ease"){
    if(score >= 80 && score < 90) result = "Easy to read. Conversational English for consumers. [6th grade]";
    else if (score >= 70 && score < 80)  result = "Fairly easy to read. [7th grade]";
    else if(score >= 60 && score < 70)  result = "Easily understood by 13- to 15-year-old students. [8th & 9th grade]";
    else if(score >= 50 && score < 60)  result = "Fairly difficult to read. [10th to 12th grade]";
    else if(score >= 30 && score < 50)  result = "Difficult to read. [College Student]";
    else result = "Very difficult to read. Best understood by university graduates. College graduated";

  }else if(class_name == "new_dale_chall_score"){
    if(score >= 5 && score <= 5.9) result = "Fifth & Sixth Grade";
    else if (score >= 6 && score <= 6.9)  result = "Seventh & Eighth Grade";
    else if(score >= 7 && score <= 7.9)  result = "Ninth & Tenth Grade";
    else if(score >= 8 && score <= 8.9)  result = "Eleventh & Twelfth Grade";
    else result = "College Student";

  }else if(class_name == "Lix_readability"){
    if(score >= 25 && score < 43) result = "Easy To read";
    else if (score >= 43 && score < 45)  result = "Standard";
    else  result = "Difficult To Read";
  }

  return result
 
}

function initialize_calculation_classes(){
  /*
  Argument:
  No argument passed its just to initialize some variables
  Return:
  list of arrays
  */
  var text_composition = ["Adjectives", "Adverbs", "Conjuctions", "Determiners",
    "Interjections", "Nouns", "Proper_Nouns", "Prepositions", "Pronouns", "Verbs"],

    arabic_text_composition = ["Nouns", "DET+NOUN", "DET+ADJ", "PUNC",
    "Verbs", "Prepositions", "DET+ADJ+NSUFF", "NUM", "Conjuctions", "NUM+NSUFF",
    "ABBREV", "Adjectives", "Adverbs", "CASE",
    "Pronouns", "V+PRON", "Determiners", "PART", "ADJ+NSUFF", "ADJ+NSUFF"],

    statics_calculations = ["character_count", "syllable_count", "word_count", "unique_word_count",
     "sentence_count",  "paragraph_count", "reading_time", "speaking_time"],

     readability_gradeLevels = ["flesch_kincaid_grade_level", "gunning_fog_index", 
     "coleman_liau_index", "smog", "automated_readability_index", "flesch_reading_ease",
     "FORCAST_grade_level", "Rix_readability", "powers_sumner_kearl_grade", "spache_score",
     "new_dale_chall_score", "Lix_readability", "lensear_write"],

     readability_issues = [ "s_g_30s", "s_g_20s", "w_g_4s", "w_g_12l",
     "s_g_30s2", "s_g_20s2", "w_g_4s2", "w_g_12l2"],

     text_density_issues = ["passive_voice_count", "characters_per_word",
      "syllables_per_word", "words_per_sentence", "words_per_paragraph", "sentences_per_paragraph"],
      arabic_AARIs = ["arabic_ARI2", "arabic_AARI", "arabic_Al_Heeti"];
 
 return [text_composition, statics_calculations, readability_gradeLevels, readability_issues,
  text_density_issues, arabic_AARIs]
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
    $(".home_page ." + readibilty_analysis[i] + " .r_scor").empty();
    $(".home_page ." + readibilty_analysis[i] + " .non_percentage").empty();
    $(".home_page ." + readibilty_analysis[i] + " .m_meaning").empty();
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
        if(readibilty_analysis[i] == "s_g_30s"){

          var r_score = data[name_of_class][readibilty_analysis[i+4]];
          if(r_score >= 0 && r_score > 6) add_sad_emojis(i, readibilty_analysis);
          else add_happy_emojis(i, readibilty_analysis);
              
        }else if(readibilty_analysis[i] == "s_g_20s"){

          var r_score = data[name_of_class][readibilty_analysis[i+4]];
          if(r_score >= 0 && r_score > 12) add_sad_emojis(i, readibilty_analysis);
          else add_happy_emojis(i, readibilty_analysis);

        }else if(readibilty_analysis[i] == "w_g_4s" || readibilty_analysis[i] == "w_g_12l" || readibilty_analysis[i] == "passive_voice_count"){

          var r_score = data[name_of_class][readibilty_analysis[i+4]];
          if(r_score >= 0 && r_score > 3 ) add_sad_emojis(i, readibilty_analysis);
          else add_happy_emojis(i, readibilty_analysis);
        }

       $(".home_page ." + readibilty_analysis[i] + " .non_percentage").append(data[name_of_class][readibilty_analysis[i]]
       +"<span>" +data[name_of_class][readibilty_analysis[i+4]] + "%</span>");
      }
   }else{
       for(var i=0;i<readibilty_analysis.length;++i){
        var r_score = data[name_of_class][readibilty_analysis[i]];
        if(readibilty_analysis[i] == "characters_per_word"){
           if(r_score >= 0 && r_score < 4.2) add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(readibilty_analysis[i] == "syllables_per_word"){
           if(r_score >= 0 && r_score < 1.4) add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(readibilty_analysis[i] == "words_per_sentence"){
           if(r_score >= 0 && r_score < 14) add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(readibilty_analysis[i] == "words_per_paragraph"){
           if(r_score >= 10 && r_score <= 17) add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(readibilty_analysis[i] == "sentences_per_paragraph"){
           if(r_score >= 30 && r_score <= 65)  add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(readibilty_analysis[i] == "lensear_write"){
          if(r_score <= 45 && r_score > 0) add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(readibilty_analysis[i] == "Lix_readability"){
           if(r_score >= 0 && r_score < 55) add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(readibilty_analysis[i] == "flesch_reading_ease"){
          if(r_score <= 100 && r_score > 60) add_happy_emojis(i, readibilty_analysis);
          else add_sad_emojis(i, readibilty_analysis);
        }
        else if(r_score >= 0 && r_score <= 10)  {
          add_happy_emojis(i, readibilty_analysis);
          $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Readable by most people.");
        }
        else{
          add_sad_emojis(i, readibilty_analysis);
          $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Not readable enough.");
        } 
      
      $(".home_page ." + readibilty_analysis[i] + " .r_scor").append(data[name_of_class][readibilty_analysis[i]]);
  
            if(readibilty_analysis[i] == "gunning_fog_index"){
              // $(".home_page ." + readibilty_analysis[i] + " .m_meaning").empty();
            var r_score = data[name_of_class][readibilty_analysis[i]];

            if(r_score <= 6){
                $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required Sixth grade");
            }else if(r_score >= 17){
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required College graduate");
            }else{
              r_score =  Math.round(r_score);
              var m_meaning = table_of_score(r_score, "gunning_fog_index");
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required "+ m_meaning);
            }

        }
        if(readibilty_analysis[i]  == "coleman_liau_index"){
          var r_score = data[name_of_class][readibilty_analysis[i]];

            if(r_score <= 1){
                $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required Basic level of read books. [Pre-kindergarten - 1st grade]");
            }else if(r_score >= 11){
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Too hard to read for most readers. [11th grade - college]");
            }else{
              r_score =  Math.round(r_score);
              var m_meaning = table_of_score(r_score, "coleman_liau_index");
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required "+ m_meaning);
            }
        }

        if(readibilty_analysis[i]  == "automated_readability_index"){
          var r_score = data[name_of_class][readibilty_analysis[i]];

            if(r_score <= 1){
                $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required Kindergarten. Age [5-6]");
            }else if(r_score >= 14){
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required Professor. Age[24+]");
            }else{
              r_score =  Math.round(r_score);
              var m_meaning = table_of_score(r_score, "automated_readability_index");
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required "+ m_meaning);
            }
        }

        if(readibilty_analysis[i]  == "flesch_reading_ease"){
          var r_score = data[name_of_class][readibilty_analysis[i]];

            if(r_score >= 90){
                $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Easily understood by 11-year-old student. [5th grade]");
            }else if(r_score <= 10){
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Extremely difficult to read. Best understood by university graduates. [Professional]");
            }else{
              r_score =  Math.round(r_score);
              var m_meaning = table_of_score(r_score, "flesch_reading_ease");
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append(m_meaning);
            }
        }
        if(readibilty_analysis[i]  == "new_dale_chall_score"){
          var r_score = data[name_of_class][readibilty_analysis[i]];

            if(r_score < 5){
                $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required Fourth Grade or smaller.");
            }else if(r_score > 9.9){
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required College Graduate.");
            }else{
              r_score =  Math.round(r_score);
              var m_meaning = table_of_score(r_score, "new_dale_chall_score");
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Required " + m_meaning);
            }
        }

        if(readibilty_analysis[i]  == "Lix_readability"){
          var r_score = data[name_of_class][readibilty_analysis[i]];

            if(r_score < 25){
                $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Very Easy To Read");
            }else if(r_score > 55){
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Very Difficult To Read");
            }else{
              r_score =  Math.round(r_score);
              var m_meaning = table_of_score(r_score, "Lix_readability");
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append(m_meaning);
            }
        }
        if(readibilty_analysis[i]  == "lensear_write"){
          var r_score = data[name_of_class][readibilty_analysis[i]];

            if(r_score < 45){
                $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Readable by most people.");
            }else{
              $(".home_page ." + readibilty_analysis[i] + " .m_meaning").append("Not readable enough.");
            }
        }
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
  // $('#language_choice .option1').append('<img class="button"></div>');  
    text_gerator();
    $(".arabic_AARIs").hide();
    $('.home_page .user_input_form .submit_btns .generate_text').click(function(e){
        e.preventDefault();
        $('.home_page .user_input_form .error_input').removeClass('error_message');
        var csrfmiddlewaretoken     = $(".home_page .user_input_form").find('input[name="csrfmiddlewaretoken"]').val();
        initialize                  =   initialize_calculation_classes(),
        text_composition            = initialize[0],
        statics_calculations        = initialize[1],
        readability_gradeLevels     = initialize[2],
        readability_issues          = initialize[3],
        text_density_issues          = initialize[4],
        arabic_AARIs                  = initialize[5],
        language_selected               = document.querySelector('input[name="language_selected"]:checked').value;
        // console.log(language_selected);
        $('.home_page .user_input_form .error_input').empty();
        $(".api_result").empty();
        // $('.home_page  .m_meaning').empty();
        // $('.home_page  .m_meaning').empty();
        var generated_text = "";
         $.ajax({
            url: '', // ipdate at the same url
            method: 'POST',
            headers: {
                // Secure key for forms its common for django
                'X-CSRFToken': csrfmiddlewaretoken,
            },
            data: JSON.stringify({
              'generated_text': generated_text,
              'language_selected': language_selected,
            }),
            success: function (data) {
              $('.home_page .user_input_form textarea').val('').empty();
              
              if(data['language_selected'] == "English"){
                $(".arabic_AARIs").hide();
                empty_text_readibilty_analysis(text_composition);
                empty_text_readibilty_analysis(statics_calculations);
                empty_text_readibilty_analysis(readability_gradeLevels);
                empty_text_readibilty_analysis(readability_issues);
                empty_text_readibilty_analysis(text_density_issues);
                empty_text_readibilty_analysis(arabic_AARIs);
                $(".api_result").empty();
                $('.home_page .user_input_form textarea').val(data['generated_text']);

              }else if(data['language_selected'] == "Arabic"){
                $(".arabic_AARIs").show();
                 tippy('.reading_time', {
                    content: "The time it would take for the average person to read this text, at a rate of 110 words per minute.",
                    placement: 'bottom',
                  });
                $('.home_page .user_input_form textarea').css({
                  "text-align": "right",
                })
                $('.home_page .user_input_form textarea').val(data['generated_text']);
              }else if(data['language_selected'] == "Hindi"){
                $(".arabic_AARIs").hide();
                $('.home_page .user_input_form textarea').css({
                  "text-align": "left",
                })
                $('.home_page .user_input_form textarea').val(data['generated_text']);
              }
              

              // add_text_readibilty_analysis(data, text_composition, "text_composition");
              // add_text_readibilty_analysis(data, statics_calculations,  "statics_calculations");
              // add_text_readibilty_analysis(data, readability_gradeLevels, "readability_gradeLevels");
              // add_text_readibilty_analysis(data, readability_issues, "readability_issues");
              // add_text_readibilty_analysis(data, text_density_issues, "text_density_issues");
            }
        })

    });

    $('.home_page .user_input_form .submit_btns .submit_text').click(function(e){

        e.preventDefault(); // prevent default action of form submitted

        $('.home_page .user_input_form .error_input').empty();
        // The div we append text to if there are a text then remove it
        $(".home_page .user_input_form .user_input_result").empty();
        var user_text                   = $('.home_page .user_input_form textarea').val(),
          csrfmiddlewaretoken         = $(".home_page .user_input_form").find('input[name="csrfmiddlewaretoken"]').val(),
          initialize                  =   initialize_calculation_classes(),
          text_composition            = initialize[0],
          statics_calculations        = initialize[1],
          readability_gradeLevels     = initialize[2],
          readability_issues          = initialize[3],
          text_density_issues         = initialize[4],
          arabic_AARIs                  = initialize[5],
          language_selected               = document.querySelector('input[name="language_selected"]:checked').value;
          
          empty_text_readibilty_analysis(text_composition);
          empty_text_readibilty_analysis(statics_calculations);
          empty_text_readibilty_analysis(readability_gradeLevels);
          empty_text_readibilty_analysis(readability_issues);
          empty_text_readibilty_analysis(text_density_issues);
          empty_text_readibilty_analysis(arabic_AARIs);
          $(".api_result").empty();
        if($('.home_page .user_input_form textarea').val() == ''){
          $('.home_page .user_input_form .error_input').addClass('error_message');
          $('.home_page .user_input_form .error_input').append("Please Enter Text");
        }else{
          $('.home_page .user_input_form .error_input').removeClass('error_message');
          $.ajax({
              url: '', 
              method: 'POST',
              headers: {
                  'X-CSRFToken': csrfmiddlewaretoken,
              },
              data: JSON.stringify({
                'user_text': user_text,
                'language_selected': language_selected,
              }),
              success: function (data) {
                empty_text_readibilty_analysis(text_composition);
                empty_text_readibilty_analysis(statics_calculations);
                empty_text_readibilty_analysis(readability_gradeLevels);
                empty_text_readibilty_analysis(readability_issues);
                empty_text_readibilty_analysis(text_density_issues);
                empty_text_readibilty_analysis(arabic_AARIs);
                $(".api_result").empty();

                if(data['language_selected'] == "English"){
                $(".arabic_AARIs").hide();
                add_text_readibilty_analysis(data, text_composition, "text_composition");
                
                add_text_readibilty_analysis(data, statics_calculations,  "statics_calculations");
                add_text_readibilty_analysis(data, readability_gradeLevels, "readability_gradeLevels");
                add_text_readibilty_analysis(data, readability_issues, "readability_issues");
                add_text_readibilty_analysis(data, text_density_issues, "text_density_issues");

                }else if(data['language_selected'] == "Arabic"){
                  tippy('.reading_time', {
                    content: "The time it would take for the average person to read this text, at a rate of 110 words per minute.",
                    placement: 'bottom',
                  });
                  add_text_readibilty_analysis(data, statics_calculations,  "statics_calculations");
                  add_text_readibilty_analysis(data, text_density_issues, "text_density_issues");
                  add_text_readibilty_analysis(data, readability_gradeLevels, "readability_gradeLevels");
                  add_text_readibilty_analysis(data, readability_issues, "readability_issues");
                  add_text_readibilty_analysis(data, text_composition, "text_composition");
                  add_text_readibilty_analysis(data, arabic_AARIs, "arabic_AARIs");
                  $(".arabic_seg .api_result").append(data['arabic_seg']);
                  $(".arabic_lemma .api_result").append(data['arabic_lemma']);
                  $(".arabic_SpCH .api_result").append(data['arabic_SpCH']);
                  // $(".arabic_Diac .api_result").append(data['arabic_Diac']);
                  $(".arabic_Diac2 .api_result").append(data['arabic_Diac2']);
                  // alert("Arabic Language analysis will add soon");
                }else if(data['language_selected'] == "Hindi"){
                  $(".arabic_AARIs").hide();
                  add_text_readibilty_analysis(data, statics_calculations,  "statics_calculations");
                  add_text_readibilty_analysis(data, text_density_issues, "text_density_issues");
                  add_text_readibilty_analysis(data, readability_gradeLevels, "readability_gradeLevels");
                  add_text_readibilty_analysis(data, readability_issues, "readability_issues");
                  // add_text_readibilty_analysis(data, text_composition, "text_composition");

                }
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


    
  
// });
/*
##########################################
-----------------------         End submit Contact Us Form
*###########################################
*/
}); // End of document ready
