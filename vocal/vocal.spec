%define date 160308
%define rev a5b01d25

Summary:        Vocal Podcatcher
Name:           vocal
Version: 2.0~git%{date}~%{rev}
Release: 1%{?dist}
License:        GPLv3
URL:            http://launchpad.net/vocal

Source0:        %{name}-%{version}.tar.gz
Source1:        %{name}.conf

Patch0:         00-webkitdeps.patch

BuildRequires:  cmake pkgconfig
BuildRequires:  vala gettext
BuildRequires:  desktop-file-utils
BuildRequires:  libappstream-glib

BuildRequires:  pkgconfig(clutter-gtk-1.0)
BuildRequires:  pkgconfig(gee-0.8)
BuildRequires:  pkgconfig(glib-2.0)
BuildRequires:  pkgconfig(granite)
BuildRequires:  pkgconfig(gstreamer-1.0)
BuildRequires:  pkgconfig(gstreamer-pbutils-1.0)
BuildRequires:  pkgconfig(gtk+-3.0)
BuildRequires:  pkgconfig(json-glib-1.0)
BuildRequires:  pkgconfig(libnotify)
BuildRequires:  pkgconfig(libsoup-2.4)
BuildRequires:  pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(sqlite3)
BuildRequires:  pkgconfig(webkit2gtk-4.0)

Requires:       hicolor-icon-theme


%description
Vocal is a podcatcher designed for elementaryOS.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install

mv %{buildroot}/%{_datadir}/locale-langpack %{buildroot}/%{_datadir}/locale

%find_lang vocal


%check
desktop-file-validate %{buildroot}/%{_datadir}/applications/vocal.desktop

# appstream-util validate-relax --nonet %{buildroot}/%{_datadir}/appdata/*.appdata.xml

#FAILED:
#? attribute-invalid     : <release> timestamp should be a UNIX time
#Validation of files failed


%clean
rm -rf %{buildroot}


%post
/bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null || :

%postun
if [ $1 -eq 0 ] ; then
    /usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
fi

if [ $1 -eq 0 ] ; then
    /bin/touch --no-create %{_datadir}/icons/hicolor &>/dev/null
    /usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :
fi

%posttrans
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null || :
/usr/bin/gtk-update-icon-cache %{_datadir}/icons/hicolor &>/dev/null || :


%files -f vocal.lang
%{_bindir}/vocal

%{_datadir}/appdata/*
%{_datadir}/applications/vocal.desktop
%{_datadir}/glib-2.0/schemas/net.launchpad.vocal.gschema.xml
%{_datadir}/icons/hicolor/*/apps/vocal.svg
%{_datadir}/icons/hicolor/*/apps/vocal-symbolic.svg
%{_datadir}/vocal


%changelog
* Tue Mar 08 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160308~a5b01d25-1
- Update to new upstream snapshot.

* Mon Mar 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160307~8d302c97-1
- Update to new upstream snapshot.

* Tue Feb 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160223~45d9135e-1
- Update to new upstream snapshot.

* Thu Feb 18 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160218~f3b06e58-1
- Update to new upstream snapshot.

* Mon Feb 15 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160215~c43321eb-1
- Update to new upstream snapshot.

* Sun Feb 07 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160207~ae1f0d39-1
- Update to new upstream snapshot.

* Sat Jan 23 2016 Fabio Valentini <decathorpe@gmail.com> - 2.0~git160123~57c4e54b-1
- Update to 2.0 git snapshots.

* Sun Nov 22 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0-1
- Unretire vocal package. Downgrade to version 1.0. Git snapshots coming soon.

