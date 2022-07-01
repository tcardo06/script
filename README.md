# script
Build a monitoring tool in the form of a Python script in order to check the proper functioning of a system or service.
The objective is to carry out a supervision (monitoring of computer systems) to automatically send alerts to administrators.

We want to query the metrics available on the supervised system at regular intervals in order to know the occupancy status of storage spaces, CPU utilization rate, memory utilization rate and network interface utilization rate.

The script will send this data to a database (temporal data base) in our case, InfluxDB.

The stored data will be used in dashboards built with a tool specialized in the presentation of data, in our case Grafana.

Getting Started:
  - Clone the project: https://github.com/tcardo06/script.git
  - Install Python, Grafana, InfluxDB and Psutil according to your operating system.
  - Open the project and write in the terminal of your directory project the following commande: 
      `python3 administration.py -i 4` (python or python3 depending on your installed version)
      -i being the interval of seconds at which the data is sent to your database (here 4 for exemple)
  - You can visualize your data on Grafana in the form of a graph (see images in exemple).

Trello link:
https://trello.com/b/6QMdi7Dn/scripting-admin

![alt text](file:///Users/thomascardoso/Desktop/Capture%20d%E2%80%99e%CC%81cran%202022-07-01%20a%CC%80%2014.13.20.png)
![alt text](file:///Users/thomascardoso/Desktop/Capture%20d%E2%80%99e%CC%81cran%202022-07-01%20a%CC%80%2014.12.53.png)