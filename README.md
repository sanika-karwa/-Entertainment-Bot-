# Entertainment Bot
A virtual assistant powered by **Rasa 2.0** which provides suggestions for entertainment options like podcasts, books and music based on our mood and what we wish to see. 

#### Instructions to run:

1.	Create virtual environment using *python3 -m venv ./venv*
2.	Activate the environment using source *./venv/bin/activate*
3.	Download all the dependencies as mentioned in requirements.txt
4.	Clone this repository in your local machine
5.	Train the model using *rasa train*
6.	Activate the action server in another terminal using *rasa run actions*
7.	Now run the bot in terminal using *rasa shell*

#### Process to open Database file:

1.	Go to venv directory where sqlite3 is present and on terminal type *.\sqlite3*
2.	Open the databse file using *.open "test.db"*
3.	View the table using *SELECT * FROM new_data;*

#### Conversation Flow:

##### Story 1:

Intent: Hey <br>

Response: Hey!! I am an entertainment bot wherein I will give you great suggestions according to your mood. What is your firstname? <br>

Intent: Sanika <br>

Response: How are you doing today, Sanika? <br>

Intent: I am doing good <br>

Response: That's awesome <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What do you wish to do today? <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1. Listen to Podcast <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2. Read a book <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3. Listen to music <br>
          
Intent: podcast <br>

Response: Great choice, Sanika!! What is the genre that you generally prefer in this to know you better? <br>

Intent: <Any of motivation/health/technology/comedy/science> ***motivation*** <br>

Response: That’s an awesome podcast genre choice!! <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;What type of podcast do you want to listen to? <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.	Happy Podcast <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.	Motivational Podcast <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.	Crime Podcast <br>
            
Intent: motivation podcast <br>

Response: Let me get some amazing options for you in this category <br>

**Bot displays the motivation podcasts fetched from Youtube API.** <br>

Intent: Thats good <br>

Response: Would you like to know some other options as well? <br>

Intent: yes <br>

Response: What do you wish to do today?  <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.	Listen to Podcast <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.	Read a book <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.	Listen to music <br>
            
Intent: book <br>

Response: Great choice, Sanika!! What is the genre that you generally prefer in this to know you better? <br>

Intent: <Any of Thriller/happy/sad/biography/fairytale> ***Thriller*** <br>

Response: That’s an awesome book genre choice!! <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; What type of book do you want to listen to? <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;1.	Thriller Book <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;2.	Self-help book <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;3.	Fictional Book <br>
            
Intent: Thriller book <br>

Response: Let me get some amazing options for you in this category <br>

**Bot displays the thriller books fetched from Google Books API.** <br>

Intent: awesome <br>

Response: Would you like to know some other options as well? <br>

Intent: no <br>

Response: Did that help you, Sanika? <br>

Intent: yes <br>

Response: I would love your feedback. Please rate me on a scale of one-five. <br>

Intent: <Any of One/two/three/four/five> ***four*** <br>

Response: Thank you for your feedback! <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp; Would you like me to save your information? <br>
          
Intent: Yes save my info/yes I want to store my information <br>

**Bot saves the information in the database. User can check the updated database to verify.** <br>

Intent: Thanks <br>

Response: You're welcome. Have fun!! <br>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;It was great to have you here! Hope you got some good suggestions! <br>
          
Intent: bye <br>

Response: Bye <br>

***This is just one of the stories. Other stories are mentioned in the stories.yml file.***

#### Open Issues in the chatbot:
1.	Deployment on slack where the APIs did not work because of http timeout error

