from http.server import HTTPServer, BaseHTTPRequestHandler
content = """
<html>
	<head>
		<title>TOP SOFTWARE COMPANIES</title>
	</head>
	<body bgcolor="violet">
	<table border="3" cellspacing="4" align="center">
	<caption>TOP FIVE REVENUE GENERATING SOFTWARE COMPANIES </caption>		
        <tr>
		<th>RANK</th>
		<th>COMPANY NAME</th>
		<th>SALES</th>
                <th>NATIONALITY</th>
	</tr>
		<tr>
			<td>1</td>
			<td>MICROSOFT</td>
			<td>57.9</td>
			<td>USA</td>
		</tr>

		<tr>
			<td>2</td>
			<td>ORACLE</td>
			<td>21.0</td>
			<td>USA</td>

		</tr>

		<tr>
                        
                        <td>3</td>
			<td>SAP</td>
			<td>16.1</td>
			<td>GERMANY</td>

		</tr>
                
                <tr>
                        
                        <td>4</td>
			<td>COMPUTER ASSOSIATES</td>
			<td>4.2</td>
			<td>USA</td>

		</tr>
                
                <tr>
                        
                        <td>5</td>
			<td>ADOBE</td>
			<td>3.4</td>
			<td>USA</td>

		</tr>

                
	</table>
	</body>
</html>
"""
class myhandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print("request received")
        self.send_response(200)
        self.send_header('content-type', 'text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write(content.encode())
server_address = ('',8000)
httpd = HTTPServer(server_address,myhandler)
print("my webserver is running...")
httpd.serve_forever()