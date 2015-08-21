%define rev 365
%define debug_package %{nil}

Summary: Switchboard System Settings Pantheon Shell Plug
Name: switchboard-plug-pantheon-shell
Version: 0.2.0.3~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: http://launchpad.net/switchboard-plug-pantheon-shell

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildRequires: cmake
BuildRequires: desktop-file-utils
BuildRequires: gettext
BuildRequires: vala

BuildRequires: pkgconfig(glib-2.0)
BuildRequires: pkgconfig(gnome-desktop-3.0)
BuildRequires: pkgconfig(granite)
BuildRequires: pkgconfig(gtk+-3.0) >= 3.14
BuildRequires: pkgconfig(plank) >= 0.7.1.1137
BuildRequires: pkgconfig(switchboard-2.0)


%description
Modular Desktop Settings Hub Pantheon Shell Plug


%prep
%setup -q


%build
%cmake
%make_build


%install
%make_install
%find_lang pantheon-desktop-plug


%check
# Pantheon not recognised as DE in OnlyShowIn, so ignore for now
# desktop-file-validate $RPM_BUILD_ROOT/%{_datadir}/applications/pantheon-plug-shell.desktop


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files -f pantheon-desktop-plug.lang
%{_libdir}/switchboard/personal/pantheon-desktop
%{_datadir}/applications/pantheon-plug-shell.desktop


%changelog
* Fri Aug 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.2.0.3~rev365-1
- Initial package.



