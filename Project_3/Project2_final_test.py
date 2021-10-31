# -*- coding: utf-8 -*-
"""
Created on Sun Oct 31 11:42:05 2021

@author: bobby
"""

import unittest
import Project2_final_v2 as proj


class TestProject2(unittest.TestCase):
    
    def test_tweets(self):
        result = proj.tweets(200,'#BTC')
        self.assertEqual(len(result), 200)
        
        result = proj.tweets(100,'#BTC')
        self.assertEqual(len(result), 100)
        
        result = proj.tweets(200,'#ETH')
        self.assertEqual(len(result), 200)
        
        result = proj.tweets(100,'#ETH')
        self.assertEqual(len(result), 100)

    

    def test_google(self):
        text_list = ['It is a beautiful day', 'I hate you', 'can we go get some pizza?']
        text_length = len(text_list)
        
        result = proj.google(text_list)
        
        # checks to make sure text list and sentimore score lines up
        self.assertEqual(len(result), text_length) 
        
        # checks to make sure sentimore scores are between -1 and 1
        self.assertLessEqual(max(result),1)
        self.assertGreaterEqual(min(result),-1)
        
        
        
        
        
if __name__ == '__main__':
    unittest.main()