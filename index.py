from http.server import HTTPServer, BaseHTTPRequestHandler



class Handler(BaseHTTPRequestHandler):
	def log_error(self,*a,**ka):
		print(self.path)



with HTTPServer(("localhost",8000),Handler) as httpd:
	print("Start")
	httpd.serve_forever()