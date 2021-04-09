# ScriptingForTesters

Exercise files for the LinkedIn course Scripting for Tester

For setting up a PyChaarm Python project with GitHib, check out https://gist.github.com/tcd1558/a838deda7dd5968bab6c3d88b9aa466d
This allows you to start with a fresh GitHub repository with the basics of a PyCharm Python project. You now can add exercises and when solving the exercises, you can tread each exercise as a bugfix. This will give you a taste of how GitHub is used professionally. 

## In Section 1, Authentication

In this section you learn about GET, POST, PUT, DELETE

You also learn about authentication with get(url, auth=('djw-test', 'password1')) 
or the use of a token. 

I have the feeling there is still something missing. Maybe this kind of authentication has been disabled and OAuth is now the standard.      
According to docs.github under https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api#authentication you can access your GitHub account using curl. I have tried using the following curl commands:

> $ curl -i -u your_username https://api.github.com/users     
> $ curl -i -u your_username https://api.github.com/users/     
> $ curl -i -u your_username https://api.github.com/users/<username\>           
 
All commands request the password to be entered. I have tried using the email address used for Github as well as the Github user for your_username and I have omitted and added the GitHub user for <username\>. None of them work. ----  I have the feeling something needs to be enabled or disabled on GitHubs end in order for this to work.       
I am using MacOS 10.12.6 ( Id like to update, but can not anymore), curl release date 2020-01-08, git 2.14.3, python 3.9.2, requests 2020.12.5

The following command:
> $ curl -i -u your_username https://api.github.com/users/ 

does return data. Apparently from 'all' users, not including self. 

## Section 2, Exercise 02_02

Problem: 
When loading ../begin/column_chart.html, the result is an empty page. 
When loading ../end/column_chart.html, a column chart is displayed. 

Comparing the two shows the flowing differences (Notes).


https://developers.google.com/chart/interactive/docs/basic_load_libs

> <script src="https://www.gstatic.com/charts/loader.js"></script>     
> <script>     
>   google.charts.load('current', {packages: ['corechart']});      
>   google.charts.setOnLoadCallback(drawChart);      
>   ...      
> </script>    

Note: The solution includes '<script type="text/javascript" ..'
	This is also included on the developers page in the video. 
	Yet, on the current developers page the 'type=".."' is missing.
	This is not the cause of the problem.    

https://developers.google.com/chart/interactive/docs/datatables_dataviews
https://developers.google.com/chart/interactive/docs/datatables_dataviews#arraytodatatable

> var data = google.visualization.arrayToDataTable([     
>        ['Employee Name', 'Salary'],      
>        ['Mike', {v:22500, f:'22,500'}], // Format as "22,500".      
>        ['Bob', 35000],      
>        ['Alice', 44000],      
>        ['Frank', 27000],      
>        ['Floyd', 92000],      
>        ['Fritz', 18500]     
>       ],      
>       false); // 'false' means that the first row contains labels, not data.      

Note: Use Clipboard icon. Replace label with $labels and data with $data 

https://developers.google.com/chart/interactive/docs/basic_draw_chart

> // Instantiate and draw our chart, passing in some options.      
>       var chart = new google.visualization.PieChart(document.getElementById('chart_div'));       
>       chart.draw(data, options);      

Note: The var should be alligned with the var data. Not the cause of 
	the problem.

> //Div that will hold the pie chart     
>     <div id="chart_div" style="width:400; height:300"></div>     

Note: If you leave the comment '//Div ..', it will be displayed on the output. 

Next you create a for loop. Make sure, the assignment of chart_data_str does 
	NOT include an extra ',' like: '%s, \n,'%row
	The extra blank is not a problem, because it does not alter the number 
	of elements. 

## 02.05 Google Developers API

You need a Google account
Create a Google Service Account

https://console.developers.google.com/apis/dashboard
Create a project

Either use the pull down menu [Select a project v] 
	New Project (up to 12)
or click on [CREATE PROJECT] to the right. 

Project Name: <MyProject>
[CREATE]
+ ENABLE APIS AND SERVICES

Search for Sheets
[ENABLE]
Back, Back
Search for Drive
Select Googe Drive API
[ENABLE]

In 'RPI APIs & Services' click on 
Dashboard

Credentials
[+ CREATE CREDENTIALS]
Service account
Section 1: Service account details
	Service account name: ScriptAccount
	Service account ID: scriptaccount@<MyProject>.iam.gserviceaccount.com
	Role - Project, Editor - moved to section 2 
	Key Type - JSON - no longer available.
	[Create]

Section 2: Grant this service account access to project 
(optional)

[Select a role v]
	Basic, Editor
[CONTINUE]

Section 3: Grant users access to this service account
(optional) 
	Learn more:
https://cloud.google.com/iam/docs/service-accounts
https://cloud.google.com/iam/docs/impersonating-service-accounts?_ga=2.193283823.-396094699.1615679811

	Service account users role: skip since optional
	Service account admins role: skip since optional

[DONE]

After click on the last [DONE] above, you get a table with 'API Keys', 'OAuth 2.0 Client IDs', 'Service Accounts'. 
Under the header 'Service Accounts', you found the just created Service Account.
Clicking on the Service Account brings up a new screen with a tab 'Keys'. 
Open that tab 'Keys'

[Add Key v]
Create new key
(o)JSON

A file is downloaded. 

https://www.google.com/sheets/about/

Start a new spreadsheet, Blank

--------------------------------------------------------------------------------

Section 02_06

Use the pip3 in the same path as python3.
The python3 used in Pycharm is defined by the link in venv/bin/python3
/usr/local/bin/pip3 install gspread
/usr/local/bin/pip3 install google-api-python-client
/usr/local/bin/pip3 install oauth2client
Prefereably install through PyCharm 

pip3 list -- gives a list
pip3 show -- gives details from one module

https://gspread.readthedocs.io
--------------------------------------------------------------------------------

## Section 02_07

Create a new spreadsheet under https://docs.google.com/spreadsheets
Name it TestRunData
Import 
(0) replace current sheet
(0) Comma
(0) Yes
[Import data]

Convert Average Run Time to '=Average(C2:G2)'

[Share] scriptaccount@<MyProject>.iam.gserviceaccount.com

--------------------------------------------------------------------------------

## Section 03_01

Open the SeleniumExample.py
import selenium from webdriver
Hover the mouse over selenium and install 

--------------------------------------------------------------------------------

## Section 03_02

https://www.seleniumhq.org has been moved to https://www.selenium.dev
The layout of the page has changed. 

--------------------------------------------------------------------------------

## Section 03_03

http://www.phptravels.net/offers is no longer a test site. They do no appreciate the testing traffic. 


