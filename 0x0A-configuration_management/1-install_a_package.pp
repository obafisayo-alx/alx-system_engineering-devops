#!/usr/bin/pup
# Install a specific version of flask (2.1.0) using puppet
package { 'python3-pip':
  ensure => installed,
}

exec { 'install_flask':
  command => '/usr/bin/pip3 install Flask==2.1.0 Werkzeug==2.1.1',
  path    => ['/usr/bin', '/bin'],
  unless  => '/usr/bin/flask --version | grep "Flask 2.1.0"',
  require => Package['python3-pip'],
}
