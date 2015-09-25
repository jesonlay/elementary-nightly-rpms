%define rev 65

Summary: Pantheon xsession settings
Name: pantheon-xsession-settings
Version: 0.5~rev%{rev}
Release: 1%{?dist}
License: GPLv3
URL: https://code.launchpad.net/~elementary-os/elementaryos/pantheon-xsession-settings

Source0: %{name}-%{version}.tar.gz
Source1: %{name}.conf

BuildArch: noarch

#BuildRequires: cmake
#BuildRequires: desktop-file-utils
#BuildRequires: gettext
#BuildRequires: vala

#BuildRequires: pkgconfig(granite)
#BuildRequires: pkgconfig(gtk+-3.0) >= 3.12
#BuildRequires: pkgconfig(switchboard-2.0)


Requires: cerbere
Requires: gnome-session
Requires: gnome-settings-daemon


%description
Pantheon xsession settings


%prep
%setup -q


%build
rm autostart/cerbere.desktop


%install
mkdir -p $RPM_BUILD_ROOT/%{_sysconfdir}/xdg/autostart/
mkdir -p $RPM_BUILD_ROOT/%{_datadir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/gnome-session/sessions
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/pantheon
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/wayland-sessions
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/xsessions

ln -s %{_datadir}/applications/cerbere.desktop $RPM_BUILD_ROOT/%{_sysconfdir}/xdg/autostart/cerbere.desktop

install autostart/* $RPM_BUILD_ROOT/%{_sysconfdir}/xdg/autostart/
install xsessions/pantheon.desktop $RPM_BUILD_ROOT/%{_datadir}/xsessions/
install wayland-sessions/pantheon-wayland.desktop $RPM_BUILD_ROOT/%{_datadir}/wayland-sessions/
install gnome-session/pantheon.session $RPM_BUILD_ROOT/%{_datadir}/gnome-session/sessions/
install applications/* $RPM_BUILD_ROOT/%{_datadir}/pantheon/


%check


%clean
rm -rf $RPM_BUILD_ROOT


%post
%postun


%files
%config %{_sysconfdir}/xdg/autostart/*
%{_datadir}/gnome-session/sessions/pantheon.session
%{_datadir}/pantheon/
%{_datadir}/xsessions/pantheon.desktop
%{_datadir}/wayland-sessions/pantheon-wayland.desktop


%changelog
* Mon Sep 21 2015 Fabio Valentini <decathorpe@gmail.com> - 0.5~rev65-1
- Remove no longer shipped GConf files. Added wayland session.

* Mon Sep 07 2015 Fabio Valentini <decathorpe@gmail.com> - 0.5~rev63-1
- Initial package.


