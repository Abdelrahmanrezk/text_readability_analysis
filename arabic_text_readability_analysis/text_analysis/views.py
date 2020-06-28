from django.shortcuts import render
from django.http import JsonResponse,HttpResponse
import json
import sys
import os
import pandas as pd
import random
import numpy as np
from .models import Contact_us
import secrets


from text_analysis.text_statics_analysis.text_composition import *
from text_analysis.text_statics_analysis.ReadabilityGradeLevels import *
from text_analysis.text_statics_analysis.arabic_text_readibilty import *
from text_analysis.text_statics_analysis.hindi_text_readibilty import *



EnglishSamples10 = [
"""
-Elementary                
Going through the forest is my favourite part of the walk. 
My dog Benji loves it too. I’m Grace. I live on a farm with my parents and I take Benji for a walk most days after school. While Benji’s playing, I stop to take a photo of a butterfly. I’m thinking about posting it on Facebook, but then I hear Benji barking. He’s jumping and running around a boy. The poor boy looks worried. 'Benji, stop! Come here!'
I call and throw him his ball. I’m about to say sorry to the boy, but he’s gone.
""",

"""
-Elementary           
For hundreds of years, people thought dreams were messages from gods or spirits. 
Today, too, many people can remember a time when they saw a place or person in their dream and then, later, the dream happened in real life. Maybe that’s not surprising because we dream a lot but we probably only remember the times when something happens in a dream and then happens for real. Most people have four to six dreams every night after the age of ten. That’s as many as 2,000 dreams per year. So, an 80-year-old person has probably had 140,000 dreams. Maybe 
we forget 95–99 per cent of our dreams, but that’s still thousands of dreams that might ‘come true’.
""",

"""
-Intermediate            
Wild animals usually come into cities to look for food. 
In Cape Town, South Africa, baboons sometimes come into the suburbs. 
They eat fruit from gardens and go into people's kitchens and take food from cupboards and fridges! Baboons are strong animals and sometimes they scare children and fight with pet dogs. 
Many people do not like them, but the city can be dangerous for baboons too. 
Sometimes, baboons are hurt in car accidents and the sugar in human food can be very bad for their teeth. The city council in Cape Town has a team of Baboon Monitors. Their job is to find baboons in the city and take them back to the countryside. This makes the city safer for people and it is healthier for the baboons. The problem is that a lot of baboons will come back to the city to find food again.
""",

"""
-Intermediate               
We usually know if something is enjoyable, but to know what brings meaning and value requires more thought. 
For example, most people will say that air pilots have jobs with clear purpose. They are responsible for hundreds of people and fly all over the world. But they often have to spend time in boring hotels or stuck in airports and they perform routine actions hundreds of times. 
Those activities might not feel like they have meaning – and they’re probably not fun either. Just like everyone else, pilots need balance in their work and life to be happy.
""",

"""
-Upper Intermediate    
Have you ever dreamt of climbing Mount Everest or walking to the South Pole? If so, you’re not alone. 
Every year, thousands of people try to climb the world’s highest mountains or walk across continents. 
Unlike the explorers of the past who used maps and compasses, today’s adventurers travel with modern technology like GPS and satellite phones. Many adventurers are nature lovers who use their travels to help raise awareness about a range of environmental issues, while others are keen to help people in need and raise money for charities. Let’s take a look at some of the 21st century’s greatest adventurers.
""",

"""
-Upper Intermediate    
When Pi is 16, his family decide to close the zoo and move to Canada. 
They sell some of the animals to zoos in North America and the family take the animals with them on a ship to Canada. On the way, there is a terrible storm and the ship sinks. Pi finds himself in a lifeboat with a hyena, zebra, orang-utan and a tiger. When he sees the animals, Pi is scared and he jumps into the ocean. Then he remembers there are sharks in the ocean and he climbs back into the lifeboat. Sadly, Pi’s family and the ship’s sailors die in the storm. One by one, the animals in the lifeboat kill and eat each other, till only Pi and the tiger are left alive. Luckily for Pi, there is some food and water on the lifeboat, but he soon needs to start catching fish. He feeds the fish to the tiger to stop it killing and eating him. 
He also uses a whistle and his knowledge of animals from the zoo to control the tiger.
""",

"""
-Beginner A1            
Beautiful two-bedroom city flat five minutes' walk from the cathedral. 
Fully equipped kitchen, living room with a large sofa and chairs, big TV and balcony. 
The balcony has space for four people to sit and gets the sun in the mornings, and the flat is light and warm. It has Wi-Fi and fast internet. The upstairs bedroom sleeps four people, with two double beds; the downstairs bedroom sleeps two in single beds. 
The flat is perfect for families and is near shops, bars and restaurants.
""",

"""
-Pre-intermediate A2    
I am an architect with 20 years' experience of designing and developing spaces. 
I am a partner in the award-winning STG Architects Ltd, which is famous for its work on the Galroy Building in London. I enjoy working with people from all over the world and have international experience of working in Italy, Greece, Thailand, Australia and Brazil. I have a Master of Science from Sheffield University and a BA in Architecture from Hull University. 
I also speak Italian and Thai. When I am not working, I spend my time hiking, skiing and diving.  
""",

"""
-Intermediate B1          
Bangkok's traffic can be a nightmare. Sure, you can easily take a taxi – if you want to spend hours 
stuck in traffic jams – but there are two much better ways to get around the city. 
To explore the temples and historical sites, catch an express boat river taxi or a longtail boat along the Chao Phraya river and the canals. For the modern part of the city, the Skytrain is a fast, cheap way to travel from the river to the shopping malls and nightlife of Sukhumvit, and the famous Chatuchak street market.
""",

"""
-Upper intermediate B2
I went from London to Prague to set up a new regional office there. 
You know I'd always wanted to go, but maybe I was imagining Prague in spring when I used to talk about that. 
Winter was really hard, with minus 15 degrees in the mornings and dark really early in the evening. But at least it was blue skies and white snow and not days on end of grey skies and rain, like at home. It's tough being away from home over Christmas, though, and Skype on Christmas Day wasn't really the same as being with everyone.
""",

"""
-Advanced C1           
Unfortunately, these conditions are also perfect for the spread of the fungus Fusarium oxysporum f. sp. cubense, 
which attacks the plant’s roots and prevents it from transporting water to the stem and leaves. 
The TR-1 strain of the fungus was resistant to crop sprays and travelled around on boots or the tyres of trucks, slowly infecting plantations across the region. In an attempt to escape the fungus, farmers abandoned infected fields, flooded them and then replanted crops somewhere else, often cutting down rainforest to do so.
""",



]


