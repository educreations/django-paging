About
=====

A simple and efficient paginator.

Jinja2
------

Jinja2_ is supported via Coffin_::

	{% with paginate(request, my_queryset) as results %}
	  {{ results.paging }}
	  {% for result in results.objects %}
	    {{ result }}
	  {% endfor %}
	  {{ results.paging }}
	{% endwith %}


Jinja2 is also supported via Jingo_::

	{% set paginate(request, my_queryset, per_page=25, endless=False, range_gap=3) as results %}
	  {# results.paging is not implemented for Jingo, make your own template... #}
	  {% for result in results.paginator.objects %}
	    {{ result }}
	  {% endfor %}
	{% endwith %}


.. _Jinja2: http://jinja.pocoo.org/2/
.. _Coffin: https://github.com/coffin/coffin/
.. _Jingo: https://github.com/jbalogh/jingo

Django
------

Django templatetags require django-templatetag-sugar_::

	{% load paging_extras %}
	
	{% paginate my_queryset from request as results %}
	{{ results.paging }}
	{% for result in results.objects %}
	  {{ result }}
	{% endfor %}
	{{ results.paging }}

.. _django-templatetag-sugar: https://github.com/alex/django-templatetag-sugar