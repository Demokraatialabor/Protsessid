#!/usr/bin/python   
import json
from pprint import pprint
import re

def no_deploy():
    json_location = '/media/psf/Home/Documents/isiklik/laura_arengukavad/pdfs.json'
    with open(json_location, 'r') as myfile:
        data = myfile.read()
    data2 = '[' + data.replace('}\n{', '},{') + ']'
    laura = json.loads(data2)
    clean_data = []
    for l in laura:
        if len(l['annotations']) > 0:
            clean_data.append(l)
    print 'After data cleaning there are', len(clean_data), 'documents left'
    
    legends_used = {0:set(), 1:set()}
    for i, l in enumerate(clean_data):
        # print
        # print i, 'keys:', l.keys()
        print
        print 'Author:', l['author']
        print 'Description:', l['description']
        print 'Originalname', l['originalname']
        # print
        # print 'Possible annotation types:'
        legends = {}
        
        with open('types.txt', 'w') as myfile:
            for j in l['legends']:
                legends[j['_id']['$oid']] = j['name']
                line = j['_id']['$oid'] + '\t' + j['name'] + '\n'
                myfile.write(line.encode('utf8'))
            print 'types written to file types.txt'
        
        with open('file' + str(i) + '.txt', 'w') as myfile:
            for j, a in enumerate(l['annotations']):
                if a['type'] in legends.keys():
                    # print str(j) + ' - ' + legends[a['type']] + ', Author: ' + a['author']
                    line = a['type'] + '\t' + legends[a['type']] + '\t' + a['content']['text'] + '\t' + a['_id']['$oid'] + '\n'
                    myfile.write(line.encode('utf8'))
                    legends_used[i].add(a['type'])
            # else:
                # print str(j) + ' - ' + 'type_missing' + ', Author: ' + a['author']
            # print a['content']['text']
            
    print 
    print 'Annotation types used in both documents:'
    for k in legends_used[i].intersection(legends_used[i]):
        print legends[k]
    
if __name__ == '__main__':
    no_deploy()
