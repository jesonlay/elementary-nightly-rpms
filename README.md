# elementary-rpms
a simple build system for RPM packages of (nightly snapshots of) elementaryOS components and applications

## USAGE

- Get my build tool (builpy) from copr or github
- configure copr for your copr account if you want to upload
- run:

```sh
builpy upload --pkgfile=pkglist
```

- or, if you want to force all packages being built:

```sh
builpy upload --force --pkgfile=pkglist
```
