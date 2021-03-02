# ScriptingForTesters

Exercise files for the LinkedIn course Scripting for Tester

For setting up a PyChaarm Python project with GitHib, check out https://gist.github.com/tcd1558/a838deda7dd5968bab6c3d88b9aa466d
This allows you to start with a fresh GitHub repository with the basics of a PyCharm Python project. You now can add exercises and when solving the exercises, you can tread each exercise as a bugfix. This will give you a taste of how GitHub is used professionally. 

## In Section 1, Authentication

I have the feeling there is still something missing. Maybe this kind of authentication has been disabled and OAuth is now the standard.      
According to docs.github under https://docs.github.com/en/rest/guides/getting-started-with-the-rest-api#authentication you can access your GitHub account using curl. I have tried using the following curl commands:

> $ curl -i -u your_username https://api.github.com/users     
> $ curl -i -u your_username https://api.github.com/users/     
> $ curl -i -u your_username https://api.github.com/users/<username\>           
 
All commands request the password to be entered. I have tried using the email address used for Github as well as the Github user for your_username and I have omitted and added the GitHub user for <username\>. None of them work. ----  I have the feeling something needs to be enabled or disabled on GitHubs end in order for this to work.       
I am using MacOS 10.12.6 ( Id like to update, but can not anymore), curl release date 2020-01-08, git 2.14.3, python 3.9.2, requests 2020.12.5
