%define rev 18
%define debug_package %{nil}

Summary: Switchboard System Settings Mouse and Touchpad Plug
Name: switchboard-plug-mouse-touchpad
Version: 0.1.1~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-mouse-touchpad

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gthread-2.0)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Mouse and Touchpad Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-mouse-touchpad


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-mouse-touchpad.lang
%{_libdir}/switchboard/hardware/pantheon-mouse-touchpad


%changelog
* Sun Aug 23 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev18-1
- Update to new upstream snapshot.

* Sat Aug 22 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev17-1
- Update to new upstream snapshot.

* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.1.1~rev16-1
- Initial package.