HindiSamples12 = [
"""
अम्मा आज लगा दे झूला, इस झूले पर मैं झूलूंगा। उस पर चढ़कर, ऊपर बढ़कर, आसमान को मैं छू लूंगा। झूला झूल रही है डाली, झूल रहा है पत्ता-पत्ता। इस झूले पर बड़ा मज़ा है, चल दिल्ली, ले चल कलकत्ता।
""",

"""
एक लड़की ने आम के एक पेड़ पर लटका हुआ एक पका आम देखा। उसके मुँह में पानी भर आया। सामने के पेड़ पर बैठा एक कौआ भी ललचाई नजरों से इस आम को देख रहा था। लड़की ने अपने भाई को बुलाया और गुलेल से उस पके हुए आम को पेड़ से तोड़ने के लिए कहा। 
""",

"""
 किसी तालाब में एक कछुआ रहता था। तालाब के पास माँद में रहने वाली एक लोमड़ी से उसकी दोस्ती हो गई। एक दिन वे तालाब के किनारे गपशप कर रहे थे कि एक तेंदुआ वहाँ आया। दोनों अपने-अपने घर की ओर जान बचाकर भागे। लोमड़ी तो सरपट दोड़कर अपनी माँद में पहुँच गई पर कछुआ अपनी धीमी चाल के कारण तालाब तक नहीं पहुँच सका। तेंदुआ एक छलाँग में उस तक पहुँच गया।  
""",

"""
 किसी जंगल में एक छोटा बाघ खेल रहा था। खेलते-खेलते वह जंगल के पास वाली सड़क पर निकल आया। सड़क पर एक बस खड़ी थी। छोटे बाघ ने देखा कि बस का दरवाज़ा खुला है। बाघ अपने अगले पंजे बस की सीढ़ी पर रखकर बस के भीतर देखने लगा।   
""",

"""
मीरा बहन का जन्म इंग्लैंड में हुआ था। गांधी जी के विचारों का उन पर इतना असर हुआ कि वे अपना घर और अपने माता-पिता को छोड़कर भारत आ गईं और गांधी जी के साथ काम करने लगीं।  
""",

"""
आज्ञादी के पाँच साल बाद उन्होंने उत्तर प्रदेश के एक पहाड़ी गाँव, गेंवली में गोपाल आश्रम की स्थापना की। उस आश्रम में मीरा बहन का बहुत सारा समय पालतू पशुओं की देखभाल में बीतता था लेकिन गेंवली गाँव के आसपास के जंगलों में बाघ जेसे खतरनाक जानवर भी रहते थे। 
""",

"""
बादशाह अकबर अपने मंत्री बीरबल को बहुत पसंद करता था। बीरबल की बुद्धि के आगेबड़े-बड़ों की भी कुछ नहीं चल पाती थी। इसीकारण कुछ दरबारी बीरबल से जलते थे। वे बीरबल को मुसीबत में फँसाने के तरीके सोचते रहते थे।
""",

"""
 एक दिन ख्वाजा ने बीरबल को मूर्ख साबित करने के लिए बहुत सोच-विचार कर कुछ मुश्किल प्रश्न सोच लिए। उन्हें विश्वास था कि बादशाह के उन प्रश्नों को सुनकर बीरबल के छक्‍के छूट हे जाएँगे और वह लाख कोशिश करके भी संतोषजनक उत्तर नहीं दे पाएगा। फिर बादशाह मान लेगा कि ख्वाजा सरा के आगे बीरबल कुछ नहीं हे।  
""",

"""
लोनपो गार तिब्बत के बत्तीसवें राजा सौनगवसेन गांपो के मंत्री थे। वे अपनी चालाकी और हाज़िरजवाबी के लिए दूर-दूर तक मशहूर थे। कोई उनके सामने टिकता न था। चेन से ज़िंदगी चल रही थी। मगर जब से उनका बेटा बड़ा हुआ था उनके लिए चिता का विषय बना हआ था। कारण यह था कि वह बहत भोला था। होशियारी उसे छकर भी नहीं गई थी।  
""",

"""
दोनों के दिल में तरह-तरह के सवाल उठते। अंडे कितने बड़े होंगे? किस रंग के होंगे? कितने होंगे? क्‍या खाते होंगे? उनमें से बच्चे किस तरह निकल आएँगे? बच्चों के पर केसे निकलेंगे? घोंसला कैसा है? लेकिन इन बातों का जवाब देने वाला कोई नहीं। न अम्मा को घर के काम-दधंधों से फ़ुरसत थी न बाबू जी को पढ़ने-लिखने से। दोनों बच्चे आपस ही में सवाल-जवाब करके अपने दिल को तसल्ली दे लिया करते थे।
""",

"""
क्या यह संभव है कि भला कोई जंगल में घंटा भर घूमे और फिर भी कोई विशेष चीज़ न देखे? मुझे जिसे कुछ भी दिखाई नहीं देता, को भी सैकड़ों रोचक चीज़ें मिल जाती हैं, जिन्हें में छूकर पहचान लेती हूँ। में भोज-पत्र के पेड़ की चिकनी छाल ओर चीड़ की खुरदरी छाल को स्पर्श से पहचान लेती हूँ। वसंत के दौरान मैं टहनियों में नयी कलियाँ खोजती हूँ।
""",

"""
आश्रम में गांधी कई ऐसे काम भी करते थे जिन्हें आमतोर पर नोकर-चाकर करते हैं। जिस ज़माने में वे बेरिस्टरी से हज़ारों रुपये कमाते थे, उस समय भी वे प्रतिदिन सुबह अपने हाथ से चक्की पर आटा पीसा करते थे। चक्की चलाने में कस्तूरबा ओर उनके लड़के भी हाथ बँटाते थे। इस प्रकार घर में रोटी बनाने के लिए महीन या मोटा आटा वे खुद पीस लेते थे।
""",


]


