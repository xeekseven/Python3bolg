#!/user/bin/env python3
# -*- coding: utf-8-*-

'url handlers'

import re,time,json,logging,hashlib,base64,asyncio

from WebKuangJia import get,post

from Model import User,Comment,Blog,next_id

@get('/')
async def index(request):
	summary='Lorem ipsum dolir sit amet,consectetur adipisicing elit,sed do eiusmod tempor incididunt ut labore et dolore magna aliqua'
	blogs=[
		Blog(id='1',name='Spring Blog',summary=summary,created_at=time.time()-120),
		Blog(id='2',name='Summery Blog',summary=summary,created_at=time.time()-3600),
		Blog(id='3',name='Automn Blog',summary=summary,created_at=time.time()-7200)
	]
	#users= await User.findAll()
	return {
		'__template__':'blogs.html',
		'blogs':blogs
	}