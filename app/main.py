"""
Flask Web Application for GCP Automated Deployment

A simple Flask-based web application that serves a welcome page.
Designed to demonstrate containerized Python application deployment on Google Cloud Platform.
"""

from flask import Flask

# Initialize Flask application
app = Flask(__name__)

def page(message):
    """
    Generate HTML page content with centered message display.
    
    Args:
        message (str): Message text to display on the page
        
    Returns:
        str: HTML page as a string
    """
    html = """
        <html>
        <head lang> 
            <meta charset="utf-8">
            <title>Index</title>
        </head>
        <body>
            <div style='font-size:60px;'>
            <center>
                {0}<br>
            </center>
            </div>
        </body>
        </html>""".format(message)
    return html

@app.route('/')
def get_page():
    """
    Route handler for the root path (/).
    
    Returns:
        str: HTML page with welcome message
    """
    message = "Hello CGI!!! Welcome to the world of DevOps :)"
    return page(message)

if __name__ == '__main__':
    # Run Flask development server
    # Listens on all network interfaces (0.0.0.0) on port 8080
    app.run(host='0.0.0.0', port=8080)
