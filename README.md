Sample Django & Selenium  based crawler
=======================================

How to use:
----------

just run:
```
./manage.py runserver
```
and start celery:
```
celery -A project worker -l info
```

that's all. Now you can add the blog in the admin panel,
choose it and select "Crawls the selected blog(s)" action.
The process will start.