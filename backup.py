from common import *

option = get_opt_arg()
config = get_config(option.config_file)

mysql_config = config['mysql']
sql = 'show databases'
cmd = 'mysql -h%s -P%s -u%s -p%s -e"%s"' % (mysql_config['host'], mysql_config['port'], mysql_config['username'], \
      mysql_config['password'], sql)
print call_system_command(cmd)