QatarSamplesGrades = [
"""
-Grad 1
هَلْ ذَهَبْتَ إِلَى حَدِيقَةِ الْحَيَوَانِ؟ نَعَمْ، ذَهَبْتُ إَلَى حَدِيقَةِ الْحَيَوَانِ. لَا، لَمْ أَذْهَبْ إِلَى حَدِيقَةِ الْحَيَوَانِ.
مَنْ قَدَّمَ إِلَيْكَ الْهَدِيَّةَ؟ أَحْمَدُ صَدِيقِي هُوَ الَّذِي قَدَّمَ إِلَى الْهَدِيَّةَ.
 مَا أَحَبُّ الْمَوَادِّ الدِّرَاسِيَّةِ إِلَيْكَ ؟ اللُّغَةُ الْعَرَبِيَّةُ أَحَبُّ الْمَوَادِّ إِلَيَّ.
مَتَى تَذْهَبُ إِلَى الشَّاطِئ؟ أَذْهَبُ إِلَى الشَّاطِئ فِي فَصْلِ الصَّيفِ.
أَيْنَ يُقَامُ الْحَفْلُ؟ يُقَامُ الْحَفْلُ فِي مَسْرَحِ الْمَدْرَسَةِ.
""",

"""
-Grad 2
شَجَرَةُ السِّدْرِ
تَنْتَشِرُ شَجَرَةُ السِّدْرِ بِشَكْلٍ وَاسِعٍ فِي الْمَنَاطِقِ الدَّافِئَةِ ، مِثْلَ شِبْةِ الْجَزِيْرَةِ الْعَرَبِيَّةِ ، وَهِي رَمْزٌ لِلخَيْرِ وَالْعَطَاءِ .
وَصْفُهَا : تَمْتَدُّ جُذُورُ شَجَرَةِ السِّدْرِ لِمَسَافَاتٍ طَوِيْلَةٍ فِي التُّرْبَةِ ، وَلَهَا أَورَاقٌ كَثِيفَةٌ بَيْضَاوِيَّةُ الشَّكْلِ ، وَتُغَطِّيْهَا طَبَقَةٌ سَمِيْكَةٌ ، أَمَّا ثِمَارُهَا فَهِيَ بُرْتُقَالِيَّةُ اللَّونِ، طَعْمُهَا حُلْوٌ ، وَرَاِئحَتُهَا عَطِرَةٌ .
فَوَائِدُهَا : تُسَاعِدُ ثِمَارُ شَجَرَةِ السِّدْرِ وَأَورَاقُهَا فِي عِلاَجِ كَثْيِرٍ مِنَ اْلأَمْرَاضِ؛ فَهِيَ تُنَقِّي الدَّمَ وَتُفِيْدُ فِي عِلاَجِ أَمْرَاضِ الْجِهَازِ التَّنَفُّسِيِّ.
وَقَدْ اهْتَمَّتْ دَوْلَةُ قَطَرَ اهْتِمَاماً كَبِيراً بِزِرَاعَةِ هَذِهِ الشَّجَرَةِ ، لِمَا لَهَا مِنْ فَوَائِدَ عَدِيدَةٍ وَلِقُدْرَتِهَا عَلَى تَحَمُّلِ ظُرُوفِ الْبِيَئةِ الْخَلِيجِيَّةِ.

""",

"""
-Grad 3
مُخْتَرِعُ الْمِصْبَاحِ الْكَهْرَبَائِيِّ.
وُلِدَ (تُومَاس أَدِيسُون) فِي مَدِينَةِ (ميلان) الْأَمْرِيكِيَّةِ، سَنَةَ أَلْفٍ وَثَمَانِمِئَةٍ وَسَبْعٍ وَأَرْبَعِينَ (1847م) . كَانَ شَغُوفاً بِالْبَحْثِ وَالْاكْتِشَافِ ، فَاهْتَمَّتْ أُمُّه بِتَعْلِيمِهِ الْقِرَاءَةَ وَالْكِتَابَةَ، وَخَصَّصَتْ لَهُ غُرْفَةً فِي الْمَنْزِلِ ليُجْرِيَ فِيهَا تَجَارِبَهُ.
اضْطُرَّ (أَديسُون) أَنْ يَبِيعَ الصُّحُفَ وَالْمَجَلَّاتِ وَالْكُتُبَ، بِسَبَبِ فَقْرِ أُسْرَتِهِ، وَعِنْدَمَا رَأَي شَغَفَ النَّاس بِالصُّحُفِ وَالْمَجَلَّاتِ اشْتَرَى آلَةَ طِبَاعَةٍ صَغِيرَةً ، وَبَدَأَ بِطِبَاعَةِ مَجَلَّةٍ مِنْ تَأْلِيفِهِ ، سَمَّاهَا "الرَّائِدَ الْأُسْبُوعِيَّ" فَأَصْبَحَ أَصْغَرَ صَاحِبِ صَحِيفَةٍ فِي الْعَالَمِ.
تَعَرَّضَ (أَديسُون) لِحَادِثٍ أَفْقَدَهُ الْقُدْرَةَ عَلَى السَّمْعِ ، فَلَمْ يَتَكَاسَلْ وقَامَ بِاخْتِرَاعِ آلَةِ (تِلِغْرَافٍ) كِتَابِيَّةٍ، وَفِي يَوْمِ الْوَاحِدِ وَالْعِشْرِينَ مِنْ أُكْتُوبَر سَنَةَ أَلْفٍ وَثَمَانِمِئَةٍ وَتِسْعٍ وَسَبْعِينَ (1879م) اسْتَطَاعَ (أَدِيسُون) أَنْ يُنِيرَ الْعَالَمَ بِاخْتِرَاعِهِ الْمِصْبَاحَ الْكَهْرَبَائِيَّ.
وَقَدْ تُوُفِّيِ الْمُخْتَرِعُ الْعَبْقَرِيُّ فِي سَنَةِ أَلْفٍ وَتِسْعِمِئَةٍ وَوَاحِدٍ وَثَلاثِينَ (1931م) بَعْدَ أَنْ سَجَّلَ أَلْفَيْنِ وخَمْسَمِئَةِ اخْتِرَاعٍ، أَفَادَ بِهَا الْبَشَرِيَّةَ كُلَّهَا.
""",

"""
-Grad 4
أَسْمَاءُ بِنْتُ أَبِي بَكْرٍ (رضي الله عنها)
عَاشَتْ حَيَاةً كُلُّهَا إِيمَانٌ وَجِهَادٌ فِي سَبِيلِ الدَّعْوَةِ الإِسْلاَمِيَّةِ، وَتَرَبَّتْ عَلَى مَبَادِئ الْحَقِّ وَالتَّوْحِيدِ وَالصَّبْرِ، إِنَّهَا السَّيِّدَةُ أَسْمَاءُ بِنْتُ أَبِي بَكْرٍ الصِّدِّيقِ(رضي الله عنها).
وُلِدتْ أَسْمَاءُ فِي مَكَّةَ الْمُكَرَّمَةِ قَبْلَ الْهِجْرَةِ بِسَبْعَةٍ وَعِشْرِينَ عَاماً، وَأَسْلَمَتْ عَنْ عُمُرٍ لاَ يَتَجَاوَزُ الرَّابِعَةَ عَشْرَةَ، وَقَدْ بَدَا وَاضِحاً مُنْذُ الْبِدَايَةِ مَظَاهِرُ ذَكَائِهَا وَأَدَبِهَا وَفَصَاحَةِ لِسَانِهَا الَّتِي اكْتَسَبَتْهَا مِنْ وَالِدِهَا سَيِّدِنَا أَبِي بَكْرٍ الصِّدِّيقِ (رضي الله عنه).
تَزَوَّجَتْ أَسْمَاءُ مِنَ الزُّبَيْرِ بْنِ الْعَوَّامِ، فَكَانَتْ لَهُ خَيْرَ الزَّوْجَةِ، وَأَنْجَبَتْ لَهُ الْبَنِينَ وَالْبَنَاتِ، كَانَ مِنْهُمْ عَبْدُ اللهِ وَعُرْوَةُ وَعَاصِمٌ، وَأُمُّ الْحَسَنِ.
وَكَانَتْ تَحُثُّهُمْ دَائِماً عَلَى الإِنْفَاقِ فِي سَبِيلِ اللهِ، وَعَلَى حُسْنِ الْخُلُقِ فِي مُعَامَلِةِ النَّاسِ. جَادَتْ أَسْمَاءُ بِكُلِّ ثَمِينٍ مِنْ أَجْلِ الإِسْلاَمِ، فَلاَ نَنْسَى مَوْقِفَهَا فِي حَادِثَةِ الْهِجْرَةِ، عِنْدَمَا شَقَّتْ نِطَاقَهَا نِصْفَيْنِ لِرَبْطِ الطَّعَاِم، فَسَمَّاهَا النَّبِيُّ (صلى الله عليه وسلم) ذَاتَ النِّطَاقَيْنِ، وَقَالَ لَهَا(صلى الله عليه وسلم): " أَبْدَلَكِ اللهُ- عَزَّ وَجَلَّ- بِنِطَاقِكِ هَذَا نِطَاقَيْنِ فِي الْجَنَّةِ".
""",

"""
-Grad 5
 التقييم  الذَّاتِيُّ 
لَقَدْ قمت بِدِرَاسَةِ نَصَّيْنِ مِنْ النُّصُوصِ الشِعْرِيَّةِ الْقَصَصِيَّةِ، وَتَعَرَّفتَ خِلَالَهُمَا الْسِّمَاتِ الْبِنَائِيَّةِ وَالْأُسْلُوبِيَّةَ لَهُمَا، وَ مِنْ الْمُؤَكَّدِ أَنَّكَ قَدِ اكْتَسَبْتَ مَهَارَاتٍ عَدِيْدَةٍ فِي مَجَالَاتِ الْقِرَاءَةِ وَالْتَحَدُّثِ، وَالاسْتِمَاعِ والْكِتَابةِ ، فَضْلاً عَنِ الْمَعَلُومَاتِ الْنَّحْوِيَّةِ.
وِالِآنِ قَيِّمْ جُهُودَكَ ذَاتِياً، مُسْتَعِيْناً بِالْجَدْوَلِ الْآتِي:
دَرَجَةُ الْفَاعِلِيَّةُ فِي الْإِعْدَادِ وَالْتَّحْضِيرِ .
القِرَاءَةُ الْبَصَرِيْةُ لِلْنُصُوصِ، وَإدْرَاكِ مَعَانِيهَا الْإجْمَالِيَّةِ.
القِرَاءَةُ الْجَهْرِيَّةُ وِفْقَ مَبَادِئ الْنُّطْقِ الْسَلِيْمِ.
الْقُدْرَةُ عَلَى شَرْحِ مَعَانِي الْنَّصِّ، وَإدْرَاكُهَا.
الْقُدْرَةُ عَلَى تَحْلِيْلِ الْسِّمَاتِ الْخَاصَّةِ لِلْنُصُوصِ الْشِّعْرِيَّةِ الْقَصَصِيَّةِ وَفَهْمُهَا.
تَعَرُّفُ عَلَى الْمَفْعُولِ الْمُطلَقِ، وإن وأَخوَاتُها  وَاسْتِخْدَامُهَا.
تَعَرُّفُ قَوَاعِدِ كِتَابَةِ الْهَمْزَةُ الْمُتَوسِطَةُ عَلَى الوَاوِ وَاسْتِخْدَامُهَا بِشَكْلٍ صَحِيْحٍ.
الْتَّمْكُنُ مِنْ نَثْرِ نُصُوصٍ شِعْرِيَّةٍ قَصَصِيَّةٍ.
الاسْتِمَاعُ بِتَرْكِيزٍ، لِلْحُصُولِ عَلَى الْمَعْنَى الْعَامِّ فِي عَدَدٍ مِنْ المَوضُوعَاتِ.
إلْقَاءُ الْشِّعْرِ بِطَلَاقَةٍ، مَعَ الْقُدْرَةِ عَلَى تَمْثِيْلِ الْمَعْنَى.
""",
"""
-Grad 6
حَلَّ الْمَساءُ وَانْتَشَرَتِ الْعَتْمَةُ وَكَانَ الْيَوْمُ التَّالِي يَوْمَ عُطْلَةٍ ، لِذَا فَقَدْ تَجَمَّعَ أَطْفَالُ الْعَائِلَةِ حَوْلَ جِدِّهِمْ ، وَطَلَبُوا مِنْهُ أَنْ يَقُصَّ عَلَيْهِمْ حِكَايَةً ، ابْتَسَمَ الْجَدُّ ...وَقَالَ : سَأَحْكِي لَكُمْ حِكَايَةً سَمِعْتُهَا مِنْ جَدِّي ، إِنَّهَا حِكَايَةُ (جِلْدُ الدُّبِّ )
يَا أَحِبَّائِي ، فِي قَدِيمِ الزَّمَانِ كَانَتْ هُنَاكَ قَرْيَةٌ تَقَعُ عَلَى تَلٍّ غَيْرِ مُرْتَفِعٍ تُحِيطُ بِهَا الْبَسَاتِينُ وَالْكُرُومُ وَالسُّهُولُ مِنْ جِهَاتِهَا الْأَرْبَعِ حَبَاهَا اللهُ الْيَنابِيعَ فَكَانَتْ مِيَاهُهَا لَا تَنْقَطِعُ شِتَاءً وَلَا صَيْفاً وَكَانَ نَاسُهَا كَأَهْلِ الْقُرَى جَمِيعاً يَتَعَاوَنُونَ فِي أَحْيانٍ كَثِيرَةٍ وَيَخْتَلِفُونَ فِي بَعْضِ الْأَحْيانِ .
وَذَاتَ يَوْمٍ اكْتَشَفَ مَالِكُ أَحَدِ كُرُومِ الْعِنَبِ فِي الْجِهَةِ الشَّمَالَّيِةِ مِنَ الْقَرْيَةِ أَنَّ عَنَاقِيدَةُ نَاقِصَهٌ وَأَصَابَ بَعْضَها التَّخْرِيبُ وَالتَّلَفُ حَتَّى قَبْلَ أَنْ تَنْضُجَ ، فَأخْبَرَ الرَّجُلُ جِيرَانَهُ بِمَا رَأى وَأخَذُوا يَبْحَثُونَ مَعَهُ عَنِ الْفَاعِلِ لَكِنْ دُونَ جَدْوَى .
""",

]


