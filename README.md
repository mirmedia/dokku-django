Django plugin for Dokku
=======================

Dokku commands for Django projects

Installation
------------
```
cd /var/lib/dokku/plugins
sudo git clone https://github.com/mirmedia/dokku-django.git django
sudo dokku plugins-install
```

Commands
--------
```
$ dokku help
     django:collect <app>                   Collect the static files for <app>.
     django:rebuild_index <app>             Run the rebuild_index command for <app>.
     django:serve <app> <folder>            Serve the files in <folder> with nginx for <app>.
     django:syncdb <app>                    Run the syncdb command for <app>.
```
