%define rev 816

Summary: The official elementary calendar
Name: maya
Version: 0.3.1.1~rev%{rev}
Release: 0%{?dist}
License: GPLv3
URL: http://launchpad.net/maya

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: pkgconfig
BuildRequires: vala

BuildRequires: pkgconfig(champlain-0.12)
BuildRequires: pkgconfig(champlain-gtk-0.12)
BuildRequires: pkgconfig(clutter-1.0)
BuildRequires: pkgconfig(folks)
BuildRequires: pkgconfig(gee-0.8)
BuildRequires: pkgconfig(geocode-glib-1.0)
BuildRequires: pkgconfig(gio-2.0)
BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gobject-2.0)
BuildRequires: pkgconfig(gmodule-2.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.11.6
BuildRequires: pkgconfig(libecal-1.2) >= 3.8.0
BuildRequires: pkgconfig(libical)

#Requires: contractor


%description
A slim, lightweight GTK+3 calendar app written in Vala, designed for elementary OS. Also looks and works great on other GTK+ desktops.

In elementary OS, Maya is known as Calendar.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang maya


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f maya.lang
%doc AUTHORS
%license COPYING



%changelog


