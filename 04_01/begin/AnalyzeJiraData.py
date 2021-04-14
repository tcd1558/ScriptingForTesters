import requests
import json

# Due to privacy concerns this can not be exposed.
url= 'http://jira.<company_name>/rest/api/latest/search?jqp=reporter=<user_name>'
# response is not going to set, because the url is fake.
# response = requests.get(url)

# use dummy data instead:
json_data = open('jiraJsonData.json').read()
data = json.loads(json_data)

status_counts = {}

for project in data['projects']:
    for issue in project['issues']:
        status = issue['status']
        # print(project['name'], ':', status)
        if not status in status_counts.keys():
            status_counts[status] = 1
        else:
            status_counts[status] = status_counts[status] + 1
print(status_counts)

# https://developers.google.com/chart/interactive/docs/gallery/piechart
from string import Template
html_string = Template("""<html>
  <head>
    <script type="text/javascript" src="https://www.gstatic.com/charts/loader.js"></script>
    <script type="text/javascript">
      google.charts.load('current', {'packages':['corechart']});
      google.charts.setOnLoadCallback(drawChart);

      function drawChart() {

        var data = google.visualization.arrayToDataTable([
          $labels,
          $data
        ]);

        var options = {
          title: '$title'
        };

        var chart = new google.visualization.PieChart(document.getElementById('piechart'));

        chart.draw(data, options);
      }
    </script>
  </head>
  <body>
    <div id="piechart" style="width: 900px; height: 500px;"></div>
  </body>
</html>""")

#my_title='My Daily Activities'
my_title='Issues hy Status'
#my_labels="['Task', 'Hours per Day']"
my_labels="['Status', 'Number of Issues']"

chart_data_str = ''
for status_count in status_counts.keys():
    print(status_count, status_counts[status_count])
    chart_data_str += "['%s', %s],\n" %(status_count, status_counts[status_count])

print(chart_data_str)

completed_html = html_string.substitute(title=my_title, labels=my_labels, data=chart_data_str)

with open('AnalyzeJiraData.html','w') as f:
    f.write(completed_html)