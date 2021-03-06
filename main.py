#!/usr/bin/env python

### IDEA
## Scan set dirs (can use external app if need-be)
## XMLRPC fuzzer (Will need to get a sample request to fuzz or get the request in a file)

import inspect, os
import commands
import urllib2
import re
import argparse

parser = argparse.ArgumentParser(description='Welcome to the most EPIC scanner ever, written by masterminds (Mantis, Oblivion)')
parser.add_argument('--payload-file', type=str, help='The payload file (usually .xml)')
parser.add_argument('--fuzz-file', type=str, help='The file with the fuzz strings. Each fuzz item must be on a new line!')
parser.add_argument('--target', type=str, help='The target URL: http://example.com')
parser.add_argument('--target-uri', type=str, help='The XMLRPC endpoint: /xmlrpc.php')
args = parser.parse_args()

fuzz_file = args.fuzz_file
payload_file = args.payload_file
target = args.target
target_uri = args.target_uri

if(len(fuzz_file) == 0): # Check if it was passed in
    fuzz_file = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe()))) + '/payloads/full.payloads.txt'

fuzz_items = open(fuzz_file).readlines() 
url = target + target_uri

prefuzzed_request = ''
with open(payload_file, 'r') as payload:
    prefuzzed_request = payload.read()

# TODO:
## Need to add Sniper and BatteringRam options (Burp Intruder style) 
## Multi-threaded
for fuzz_item in fuzz_items:

    fuzzed_request = prefuzzed_request.replace('{{PAYLOAD}}', fuzz_item)
    request = urllib2.urlopen(url, fuzzed_request) # I believe that makes it a POST rather than a GET
    response = request.read()

    print response

print 'Finished :>'