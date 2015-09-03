%define rev 78
%define debug_package %{nil}

Summary: Switchboard System Settings Date and Time Plug
Name: switchboard-plug-datetime
Version: 0.1.0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-datetime

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Date and Time Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-datetime-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-datetime.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f pantheon-datetime-plug.lang
%{_libdir}/switchboard/system/pantheon-datetime
%{_datadir}/applications/pantheon-plug-datetime.desktop


%changelog
* Thu Sep 03 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev78-1
- Update to new upstream snapshot.

* Tue Sep 01 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev76-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.0.1~rev75-1
- Initial package.


