from flask import Flask, render_template_string

app = Flask(__name__)

@app.route('/')
def index():
    original_html = """
    <!DOCTYPE html>
<html>
<head>
  <title>Salary Calculator</title>
</head>
<body>

  <form>
    <label for="hoursPerDay">Hours Per Day:</label><br>
    <input type="text" id="hoursPerDay" name="hoursPerDay"><br>

    <label for="payPerHour">Pay Per Hour:</label><br>
    <input type="text" id="payPerHour" name="payPerHour"><br>

    <label for="weekDays">Week Days:</label><br>
    <input type="text" id="weekDays" name="weekDays"><br>

    <label for="holidayHours">Holiday Hours:</label><br>
    <input type="text" id="holidayHours" name="holidayHours"><br>

    <input type="button" value="Calculate" onclick="calculateSalary()">
    
    <p></p>
    <label for="salary">Yearly Salary:</label><br>
    <textarea id="salary" name="salary"></textarea>

  </form>
  
  <script>
    function calculateSalary() {
      let hoursPerDay = document.getElementById("hoursPerDay").value;
      let payPerHour = document.getElementById("payPerHour").value;
      let weekDays = document.getElementById("weekDays").value;
      let holidayHours = document.getElementById("holidayHours").value;
      
      let weeklyHours = hoursPerDay * weekDays;
      let holidayPay = holidayHours * payPerHour;
      let weeklyPay = weeklyHours * payPerHour;
      let yearlyPay = weeklyPay * 52 + holidayPay;
      
      document.getElementById("salary").value =("Your yearly salary ="   + yearlyPay);
    }
  </script>

</body>
</html>
    """

    return render_template_string(original_html)

if __name__ == '__main__':
    app.run(debug=True)
