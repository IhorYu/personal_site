<h1>Personal Site</h1>
<p>This is a Flask application that displays information about the author, their projects, skills, certifications, and contact information.</p>

<h2>Getting Started</h2>
<p>To get the app up and running on your local machine, follow these steps:</p>
<ol>
  <li>Clone the repository to your local machine:
  <pre>
git clone https://github.com/IhorYu/personal_site.git
</pre></li>
  <li>Navigate to the directory where you cloned the repository:
  <pre>
cd personal_site
</pre></li>
  <li>Create a virtual environment and activate it (optional):
  <pre>
python3 -m venv venv
source venv/bin/activate
</pre></li>
  <li>Run the application:
  <pre>
flask run
</pre></li>
</ol>
<p>The app should now be running at http://127.0.0.1:5000/.</p>

<h2>Customizing the Site</h2>
<p>To customize the content of the site, you can modify the following files:</p>
<ul>
  <li>templates/index.html: This is the main template for the site. It includes blocks for the author's name, bio, skills, projects, certifications, and contact information.</li>
  <li>static/img: This directory contains the images for the site. You can replace these with your own images.</li>
</ul>

<h2>Deployment</h2>
<p>To deploy the app to a production server, you can follow these steps:</p>
<ol>
  <li>Build the production version of the app:
  <pre>
flask run
</pre></li>
  <li>Run the app:
  <pre>
flask run --host=0.0.0.0
</pre></li>
</ol>
<p>The app should now be running in production mode and be accessible to users.</p>

<h2>Credits</h2>
<p>This application was developed by <a href="https://github.com/IhorYu">Ihor Yu</a>.</p>
