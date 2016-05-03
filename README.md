# elementary-rpms
I use this repository to keep track of files related to packaging / building nightly snapshots of elementaryOS / pantheon desktop components and applications for fedora.

## USAGE

- Get my build tool (kentauros) from copr or github
- configure copr for your copr account if you want to upload
- change settings in the configs as you wish (e.g. change copr repository name)
- run:

```sh
ktr --verbose chain --all
```

- or, if you want to force actions on all packages:

```sh
ktr --verbose chain --force --all
```

