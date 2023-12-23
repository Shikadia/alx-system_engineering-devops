# Execute a command to kill a process named 'killmenow' using Puppet

exec { 'pkill killmenow':
  command => '/usr/bin/pkill -f /killmenow'
}
