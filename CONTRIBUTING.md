# Contributing to elementary packaging

## Packaging new software (simple method)

This involves about the same steps the automatic build
system does - just done manually, so the build system doesn't
have to be set up first.

### 0. Prerequisites

The following packages are needed for the steps below:

```
bzr / git
mock
rpmdevtools
```

After installing those, you will have to add yourself to the ```mock``` group
to be able to execute builds without root.

```
sudo usermod -a -G mock $USER
```

After logging out and back in, builds can be executed.

Additionally, if builds require other elementary packages, a specific mock
configuration has to be used, pointing to the existing COPR repository (an example
can be found inside the misc folder inside the repository).


### 1. Downloading repository

Download the bzr or git repository that will be packaged up,
for example:

```
bzr clone lp:switchboard-plug-display           # for bzr repo on launchpad
git clone https://github.com/vocalapp/vocal     # for git repo on github
```

### 2. Exporting sources to static tarball

This produces a reusable tarball that can be used for packaging
without problems. Executing these commands within the downloaded
repository will produce
*.tar.gz files:

```
bzr export ../switchboard-plug-display-0.1~rev10.tar.gz     # for bzr repo

git archive HEAD --prefix="vocal-2.0~git160709/" \\          # for git repo
    --output="../vocal-2.0~git160709.tar.gz"
```

### 3. Creating an RPM spec file (from template)

Using one of the already existing .spec files as template (choosing one that is
as similar to the needed .spec as possible), a new file is created and filled
with the information about the new package (using the same formatting of the
.spec file for readability and consistency).

The ```Source0:``` tag has to be set to the name of the tarball produced in step 2.
All other tags have to be adapted to the new software package (by looking them
up at the upstream homepage, for example).

Set the ```Version: ``` tag according to the upstream version and append
```~git****``` or ```~rev***``` as needed.

Set the ```Release: ``` tag to ```0%{dist}``` for now.


### 4. Finishing up package spec

When this is done, the ```BuildRequires: ``` tags of the template have to be
replaced by the actual ones. The required packages can often be determined by
reading the ```CMakeLists.txt``` file in the repository.

Using the ```pkgconfig()``` directive instead of referencing package names directly
is considered good practice, since package names may change in the future, while
pkgconfig identifiers are unique.

The ```%prep```, ```%build``` and ```%install``` sections of the spec should be
fine for most CMake projects. Otherwise, they may need some tweaks.

The ```%files``` sections have to be empty for now and will be filled later.


### 5. Creating an SRPM package

After creating the following directories,

```
~/rpmbuild
~/rpmbuild/SOURCES
~/rpmbuild/SPECS
```

move the tarball into the ```SOURCES``` directory and the .spec file into the SPECS
directory. Move the mock configuration file inside the rpmbuild directory for
easy access to it.

Then, within the ```SPECS``` directory, execute the following command

```
rpmbuild -bs *.spec
```

to produce an ```*.src.rpm``` file within the ```~/rpmbuild/SRPMS/``` directory.
If this command doesn't succeed, correct the indicated errors until it does.


### 6. Building the package locally

The following command will execute the build of the source package in a clean
environment:

```
mock -r ../fedora-23-x86_64-ele-nightly.cfg $SRPM_NAME
```

There are several reasons why the build may not succeed:

- missing development packages (indicated by CMake or automake).
  fix by adding the missing requirements to the spec and regenerating the src.rpm file.
- missing build tools (also indicated by CMake or automake). add them to
  BuildRequires, too.
- compilation failures (not much can be done about those, except maybe notifying
  upstream)

If the build does succeed, it will print a list of installed but unpackaged files.
Add those to the appropriate ```%files``` section in the spec file, regenerate the
source package and repeat until everything finishes successfully.

Examples of the provided macros can be found in existing spec files. Also, examples
of where to put development files etc. are also in the existing specs.


### 7. Misc spec improvements

There are several things one can add that make a .spec better.

- consistent formatting (spaces, no tabs, consistent indentation, etc.). see the
  already packaged software for inspiration
- check for common spec and package errors with rpmlint
- .desktop file validation for packages including a desktop file
- .appdata.xml file validation for packages including an appdata file
- scriptlets for regenerating icon cache (if icons are shipped)
- scriptlets for updating the gsettings database (if gsettings schemas are shipped)
- etc.

Examples of those can be found in most of the already packaged GUI applications.


### 8. (Optional) Write kentauros configuration file

Write a kentauros configuration file for the new package, that can be part of the
pull request along with the new spec file. Examples of the settings syntax,
layout and required fields are the already existing .conf files.


### 9. Submit pull request

spec + conf + request = <3

