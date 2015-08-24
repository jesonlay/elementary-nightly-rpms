%define rev 252
%define debug_package %{nil}

Summary: Switchboard System Settings Power Plug
Name: switchboard-plug-power
Version: 0.2.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-power

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(gnome-settings-daemon)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Power Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-power-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-power.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f pantheon-power-plug.lang
%{_libdir}/switchboard/hardware/pantheon-power/
%{_datadir}/applications/pantheon-plug-power.desktop


%changelog
* Mon Aug 24 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev252-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev251-1
- Initial package.



