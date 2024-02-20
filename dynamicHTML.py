from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    # Original HTML template
    original_html = """
    <!DOCTYPE html>
<html>
<head>
  <title>Salary Form</title>
</head>
<body>

  <form>
    <label for="name">hoursPerDay</label><br>
    <input type="text" id="name" name="name"><br>

    <label for="email">payPerHour:</label><br>
    <input type="email" id="email" name="email"><br>

    <label for="phone">weekDays:</label><br> 
    <input type="tel" id="phone" name="phone"><br>

    <label for="phone">holidayHours:</label><br> 
    <input type="tel" id="phone" name="phone"><br>


    <input type="submit" value="Submit">
    <p></p>
    <label for="phone">Result:</label><br> 
    <textarea id="message" name="message"></textarea><br>

  </form>

</body>
</html>
    """
    
    # Modify appearance of <p> tags
    modified_html = original_html.replace('<p>', '<p style="color: red; font-size: 18px; font-weight: bold;">')

    return render_template_string(modified_html)

if __name__ == '__main__':
    app.run(debug=True)
