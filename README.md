### Overview

This [flask app][FLASK] provides a lightweight [api][API] for [library-cluster-computer availability][CLUSTER_API].

It accesses, on a fixed schedule, the official [CIS][CIS] [LabStats html page][LABSTATS] page (may require on-campus access or [VPN][VPN]). That html is parsed and the resulting json is saved to disk, where it is accessed by the flask app. (This way we don't hit the CIS data source too often.)

Note: I've checked with a CIS contact who confirmed that the 'calculated_available' number returned by the api, which is the sum of 'available' and 'offline', will more accurately reflect the availability a user would expect.

Contact: birkin_diana@brown.edu; Digital Library Technologies Programmer

##### Geek Notes

- utils.grabber_handler.Grabber.update_data() is triggered by a cron script

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

[API]: http://readwrite.com/2013/09/19/api-defined
[CIS]: https://it.brown.edu
[CLUSTER_API]: http://library.brown.edu/clusters_api/data/
[FLASK]: http://flask.pocoo.org
[LABSTATS]: http://labstats.cis.brown.edu/LabStats/public/public.aspx
[VPN]: https://it.brown.edu/services/type/virtual-private-network-vpn
