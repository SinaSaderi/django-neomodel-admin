django-neo4jadmin
===============

This is a sample module allow you to use the neo4j graph database with Django admin interface.

Installable App
---------------

This app can be installed and used in your django project by:

.. code-block:: bash

    $ pip install django_neomodel_admin


Edit your `settings.py` file to include `'receipts'` in the `INSTALLED_APPS`
listing.

.. code-block:: python

    INSTALLED_APPS = [
        ...

        'neomodel_admin',
    ]


Edit your project `urls.py` file to import the URLs:


.. code-block:: python

    url_patterns = [
        ...

        path('neoadmin/', include('neomodel_admin.urls')),
    ]
