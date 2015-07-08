%define rev 229

Summary: Stylish top panel that holds indicators and spawns an application launcher
Name: wingpanel
Version: 0.3.0.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/wingpanel

Source0: %{name}-%{version}.tar.gz

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

BuildRequires: desktop-file-utils

BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0)
# BuildRequires: pkgconfig(libido3-0.1)
BuildRequires: pkgconfig(indicator3-0.4)
BuildRequires: pkgconfig(libwnck-3.0)


%description
Wingpanel is the panel from the elementary project, used in its pantheon shell.


%prep
%setup -q


%build
%cmake # -DNO_INDICATOR_NG=on -DOLD_LIB_IDO=on


%install
make install DESTDIR=$RPM_BUILD_ROOT

desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/wingpanel.desktop

%find_lang wingpanel


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datarootdir}/glib-2.0/schemas &> /dev/null


%files -f wingpanel.lang
%{_bindir}/wingpanel

%{_datarootdir}/applications/wingpanel.desktop
%{_datarootdir}/glib-2.0/schemas/org.pantheon.desktop.wingpanel.gschema.xml

%{_datarootdir}/icons/hicolor/scalable/apps/wingpanel.svg


%changelog
* Sat Mar 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev208-8
- Update to latest bzr snapshot.

* Sun Feb 01 2015 Fabio Valentini (fafa) <decathorpe@gmail.com> - 0.3~rev201-7
- Update to latest bzr snapshot.

* Fri Jan 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev200-6
- Update to latest bzr snapshot.

* Sun Jan 18 2015 Fabio Valentini <decathorpe@gmail.com> - 0.3~rev198-5
- Update to latest bzr snapshot.

* Tue Jan 13 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3~rev196-4
- Update to latest bzr snapshot.

* Mon Jan 05 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3~rev195-3
- Fix upstream version.

* Sat Jan 03 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev195-2
- Cleaned up spec file.

* Fri Jan 02 2015 Fabio Valentini <fafatheone@gmail.com> - 0.3.0~rev195-1
- Initial package.
