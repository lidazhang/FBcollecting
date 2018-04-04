#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 27 21:48:54 2018

@author: zhanglida
"""
import facebook
import json
#from urllib import request


def collectComment(feeds,g):
    hsbc = {}
    hsbc['post'] = []
    post_data = feeds['data']
    for post in post_data:
        post_id = post['id']
        post_create_time = post['created_time']
        try:
            post_message = post['message']
        except:
            post_message = None
        try:
            post_story = post['story']
        except:
            post_story = None
        hsbc['post'].append({
                'post_id':post_id,
                'post_create_time':post_create_time,
                'post_message':post_message,
                'post_story':post_story
                })
    
    hsbc['comment'] = []
    
    for post in hsbc['post']:
        post_id = post['post_id']
        feed = g.get_connections(post_id,'comments')
        comment = []
        for data in feed['data']:
            comment_id = data['id']
            comment_message = data['message']
            comment_create_time = data['created_time']
            comment.append({
                    'comment_id':comment_id,
                    'comment_message':comment_message,
                    'comment_create_time':comment_create_time
                    })

        hsbc['comment'].append({
                'post_id':post_id,
                'data':comment
                })
    #print hsbc
    return hsbc


def main(ACCESS_TOKEN):
    g= facebook.GraphAPI(ACCESS_TOKEN)
    feeds = g.get_connections('me','feed')
    hsbc = collectComment(feeds,g)


    with open('lidadata.json', 'w') as outfile:  
        json.dump(hsbc, outfile)



if __name__ == '__main__':
    ACCESS_TOKEN = raw_input("Please enter your access_token: ")
    main(ACCESS_TOKEN)
    # get your token from https://developers.facebook.com
    
    
    
    
