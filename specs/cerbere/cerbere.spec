Name:           cerbere
Summary:        Pantheon session watchdog
Version:        0.2.2+rev%{rev}
Release:        1%{?dist}
License:        GPLv2
URL:            https://launchpad.net/cerbere

# The tarball is generated from a checkout of the specified branch and
# by executing 'bzr export' and has the usual format
# ('%{name}-%{version}.tar.gz'), where %{version} contains the upstream
# version number with a '+bzr%{rev}' suffix specifying the bzr revision.
Source0:        %{name}-%{version}.tar.gz

Source2:        %{name}.conf

BuildRequires:  cmake
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  vala >= 0.16
BuildRequires:  vala-tools

BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0) >= 2.32.0

Recommends:     gala
Recommends:     plank
Recommends:     wingpanel


%description
Cerbere is a sort of watchdog designed for Pantheon. It monitors a
predefined list of processes (configurable through dconf) and relaunches
them if they end. This is helpful to keep the panel, dock, and wallpaper
running, even if they crash or are killed by another process.

Designed for elementary OS.


%prep
%autosetup


%build
mkdir build && pushd build
%cmake ..
%make_build
popd


%install
pushd build
%make_install
popd


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/cerbere.desktop


%files
%{_bindir}/cerbere

%{_datadir}/applications/cerbere.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.cerbere.gschema.xml


%changelog
* Sun Jul 02 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev59-1
- Update to latest snapshot.

* Sat Jun 17 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev58-1
- Update to latest snapshot.

* Wed Apr 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev57-1
- Update to latest snapshot.

* Tue Apr 25 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev56-1
- Update to latest snapshot.

* Wed Apr 12 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev55-1
- Update to latest snapshot.

* Wed Feb 15 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev53-1
- Update to latest snapshot.

* Thu Jan 26 2017 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev52-3
- Sync with fedora packaging.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev52-2
- Add missing BR: desktop-file-utils.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.2+rev52-1
- Update to version 0.2.2.

* Wed Sep 28 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev52-2
- Spec file cosmetics.

* Wed Aug 10 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev52-1
- Update to latest snapshot.

* Sun Aug 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev51-5
- Update for packaging changes.

* Wed Jul 06 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev51-4
- Update for packaging changes.

* Mon May 30 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev51-3
- Update for packaging changes.

* Sun May 29 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev51-2
- Update for packaging changes.

* Sun May 08 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev51-1
- Update to latest snapshot.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev50-2
- Update for packaging changes.

* Sat May 07 2016 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev50-1
- Initial package.


