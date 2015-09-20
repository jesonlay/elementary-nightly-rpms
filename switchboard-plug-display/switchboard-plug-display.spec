%define rev 108
%define debug_package %{nil}

Summary: Switchboard System Settings Display Plug
Name: switchboard-plug-display
Version: 0.1.1~rev%{rev}
Release: 0%{?dist}
License: LGPLv3
URL: http://launchpad.net/switchboard-plug-display

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(clutter-gtk-1.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Display Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-display-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-display.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f pantheon-display-plug.lang
%{_libdir}/switchboard/hardware/pantheon-display
%{_datadir}/applications/pantheon-plug-display.desktop


%changelog
* Fri Sep 04 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev107-2
- rebuild trigger for granite soname bump

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev107-1
- Initial package.