def text_static_readability_composition(data, text):
	'''
	Argument:
		data: as python dictionary
		text: That user input on our interphase
	return:
		data as dictionary with text analysis calculated
	'''

	# Counts Statics
	minute1, seconds1 = (ReadingTime(text))
	minute, seconds = (SpeakingTime(text))
	# reading_time = reading_time.split('.')
	# speaking_time = speaking_time.split('.')
	reading_time= str(minute1) + ":" + str(seconds1)
	speaking_time= str(minute) + ":" + str(seconds)
	statics_calculations = {
		'character_count'   : characterCount(text),  # ReadabilityGradeLevels file
		'syllable_count'	: syllableCount(text), 	 # ReadabilityGradeLevels file
		'word_count'		: wordCount(text), 		 # ReadabilityGradeLevels file
		'unique_word_count'	: uniqueWordCount(text), # ReadabilityGradeLevels file
		'sentence_count'	: sentenceCount(text), 	 # ReadabilityGradeLevels file
		'paragraph_count' 	: paragraphCount(text),  # ReadabilityGradeLevels file
		'reading_time' 		: reading_time,  	 # ReadabilityGradeLevels file
		'speaking_time' 	: speaking_time,  	 # ReadabilityGradeLevels file
	}
	
	

	# Readability GradeLevels
	readability_gradeLevels = {
		'flesch_kincaid_grade_level'   	: FKRA(text),    # ReadabilityGradeLevels file
		'gunning_fog_index'				: GFI(text),     # ReadabilityGradeLevels file
		'coleman_liau_index'			: CLI(text),     # ReadabilityGradeLevels file
		'smog'							: SMOGI(text),   # ReadabilityGradeLevels file
		'automated_readability_index'	: ARI(text),     # ReadabilityGradeLevels file
		'flesch_reading_ease' 			: FRE(text), # ReadabilityGradeLevels file
		'powers_sumner_kearl_grade' 	: PSKG(text),    # ReadabilityGradeLevels file
		'FORCAST_grade_level' 			: FORCAST(text),    # ReadabilityGradeLevels file
		'Rix_readability' 				: RIX(text),    # ReadabilityGradeLevels file
		'spache_score' 					: SPACHE(text),    # ReadabilityGradeLevels file
		'new_dale_chall_score' 			: NDC(text),    # ReadabilityGradeLevels file
		'Lix_readability' 				: LIX(text),    # ReadabilityGradeLevels file
		'lensear_write' 				: LensearWrite(text),    # ReadabilityGradeLevels file
	}

	# Readability Issues
	readability_issues = {
		's_g_30s' 						: s_g_30s(text),    # ReadabilityGradeLevels file
		's_g_20s' 						: s_g_20s(text),    # ReadabilityGradeLevels file
		'w_g_4s' 						: w_g_4s(text),    # ReadabilityGradeLevels file
		'w_g_12l' 						: w_g_12l(text),    # ReadabilityGradeLevels file

		's_g_30s2' 						: (int((s_g_30s(text)/sentenceCount(text)*100))),    # ReadabilityGradeLevels file
		's_g_20s2' 						: (int((s_g_20s(text)/sentenceCount(text)*100))),    # ReadabilityGradeLevels file
		'w_g_4s2' 						: (int((w_g_4s(text)/wordCount(text)*100))),    # ReadabilityGradeLevels file
		'w_g_12l2' 						: (int((w_g_12l(text)/wordCount(text)*100))),    # ReadabilityGradeLevels file
	}


	# Text Density Issues & Language Issues
	text_density_issues = {
		# 'spelling_issues'				: spellingIssues(text), # ReadabilityGradeLevels file
		# 'grammar_issues'				: grammarIssues(text), # ReadabilityGradeLevels file
		'passive_voice_count'			: passiveCount(text), # ReadabilityGradeLevels file
		'characters_per_word' 			: CPW(text),    # ReadabilityGradeLevels file
		'syllables_per_word' 			: SPW(text),    # ReadabilityGradeLevels file
		'words_per_sentence' 			: WPS(text),    # ReadabilityGradeLevels file
		'words_per_paragraph' 			: WPP(text),    # ReadabilityGradeLevels file
		'sentences_per_paragraph' 		: SPP(text),    # ReadabilityGradeLevels file
	}

	# print(statics_calculations['reading_time'].)
	# statics_calculations dictionary created above
	data['statics_calculations'] = statics_calculations

	# readability_issues dictionary created above
	data['readability_issues'] = readability_issues

	# text_density_issues & Language Issues dictionary created above
	data['text_density_issues'] = text_density_issues

	# readability_gradeLevels dictionary created above
	data['readability_gradeLevels'] = readability_gradeLevels

	# Text Composition 
	data['text_composition'] 		= get_text_composition(text) # text_composition file
	return data


