#!/usr/bin/python
import os
import urllib2
import json
import platform


urldata = urllib2.urlopen("http://api.piyasa.com/json/?kaynak=doviz_guncel_serb")
rates = json.load(urldata)

print "Content-Type: text/html"
print
print """\
<!DOCTYPE html>
<html lang="en">
<head>  <meta charset="utf-8">
  <title>Exchange Rates</title>
  <meta name="viewport" content="width=device-width,initial-scale=1">
  <link rel="stylesheet" href="//koding.com/hello/css/style.css">
  
  <link href='//fonts.googleapis.com/css?family=Open+Sans:300italic,400italic,600italic,700italic,800italic,400,300,600,700,800' rel='stylesheet' type='text/css'>
</head>
<body class="python">
  <div id="container">
    <div id="main" role="main"  class="hellobox" >
<header><a href="http://koding.com">Exchange Rates</a></header>
    <h1>Exchange Rates</h1>
    <h2>From Python 
    """
print platform.python_version()
print """\
  </h2> </div>

<footer>
<h4>Exchange rates for currencies</h4> 
<p>Look up the table:</p>
<pre>"""



print "<center><table border="+"1"+ " cellpadding="+"5>" 

print "<tr>"+"<th>FOEX</th>"+"<th>BUY</th>"+"<th>SELL</th>"+"<th>CHANGE</th>"+"<th>TIME</th>"+"</tr>"

for i in rates:    
    textColor = ""
    if float(i['change']) > 0:
        textColor = "\"Green\""
    elif float(i['change']) < 0:
        textColor = "\"Red\""
    else:
        textColor = "\"Yellow\""
    
    print "<tr><td>" + i['foex']+ "</td> <td>"  +i['buy']+"</td> <td>" +i['sell']+"</td> <td><font color="+textColor+">"+i['change'] +"</font></td><td>"+i['time'] + "</td></tr>"

print "</table></center>"

print """\
</pre>
</footer>
</div> 
</body>
</html>
"""
