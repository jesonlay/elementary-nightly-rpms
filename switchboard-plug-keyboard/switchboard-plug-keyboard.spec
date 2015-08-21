%define rev 353
%define debug_package %{nil}

Summary: Switchboard System Settings Keyboard Plug
Name: switchboard-plug-keyboard
Version: 0.2.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-keyboard

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
Modular Desktop Settings Hub Keyboard Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-keyboard-plug


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null

%postun
/sbin/ldconfig
/usr/bin/glib-compile-schemas %{_datadir}/glib-2.0/schemas &> /dev/null


%files -f pantheon-keyboard-plug.lang
%{_libdir}/switchboard/hardware/pantheon-keyboard


%changelog
* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.1~rev353-1
- Initial package.



