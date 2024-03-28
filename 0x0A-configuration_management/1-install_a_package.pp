#!/usr/bin/pup
# Installs a specific version of flask (2.1.0) from pip3.

package {'Flask':
  ensure   => '2.1.0',
  provider => 'pip3'
}
