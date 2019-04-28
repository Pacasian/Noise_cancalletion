# Noise_cancalletion

Basically, the main objective of this project is to eliminate the background noise while having a voice call(voip) or voice message.
so the project can be layed out into three successive modules. 
<br> 
 -  Android application      
 -  AWS or Firebase (as a back-end server)     
 -  A python script which will itenfier and mask the noise    
 
 ### 1. Android Application :
 
 So , the android application will work as a front-end of your project, providing **chat** and **voip** services to our clients. The working schema of the project is :-
 > The app provide one to one chat servuce 
 > The app send the voice message file to the **aws** or **firebase** server along with the receives id.(only 50 percent completed)
 > The app can connect its users through voip over the back-end server.(Future Enhancement)  
 
 ### 2. AWS back-end server:
 The aws or firebase as mentioned work as an backend for this project. bascially it receives the audio message through api and execute the python script over this message for quality correction.
 
 ### 3.Python script :
 basically we used the reduced noise power algoritkm on this file 
 

