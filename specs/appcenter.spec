Summary:        Get apps for elementary OS
Name:           appcenter
Version:        0.1.1+rev%{rev}
Release:        1%{?dist}
License:        GPLv3
URL:            https://launchpad.net/appcenter

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

# Upgrades AppStream requirement to 0.10.0, see https://bugs.launchpad.net/appcenter/+bug/1626398
# From https://code.launchpad.net/~tintou/appcenter/appstream-0.10/+merge/307131/+preview-diff/749501/+files/preview.diff
Patch0:         00-appcenter-0.1.1-appstream-0.10.0-support.patch

BuildRequires:  cmake
BuildRequires:  cmake-elementary
BuildRequires:  desktop-file-utils
BuildRequires:  gettext
BuildRequires:  intltool
BuildRequires:  libappstream-glib
BuildRequires:  pkgconfig
BuildRequires:  vala >= 0.26

BuildRequires:  appstream-vala

%if 0%{?fedora} >= 25
BuildRequires:  pkgconfig(appstream) >= 0.10.0
%else
BuildRequires:  pkgconfig(appstream) >= 0.9.0
%endif
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(gobject-introspection-1.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gthread-2.0)
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.10
BuildRequires:  pkgconfig(packagekit-glib2)

Requires:       PackageKit


%description
Get apps for elementary OS.

AppCenter is a native Gtk+ app store built on AppStream and Packagekit.


%prep
%setup -q
%if 0%{?fedora} >= 25
%patch0 -b .appstream-0.10.0
%endif

%build
%cmake
%make_build


%install
%make_install
%find_lang appcenter


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/*.desktop
appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml


%clean
rm -rf %{buildroot}


%if %{?fedora} < 25
%post
/usr/bin/update-desktop-database &> /dev/null || :

%postun
/usr/bin/update-desktop-database &> /dev/null || :
%endif


%files -f appcenter.lang
%doc AUTHORS
%license COPYING

%{_bindir}/appcenter

%{_datadir}/appdata/appcenter.appdata.xml
%{_datadir}/applications/org.pantheon.appcenter.desktop
%{_datadir}/applications/org.pantheon.appcenter-daemon.desktop
%{_datadir}/glib-2.0/schemas/org.pantheon.appcenter.gschema.xml


%changelog
* Fri Oct 21 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev325-1
- Update to latest snapshot.

* Mon Oct 17 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev324-1
- Update to latest snapshot.

* Sun Oct 16 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev323-1
- Update to latest snapshot.

* Sat Oct 15 2016 Fabio Valentini <decathorpe@gmail.com> - 0.1.1+rev322-1
- Update to version 0.1.1.


