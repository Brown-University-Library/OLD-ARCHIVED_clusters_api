### Purpose

This flask app provides a lightweight api for the library cluster computers.

### Notes

- This app assumes a project structure like:

        some_enclosing_directory/
            clusters_api/
                config/
                clusters_app.py
            env_clusters/


- This app ssumes an entry in our existing apache .conf file like:

        <Directory /path/to/clusters_api>
          Order allow,deny
          Allow from all
        </Directory>
        WSGIScriptAlias /path/to/clusters_api/config/wsgi.py

---
