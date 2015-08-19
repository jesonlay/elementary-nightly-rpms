%define rev 154

Summary: The elementary continuation of Shotwell, originally written by Yorba Foundation.
Name: pantheon-photos
Version: 0.1.1~rev%{rev}
Release: 1%{?dist}
License: GPLv2, LGPLv2.1, CC-BY-SA
URL: http://launchpad.net/pantheon-photos

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake pkgconfig
BuildRequires: vala gettext

#BuildRequires: pkgconfig(granite)
#BuildRequires: pkgconfig(gtk+-3.0) >= 3.11.6


#Requires: contractor


%description
The elementary continuation of Shotwell, originally written by Yorba Foundation.

Designed for elementary OS. Works and looks great on any GTK+ desktop.


%prep
%autosetup


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-photos


%clean
rm -rf $RPM_BUILD_ROOT


%post
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f pantheon-photos.lang


%changelog


