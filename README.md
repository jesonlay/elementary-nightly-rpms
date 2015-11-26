# elementary-rpms
 repository to keep track of packaging of (nightly snapshots of) elementaryOS components and applications for fedora.

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
