%define rev 307

Summary: Vocal Podcatcher
Name: vocal
Version: 1.0~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/vocal

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext
BuildRequires: desktop-file-utils
BuildRequires: libappstream-glib

BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gstreamer-1.0)
BuildRequires: pkgconfig(gstreamer-pbutils-1.0)
BuildRequires: pkgconfig(gtk+-3.0)
BuildRequires: pkgconfig(libnotify)
BuildRequires: pkgconfig(sqlite3)


Requires: hicolor-icon-theme


%description
Vocal is a podcatcher designed for elementaryOS.


%prep
%setup -q


%build
%cmake


%install
make install DESTDIR=$RPM_BUILD_ROOT

mv $RPM_BUILD_ROOT/%{_datadir}/locale-langpack $RPM_BUILD_ROOT/%{_datadir}/locale

mv $RPM_BUILD_ROOT/%{_datadir}/appdata/vocal.desktop.appdata.xml \
	$RPM_BUILD_ROOT/%{_datadir}/appdata/vocal.desktop.appdata.xml.old

mv $RPM_BUILD_ROOT/%{_datadir}/appdata/vocal.desktop.appdata.xml.old/vocal.desktop.appdata.xml	\
	$RPM_BUILD_ROOT/%{_datadir}/appdata/vocal.desktop.appdata.xml

rmdir $RPM_BUILD_ROOT/%{_datadir}/appdata/vocal.desktop.appdata.xml.old

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/vocal.desktop

# appstream-util validate-relax --nonet $RPM_BUILD_ROOT/%{_datadir}/appdata/vocal.desktop.appdata.xml

%find_lang vocal


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f vocal.lang
%{_bindir}/vocal

%{_datadir}/appdata/vocal.desktop.appdata.xml
%{_datadir}/applications/vocal.desktop

%{_datadir}/glib-2.0/schemas/net.launchpad.vocal.gschema.xml

%{_datadir}/icons/hicolor/22x22/apps/vocal.svg
%{_datadir}/icons/hicolor/24x24/apps/vocal.svg
%{_datadir}/icons/hicolor/32x32/apps/vocal.svg
%{_datadir}/icons/hicolor/48x48/apps/vocal.svg
%{_datadir}/icons/hicolor/64x64/apps/vocal.svg
%{_datadir}/icons/hicolor/128x128/apps/vocal.svg

%{_datadir}/vocal


%changelog
* Mon Oct 19 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0~rev307-1
- Update to new upstream snapshot.

* Sun Oct 18 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0~rev306-1
- Update to new upstream snapshot.

* Fri Oct 16 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0~rev305-1
- Update to new upstream snapshot.

* Sat Oct 10 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0~rev304-1
- Update to new upstream snapshot.

* Thu Oct 08 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0~rev303-1
- Update to new upstream snapshot.

* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 1.0~rev301-2
- rebuild trigger for granite soname bump

* Mon Aug 17 2015 Fabio Valentini - 1.0~rev301-1
- Update to new upstream snapshot.

