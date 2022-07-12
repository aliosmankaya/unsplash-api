<h1>Unsplash API</h1>

<img src="https://unsplash.com/blog/content/images/max/2560/1-vQ5EsgnJkANWb5fktHPwnw.jpeg" style="float:left; width:50%;">
<img src="https://i.imgur.com/p0Nufjn.jpg" style="width:50%;">

<h3>Contents</h3>
<ul>
    <li><b>/app</b> : API Configuration</li>
    <li>
        <b>/classes</b> : Class Configuration
        <ul>
            <li>photos</li>
            <li>random</li>
            <li>search</li>
            <li>unsplash</li>
        </ul>
    </li>
    <li>
        <b>/controller</b> : Controller for services
        <ul>
            <li>photos_controller</li>
            <li>random_controller</li>
            <li>search_controller</li>
        </ul>
    </li>
    <li>
        <b>/models</b> : Pydantic Data Validation
        <ul>
            <li>photos_model</li>
            <li>random_model</li>
            <li>search_model</li>
        </ul>
    </li>
    <li>
        <b>/services</b> : API Service Configuration
        <ul>
            <li>photos_service</li>
            <li>random_service</li>
            <li>search_service</li>
        </ul>
    </li>
</ul>

<li>Before using the Unsplash API, <a href="https://unsplash.com/developers">register</a> 
as a developer and get your access key. After that, use that key as your <i>client_id</i></li>

<h3>Installation</h3>
<pre>$ pip install requirements.txt</pre>

<h3>Usage</h3>
<pre>$ python main.py</pre>
<pre>0.0.0.0:8000/docs  # Open on browser</pre>
