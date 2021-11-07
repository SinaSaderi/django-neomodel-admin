django-neo4jadmin
===============

.. image:: https://i.ibb.co/RDG1Yk3/django-neomodel-admin.png
   :alt: neomodel-admin

This is a sample module allow you to use the neo4j_ graph database with Django admin interface.

.. _neo4j: https://www.neo4j.org

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