##-----------------------------------Arabic


def arabic_text_static_readability_composition(data, text):
	'''
	Argument:
		data: as python dictionary
		text: That user input on our interphase
	return:
		data as dictionary with text analysis calculated
	'''

	minute1, seconds1 = (arabic_ReadingTime(text))
	minute, seconds = (arabic_SpeakingTime(text))
	# reading_time = reading_time.split('.')
	# speaking_time = speaking_time.split('.')
	reading_time= str(minute1) + ":" + str(seconds1)
	speaking_time= str(minute) + ":" + str(seconds)
	# reading_time = reading_time[0] + ":" + reading_time[1]
	# Counts Statics
	statics_calculations = {
		'character_count'   : arabic_characterCount(text),  # ReadabilityGradeLevels file
		'syllable_count'	: arabic_syllables_count(text), 	 # ReadabilityGradeLevels file
		'word_count'		: arabic_wordCount(text), 		 # ReadabilityGradeLevels file
		'unique_word_count'	: arabic_uniqueWordCount(text), # ReadabilityGradeLevels file
		'sentence_count'	: arabic_sentenceCount(text), 	 # ReadabilityGradeLevels file
		'paragraph_count' 	: arabic_paragraphCount(text),  # ReadabilityGradeLevels file
		'reading_time' 		: reading_time,  	 # ReadabilityGradeLevels file
		'speaking_time' 	: speaking_time,  	 # ReadabilityGradeLevels file

	}

	arabic_AARIs = {
		'arabic_ARI2'   		: arabic_ARI2(text),  # ReadabilityGradeLevels file
		'arabic_AARI'			: arabic_AARI(text), 	 # ReadabilityGradeLevels file
		'arabic_Al_Heeti'		: arabic_Al_Heeti(text), 		 # ReadabilityGradeLevels file

	}
	# Text Density Issues & Language Issues
	text_density_issues = {
		# 'spelling_issues'				: arabic_spellingIssues(text), # ReadabilityGradeLevels file
		# 'grammar_issues'				: grammarIssues(text), # ReadabilityGradeLevels file
		'passive_voice_count'			: passiveCount(text), # ReadabilityGradeLevels file
		'characters_per_word' 			: arabic_CPW(text),    # ReadabilityGradeLevels file
		'syllables_per_word' 			: arabic_SPW(text),    # ReadabilityGradeLevels file
		'words_per_sentence' 			: arabic_WPS(text),    # ReadabilityGradeLevels file
		'words_per_paragraph' 			: arabic_WPP(text),    # ReadabilityGradeLevels file
		'sentences_per_paragraph' 		: arabic_SPP(text),    # ReadabilityGradeLevels file
	}

	# readability_gradeLevels dictionary created above
	readability_gradeLevels = {
		'flesch_kincaid_grade_level'   	: arabic_FKRA(text),    # ReadabilityGradeLevels file
		'gunning_fog_index'				: arabic_GFI(text),     # ReadabilityGradeLevels file
		'coleman_liau_index'			: arabic_CLI(text),     # ReadabilityGradeLevels file
		'smog'							: arabic_SMOGI(text),   # ReadabilityGradeLevels file
		'automated_readability_index'	: arabic_ARI(text),     # ReadabilityGradeLevels file
		'flesch_reading_ease' 			: arabic_FRE(text), # ReadabilityGradeLevels file
		'powers_sumner_kearl_grade' 	: arabic_PSKG(text),    # ReadabilityGradeLevels file
		'FORCAST_grade_level' 			: arabic_FORCAST(text),    # ReadabilityGradeLevels file
		'Rix_readability' 				: arabic_RIX(text),    # ReadabilityGradeLevels file
		'spache_score' 					: arabic_SPACHE(text),    # ReadabilityGradeLevels file
		'new_dale_chall_score' 			: arabic_NDC(text),    # ReadabilityGradeLevels file
		'Lix_readability' 				: LIX(text),    # ReadabilityGradeLevels file
		'lensear_write' 				: LensearWrite(text),    # ReadabilityGradeLevels file
	}
	
	# Readability Issues
	readability_issues = {
		's_g_30s' 						: arabic_s_g_30s(text),    # ReadabilityGradeLevels file
		's_g_20s' 						: arabic_s_g_20s(text),    # ReadabilityGradeLevels file
		'w_g_4s' 						: arabic_w_g_4s(text),    # ReadabilityGradeLevels file
		'w_g_12l' 						: arabic_w_g_12l(text),    # ReadabilityGradeLevels file

		's_g_30s2' 						: (int((arabic_s_g_30s(text)/arabic_sentenceCount(text)*100))),    # ReadabilityGradeLevels file
		's_g_20s2' 						: (int((arabic_s_g_20s(text)/arabic_sentenceCount(text)*100))),    # ReadabilityGradeLevels file
		'w_g_4s2' 						: (int((arabic_w_g_4s(text)/arabic_wordCount(text)*100))),    # ReadabilityGradeLevels file
		'w_g_12l2' 						: (int((arabic_w_g_12l(text)/arabic_wordCount(text)*100))),    # ReadabilityGradeLevels file
	
	}

	# statics_calculations dictionary created above
	data['statics_calculations'] = statics_calculations

	# text_density_issues & Language Issues dictionary created above
	data['text_density_issues'] = text_density_issues

	# readability_gradeLevels dictionary created above
	data['readability_gradeLevels'] = readability_gradeLevels
	
	data['readability_issues'] = readability_issues

	data['arabic_AARIs'] = arabic_AARIs

	data['text_composition'] = arabic_POS(text)


	#----------Connect to farasa APIs
	data['arabic_seg'] = arabic_seg(text)

	data['arabic_lemma'] = arabic_lemma(text)
	data['arabic_SpCH'] = arabic_SpCH(text)
	# data['arabic_Diac'] = arabic_Diac(text)
	data['arabic_Diac2'] = arabic_Diac2(text)

	return data


