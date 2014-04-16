opencontrail-netns
==================

OpenContrail Linux network namespace provisioning

This package contains two scripts (netns-daemon-start, netns-daemon-stop) which are intended to be used as pre-start and post-stop scripts for applications started out of init.d.

The application itself should then be executed as:
```
ip netns exec ns-<daemon> /usr/bin/<daemon>
```

Example:
```
# daemon upstart configuration file

pre-start script
  netns-daemon-start --network=<virtual-network> daemon
end script

post-stop script
  netns-deamon-start daemon
end script

script
  ip netns exec ns-daemon /usr/bin/daemon
end script
```
