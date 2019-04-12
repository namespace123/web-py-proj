#!/usr/bin/env python
#-*- coding: utf-8 -*-

urls = (
    '/index', 'index',
    '/article', 'article',
    '/blog/\d+', 'blog',
    '/(.*)', 'hello',
)