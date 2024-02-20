# Salary Calculator Web App

This Python web application Salary.py is a simple app for calculating an annual salary based on #hourly pay rate, hours worked per day, days worked per week, and holiday hours.
#
It uses the Flask framework to set up a basic web server and render HTML templates. The main route '/' will display the salary calculator page.

The calculator page is defined in the 'original_html' variable as a HTML string. It contains a form with input fields for hours per day, pay per hour, week days, and holiday hours. There is a Calculate button that calls the JavaScript function calculateSalary() when clicked. Below the button is a textarea field to display the final yearly salary result.

The calculateSalary() function is a javascrpt functiom that gets the values entered into the form fields, calculates the weekly hours (hours per day * week days), holiday pay (holiday hours * pay per hour), weekly pay (weekly hours * pay per hour), and total yearly pay (weekly pay * 52 weeks + holiday pay). It sets the salary textarea to a message showing the yearly pay result.

When the Calculate button is clicked, the JavaScript function will take the input values, run the calculations, and put the final salary number into the textarea. This allows the user to dynamically compute their estimated yearly salary based on their inputs.

The key logic is calculating weekly hours, holiday pay, weekly pay, and total yearly pay based on the input values. The output is the salary estimate displayed back to the user. The main purpose is to create an easy web interface for computing an estimated yearly salary from a few key inputs.
This Simple application shows how to combine the power of python and javascript to make a simple user friendly web application. There is room for improvement. 


I also attached a python template # dybamicHTML.py that is able to generate dynamic HTML5 pages. The template can be modified to produce an entirely different result. 
