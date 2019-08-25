# -*- coding: utf-8 -*-

from django.shortcuts import reverse


def test_main_page(client, main_heading):
    """This test ensures that main page works."""
    response = client.get('/')

    assert response.status_code == 200
    assert main_heading in str(response.content)


def test_hello_page(client, main_heading):
    """This test ensures that hello page works."""
    response = client.get(reverse('main:hello'))

    assert response.status_code == 200
    assert main_heading in str(response.content)
