# Script to convert the output of tuya-local-key to a devices.conf file for tuya-myqq
# 
# copyright Mark McIntyre, 2026

import argparse

if __name__ == '__main__':

    arg_parser = argparse.ArgumentParser(description='Convert device data from tuya-local-key to tuya-mqtt format')
    arg_parser.add_argument('-i', '--srcfile', metavar='SRCFILE', type=str, help='source file, default device_data.txt', default='device_data.txt')
    arg_parser.add_argument('-o', '--outfile', metavar='DESTFILE', type=str, help='output file, default devices.conf', default='devices.conf')
    cml_args = arg_parser.parse_args()

    print(f'reading from {cml_args.srcfile}')

    rawdata = open(cml_args.srcfile, 'r').readlines()
    devname = None
    devid = None
    localkey = None
    outdata = '[\n'    
    for li in rawdata:
        if '      name'  in li:
           devname = li.split(':')[1].strip()
        if '      id'  in li:
           devid = li.split(':')[1].strip()
        if '      local_key'  in li:
           localkey = li.split(':')[1].strip()
        if devname and devid and localkey:
            devstr = "  {\n    name: '" + devname + "',\n    id: '" + devid + "'," + f'\n    key: "{localkey}"\n' + '  },\n'
            outdata = outdata + devstr
            devname = None
            devid = None
            localkey = None
    outdata += ']\n'
    print(f'writing to {cml_args.outfile}')
    open(cml_args.outfile, 'w').write(outdata)
