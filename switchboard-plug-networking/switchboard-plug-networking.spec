%define rev 154
%define debug_package %{nil}

Summary: Switchboard System Settings Networking Plug
Name: switchboard-plug-networking
Version: 0.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-networking

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(libnm-glib)
BuildRequires: pkgconfig(libnm-gtk)
BuildRequires: pkgconfig(polkit-gobject-1)
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Network Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-network-plug


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-network-plug.lang
%{_libdir}/switchboard/network/pantheon-network


%changelog
* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1~rev154-1
- Initial package.