##-----------------------------------Hindi


def hindi_text_static_readability_composition(data, text):
	'''
	Argument:
		data: as python dictionary
		text: That user input on our interphase
	return:
		data as dictionary with text analysis calculated
	'''

	# Counts Statics
	reading_time = str(ReadingTime(text))
	speaking_time = str(SpeakingTime(text))
	reading_time = reading_time.split('.')
	speaking_time = speaking_time.split('.')
	reading_time = reading_time[0] + ":" + reading_time[1]
	speaking_time = speaking_time[0] + ":" + speaking_time[1]

	statics_calculations = {
		'character_count'   : characterCountHindi(text),  # ReadabilityGradeLevels file
		'syllable_count'	: syllableCountHindi(text), 	 # ReadabilityGradeLevels file
		'word_count'		: wordCountHindi(text), 		 # ReadabilityGradeLevels file
		'unique_word_count'	: uniqueWordCountHindi(text), # ReadabilityGradeLevels file
		'sentence_count'	: sentenceCountHindi(text), 	 # ReadabilityGradeLevels file
		'paragraph_count' 	: paragraphCountHindi(text),  # ReadabilityGradeLevels file
		'reading_time' 		: reading_time,  	 # ReadabilityGradeLevels file
		'speaking_time' 	: speaking_time,  	 # ReadabilityGradeLevels file
	}
	

	# Readability GradeLevels
	readability_gradeLevels = {
		'flesch_kincaid_grade_level'   	: FKRAHindi(text),    # ReadabilityGradeLevels file
		'gunning_fog_index'				: GFIHindi(text),     # ReadabilityGradeLevels file
		'coleman_liau_index'			: CLIHindi(text),     # ReadabilityGradeLevels file
		'smog'							: SMOGIHindi(text),   # ReadabilityGradeLevels file
		'automated_readability_index'	: ARIHindi(text),     # ReadabilityGradeLevels file
		'flesch_reading_ease' 			: FREHindi(text), # ReadabilityGradeLevels file
		'powers_sumner_kearl_grade' 	: PSKGHindi(text),    # ReadabilityGradeLevels file
		'FORCAST_grade_level' 			: FORCASTHindi(text),    # ReadabilityGradeLevels file
		'Rix_readability' 				: RIXHindi(text),    # ReadabilityGradeLevels file
		'spache_score' 					: SPACHEHindi(text),    # ReadabilityGradeLevels file
		'new_dale_chall_score' 			: NDCHindi(text),    # ReadabilityGradeLevels file
		'Lix_readability' 				: LIXHindi(text),    # ReadabilityGradeLevels file
		'lensear_write' 				: LensearWriteHindi(text),    # ReadabilityGradeLevels file
	}

	# print(readability_gradeLevels)

	# # Readability Issues
	readability_issues = {
		's_g_30s' 						: s_g_30Hindi(text),    # ReadabilityGradeLevels file
		's_g_20s' 						: s_g_20Hindi(text),    # ReadabilityGradeLevels file
		'w_g_4s' 						: w_g_4Hindi(text),    # ReadabilityGradeLevels file
		'w_g_12l' 						: w_g_12Hindi(text),    # ReadabilityGradeLevels file

		's_g_30s2' 						: (int((s_g_30Hindi(text)/sentenceCountHindi(text)*100))),    # ReadabilityGradeLevels file
		's_g_20s2' 						: (int((s_g_20Hindi(text)/sentenceCountHindi(text)*100))),    # ReadabilityGradeLevels file
		'w_g_4s2' 						: (int((w_g_4Hindi(text)/wordCountHindi(text)*100))),    # ReadabilityGradeLevels file
		'w_g_12l2' 						: (int((w_g_12Hindi(text)/wordCountHindi(text)*100))),    # ReadabilityGradeLevels file
	}


	# Text Density Issues & Language Issues
	text_density_issues = {
		# 'spelling_issues'				: spellingIssues(text), # ReadabilityGradeLevels file
		# 'grammar_issues'				: grammarIssues(text), # ReadabilityGradeLevels file
		'passive_voice_count'			: passiveCount(text), # ReadabilityGradeLevels file
		'characters_per_word' 			: CPWHindi(text),    # ReadabilityGradeLevels file
		'syllables_per_word' 			: SPWHindi(text),    # ReadabilityGradeLevels file
		'words_per_sentence' 			: WPSHindi(text),    # ReadabilityGradeLevels file
		'words_per_paragraph' 			: WPPHindi(text),    # ReadabilityGradeLevels file
		'sentences_per_paragraph' 		: SPPHindi(text),    # ReadabilityGradeLevels file
	}
	# # print(statics_calculations['reading_time'].)
	# # statics_calculations dictionary created above
	data['statics_calculations'] = statics_calculations

	# # readability_issues dictionary created above
	data['readability_issues'] = readability_issues

	# # text_density_issues & Language Issues dictionary created above
	data['text_density_issues'] = text_density_issues

	# # readability_gradeLevels dictionary created above
	data['readability_gradeLevels'] = readability_gradeLevels

	# # Text Composition 
	# data['text_composition'] 		= get_text_composition(text) # text_composition file
	return data


