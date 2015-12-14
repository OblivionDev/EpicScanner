#!/usr/bin/env python

#Right that's me done mate, I'm gonna create the repo, add this to it and send you the URL :)

### IDEA
## Scan set dirs (can use external app if need-be)
## XMLRPC fuzzer (Will need to get a sample request to fuzz or get the request in a file)

### Notes for Drupal
# /sites/all/{themes/, modules/}custom/
# /sites/default/files/
# CHANGELOG.txt, install.php, update.php, etc (need a full list of default files too)

# Are we doing a Drupal scanner specificly or are we just writing a fuzzer?
# Alright I'll add my shit to it later for what i need for tomorrow xD - Just ignore my notes ;D
#  Okay mantis ;)
import os
import commands
import urllib2
import re

debug = True

print " Welcome to the most EPIC scanner ever, written by masterminds (Mantis, Oblivion)\n" # 
target = raw_input('Enter your target: ') # http://example.com 
uri = raw_input('Enter the target URI: ') # /xmlrpc.php or whatever
print "NOTE: Every payload has to be on a newline!" # NOTE for dummies 
payload_file = raw_input('Enter the path to a payload file (or leave blank for default): ') 

if(len(payload_file)): # Check if it was passed in
    payload_file = './payloads/full.payloads.txt'

payloads = open(payload_file).read() # Todo: add error checking
url = target + uri

print "Looping payloads."

for i in payloads:
    print payloads[i] if debug else '' # Checking if payloads are ready to fire!
    
    request = urllib2.open(url, payloads[i]) # I believe that makes it a POST rather than a GET
    response = request.read()

    if(re.search('/.?('+payloads[i]+')/i', response)): # That'll do as a test I reckon? ehm don't think so, responses differ for reguests for example
        print " Vulnerability found at >  %s \n Response:\n %s " % (url, response) 
    else: 
        print "That's too bad! h4x0rb0t couldn't find any vulns * cries in a corner * \n" #haha i'm so creative 

print 'Finished :>'