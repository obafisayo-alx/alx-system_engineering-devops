#!/usr/bin/pup
# Install an especific version of flask (2.1.0)
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install flask==2.1.0',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/flask --version | grep "Flask 2.1.0"',
  require => Package['python3-pip'],
}
