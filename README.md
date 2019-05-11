# hello-world
first repository

Humans aware, this is a funny message. 

None of the following is true.

Nowhere. Nobody. Free space.


|Task 0|
|-|

As a Software Tester in an Agile team, you’re part of a team developing this new cool website: http://e.ggtimer.com/, which mainly comprises a front-end application. Get familiar with the project and do some exploratory testing to get a feeling for the website. Please document your findings.

First manual test with no knowledge about the application:
-Checking the elements on the mainpage e.ggtimer.
- several examples and hyperlinks (do all links work properly)
- text input field 
- which data types can be typed in? Numeric, alphanumeric, emojicons? 
- result of blank field? 
- standard field
- browser compatibility? Firefox – yes, Chrome – yes, Internet explorer/edge – problems, 
- mobilphone connectivity? Only ipad/ iphone possible > what happens if you turn screen from portrait to landscape
- audio signal output?
- result after timer is up? > no back arrow, just message time is up, so this is the endscreen, might be endscreen for several test cases
- maximum/minimum input value?


|Task 1|
|-|

|Test case/scenario | Expected result | Passed or failed|
|---|---|---|
|User clicks on all hyperlinks | All hyperlinks work |?|
|All fonts of the webpage are uniform/ the same style (depends on design specification) | All fonts are fine |?|
|User enters „-3 seconds“ into „Start a timer“ -textfield and presses „GO!“. | Timer is not starting, due to wrong usage/syntax. | |
|Minimum number of symbols is being typed in the textfield (empty) | Timer starts. | |
|Maximum number of symbols is being typed in the textfield. | Timer starts with maximumg value.| |
|1) Start browser on mobile device (ios) 2) browse to eggtimer and start countdown when position of device is in portray mode 3) turn the device into landscape 4) turn the device back in portrait 5) wait for timer to be finished | countdown visible as visual and text, "Time Expired!" pops up after time ran out, | |
| 1) Start eggtimer on mobile device (android) 2) browse to eggtimer and start countdown when position of device is in portray mode 3) turn the device into landscape  4) turn the device back in portrait5 wait for timer to be finished	|	countdown visible as visual and text, "Time Expired!" pops up after time ran out,|   | 
|Start the timer and disconnect from internet | The timer should continue / or bring an error message (depending on software design specification)	| |
|Check the compatibility to common browsers: Internet explorer Firefox Google chrome | Eggtimer works in all browsers	| |
|Maximising browser window Minimising browser window Maximising browser window | Shown text is properly shown, eggtimer still running | |
|Language compatibility check of the input | Is only possible to type in english language | |
|Check other input formats like time to a certain event (e.g. morning) | Time shown is time until the event | |


|Task 2|
|-|

Use the website http://e.ggtimer.com/ and your automation framework of choice. Setup a new test suite and implement the example integration test from above. Document how to setup the enviornment for your tests and how to run them in INSTALL.md. Commit your solution in this repository.

see INSTALL.md

|Task 3|
|-|

Pick 1-2 of the test cases from Task 1 and implement them as well.
See repository git

see INSTALL.md