def random_lines_language(language_samples):
	'''
	Argument:
	language_samples: choose random samples
	return:
		random lines from created list above based on user language choice
	'''
	random_index 			 	= np.random.randint(len(language_samples))
	random_lines 			 	= language_samples[random_index]
	return random_lines


def home_page(request):
	'''
	Argument:
		request: page request
	return:
		either the page itself if get request
		or if post make some analysis and return json result to js and js add to page
	'''
	data = {}
	if request.method == 'POST':
		try:
			# if the user write in input text
			data = json.loads(request.body)
			text = data['user_text']
			t = text[:24]
			if data['language_selected'] 	== 'English':
				if "-Elementary" in t or "-Intermediate B1" in t or "-Upper Intermediate" in t or "-Intermediate" in t or "-Beginner A1" in t or "-Advanced C1  " in t or "-Upper intermediate B2" in t or "-Pre-intermediate A2 " in t:
					text = text[24:]
				# text = text[20:]
				data 						= text_static_readability_composition(data, text)
				return JsonResponse(data)

			elif data['language_selected'] 	== 'Arabic':
				if "-Grad" in text[:10]:
					text = text[8:]
				data 						= arabic_text_static_readability_composition(data, text)
				return JsonResponse(data)

			elif data['language_selected'] 	== 'Hindi':
				data 						= hindi_text_static_readability_composition(data, text)
				return JsonResponse(data)
		except:
			# if the user choose to get random input
			if data['language_selected'] 	== 'English':
				data['generated_text'] 		= random_lines_language(EnglishSamples10)
				return JsonResponse(data)

			elif data['language_selected'] 	== 'Arabic':
				data['generated_text'] 		= random_lines_language(QatarSamplesGrades)
				return JsonResponse(data)

			elif data['language_selected'] 	== 'Hindi':
				data['generated_text'] 		= random_lines_language(HindiSamples12)
				return JsonResponse(data)
	return render(request, 'text_analysis/home_page.html', data)
	



def about_page(request):
	'''
	Argument:
		request: page request
	return:
		get about request
	'''
	return render(request, 'text_analysis/about.html')
	


def contact_page(request):
	'''
	Argument:
		request: page request
	return:
		either the page itself if get request
		Or retrieve and send form data to database
	'''
	if request.method == "POST":
		data = json.loads(request.body)
		Contact_us.objects.create(
		    mail=data['mail'],
		    first_name=data['first_name'],
		    phonenumber=data['phonenumber'],
		    message=data['message']
		)
		return JsonResponse(data)
	return render(request, 'text_analysis/contact.html')