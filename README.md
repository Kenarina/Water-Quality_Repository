# Water Quality Advisory #

The Water Quality Advisory (WaQua) is a simple tool that can be adapted for water water quality monitoring and water-safety related advisory services. The potential for its further development is huge. In its current form, the Advisory is is command-line based application.  

## Description ##

The WaQua application starts with a request for user input. Numerical data from measurement of water quality parameters (including pH and concentrations of trace heavy metals: Lead, CCadmium, Zinc, Mercury, Arsenic, Chromium and Nickel), along with numerical day of the month, are entered. The user data is validated for completeness and writted to a google spreadsheet. While there, the metal concentration data is isolated in another sheet and used to compute a weekly summary, using python. The summary data (average, median,minimum and maximum,) is then written in a separate sheet within the parent file. The weekly average concentration values are then compared with the Maximum Contamination Limits tolerable for drinking water. On the basis of this comparison, advisory message is printed for the user. 

The live site is available [here](https://kenarina.github.io//)

## User stories ##

The following considerations of the user experience underly the design of the website:  

1. A simple and easily understandable application.  

2. Some degree of interactivity to the extent of input of user data and feedback regarding the progress of the program.

4. Relevance to daily living, hence potentially useful on daily basis.

# UX/UI Design #

## Structure ##

Although this is a command-line application, the process of the application was envisioned using a chart created via Lucidchart [Lucidchart](https://lucid.app/lucidchart/20e7547c-a810-4419-be15-12fae9b00459/edit?viewport_loc=218%2C127%2C1645%2C695%2C0_0&invitationId=inv_246535d8-66cd-430b-927c-db1e51849ffa):  

## Testing ##
Performance of the written python code to achieve the desired outcome was regularly tested using print statements to the terminal in stepwise and consistent manner. Corrections were made and tested iteratively until the desired outcome was achieved. The program alsoperformed successfully on the Heroku mock terminal. The code was also tested using CI Python Linter and the detected bugs were addressed. Just one bug (153: E501 line too long (85 > 79 characters)) was not addressed as it was just 5 characters longer in a function.


##  Technologies ##
 
[Codeanywhere](https://codeanywhere.com/) cloud IDE for writing the program. 
[Lucidchart](https://lucidchart.com/) for process workflow design.  
[GitHub](https://github.com/) to host the source code.
[Git](https://git-scm.com/) for version control. 

Other resources, including course material from Code Institute, were consulted from time to time. Examples include: [StackOverflow](https://stackoverflow.com/).

 However, the course material from Code Institute was the primary resource. 

 Microsoft Edge chat was used to get insight into some coding solutions, especially the function for comparing weekly averages with MCLs. 

## Deployment ##

This project was deployed to Heroku via Github. The live site is [here](https://water-quality-advisory-514eb5718a6d.herokuapp.com/)

## Acknowledgements ##

I am always grateful to Ronan McClelland, for his very helpful advice towards this project. Special thanks to the Code Institute Student Care team for their support along this journey.