#!/usr/bin/pup
# Install a specific version of flask (2.1.0) using puppet
package { 'flask':
  ensure   => '2.1.0',
  provider => 'pip3',
}

package { 'werkzeug':
  ensure   => '2.1.1',
  provider => 'pip3',
}
