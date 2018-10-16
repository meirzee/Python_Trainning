#!C:\\Users\\meirzee\\AppData\\Local\\Programs\\Python\\Python37\\python.exe
# use http://localhost/cgi-bin/hellowWorld.py

print("Content-Type: text/html")
print()

print ("<html>")
print ("<title> This is a test site </title>")
print ("<body>")
print("<h1>First Form</h1>")
print ("<form action='action1.py' method='post'>")
print ("Name: <input type='text' name='name' size='25'>")
print ("Title: <input type='text' name='title' size='30'>")
print ("E-Mail: <input type='text' name='email' size='30'>")
print ("<input type='submit' value='submit'>")
print ("</form>")
print ("</body>")
print ("</html>")
