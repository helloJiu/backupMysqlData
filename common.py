import ConfigParser
import subprocess
import traceback
from optparse import OptionParser


def get_opt_arg():
    parser = OptionParser(usage='usage: %prog [options]', \
                          version='version: %prog 1.0')
    parser.add_option('-c', '--config-file', dest='config_file', \
                      default='./app.conf', action='store', type='string', \
                      metavar='CFILE', help='read config file from CFILE' \
                      )
    (options, args) = parser.parse_args()
    if len(args) != 0:
        parser.error('incorrect number of arguments')
    return options


def get_config(config_file_name):
    # Parse config file
    try:
        cf = ConfigParser.ConfigParser()
        cf.read(config_file_name)
        secs = cf.sections()
        if secs == []:
            print 'ERROR SECTION IN CONFIG FILE'

        var_dict = {}
        for sec in secs:
            var_dict[sec] = {}
            items = cf.items(sec)
            for item in items:
                var_dict[sec][item[0]] = item[1]

        return var_dict
    except Exception:
        e = traceback.format_exc()
        print 'parse arguments exception!\n%s' % e


def call_system_command(cmd):
    process = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    (stdout, stderr) = process.communicate()
    return stdout